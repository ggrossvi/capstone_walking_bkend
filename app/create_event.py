from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from google.oauth2.credentials import Credentials

# additional imports
# https://gist.github.com/cwurld/9b4e10dbeecab28345a3
import httplib2
import os

# from apiclient import discovery
# import oauth2client
# from oauth2client import client
# from oauth2client import tools
import pytz
import datetime


def check_creds():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # service = build("calendar", "v3", credentials=creds)
    service = build("calendar", "v3", credentials=creds)
    return service


# If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SCOPES = ["https://www.googleapis.com/auth/calendar"]

# Create Calendar Event
# def get_credentials():
# # """Gets valid user credentials from storage.
# # If nothing has been stored, or if the stored credentials are invalid,
# # the OAuth2 flow is completed to obtain the new credentials.
# # Returns:
# #     Credentials, the obtained credential.
# # """
#     home_dir = os.path.expanduser('~')
#     credential_dir = os.path.join(home_dir, '.credentials')
#     if not os.path.exists(credential_dir):
#         os.makedirs(credential_dir)
#     credential_path = os.path.join(credential_dir,
#                                    'calendar-python-quickstart.json')

#     store = oauth2client.file.Storage(credential_path)
#     credentials = store.get()
#     if not credentials or credentials.invalid:
#         flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
#         flow.user_agent = APPLICATION_NAME
#         if flags:
#             credentials = tools.run_flow(flow, store, flags)
#         else: # Needed only for compatibility with Python 2.6
#             credentials = tools.run(flow, store)
#         print('Storing credentials to ' + credential_path)
#     return credentials

####


def next_ten_events():
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming 10 events")
    # events_result = service.events().list(calendarId='primary', timeMin=now,
    #                                     maxResults=10, singleEvents=True,
    #                                     orderBy='startTime').execute()
    # events = events_result.get('items', [])

    # if not events:
    #     print('No upcoming events found.')
    # for event in events:
    #     start = event['start'].get('dateTime', event['start'].get('date'))
    #     print(start, event['summary'])


def free_or_busy_time(service,email):
    # This event should be returned by freebusy empty busy [] means they are not busy
    tz = pytz.timezone("US/Central")
    today = datetime.date.today()
    print("1", today.year, today.month, today.day)
    today += datetime.timedelta(days=1)

    print("2", today)
    print("3", today.year, today.month, today.day)
    # from datetime import date

    # my_date = date.today()
    # my_datetime = datetime(my_date.year, my_date.month, my_date.day)
    # print(my_datetime)
    # convert our date into a datetime and add the 6 PM hour to it
    the_datetime = tz.localize(
        datetime.datetime(today.year, today.month, today.day, 18)
    )
    the_datetime2 = tz.localize(
        datetime.datetime(today.year, today.month, today.day, 19)
    )
    print(the_datetime, the_datetime2)
    body = {
        "timeMin": the_datetime.isoformat(),
        "timeMax": the_datetime2.isoformat(),
        "timeZone": "US/Central",
        "items": [{"id": email}],
    }

    eventsResult = service.freebusy().query(body=body).execute()
    import json

    print("eventsResult:", json.dumps(eventsResult))

    cal_dict = eventsResult[u"calendars"]
    for cal_name in cal_dict:
        print(cal_name, cal_dict[cal_name])
    if eventsResult["calendars"][email] == "busy":
        return "busy"


# Add event
def add_event(service,email):
    tz = pytz.timezone("US/Central")
    today = datetime.date.today()
    today += datetime.timedelta(days=1)
    start_datetime = tz.localize(
        datetime.datetime(today.year, today.month, today.day, 18)
    )
    stop_datetime = tz.localize(
        datetime.datetime(today.year, today.month, today.day, 19)
    )
    event = {
        "summary": "Let's go walking",
        "description": "An invitation from your walking buddy",
        "start": {
            "dateTime": start_datetime.isoformat(),
            "timeZone": "US/Central",
        },
        "end": {
            "dateTime": stop_datetime.isoformat(),
            "timeZone": "US/Central",
        },
        "attendees": [
            {"email": email}
            # {"email": "treasuresoftheandes@yahoo.com"},
        ],
    }
    # inserts event in calendar
    event = service.events().insert(calendarId="primary", body=event).execute()
    print("Event created: %s" % (event.get("htmlLink")))
    return "Event created: %s" % (event.get("htmlLink"))


def add_calendar_event(email):

    service = check_creds()
    # next_ten_events()
    free_or_busy_time(service,email)
    #getting msg back from function
    message = add_event(service,email)
    return message
#use when it is a flask app
# if __name__ == "__main__":
#     main()
