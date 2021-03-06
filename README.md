 **Description:**
 Walking Buddy is a React Web App that helps users be matched up with a walking buddy.  
 It allows users to make a calendar appointment with a buddy to walk. In progress: Ask Alexa how many buddies are in my zip code.  

 Tech Stack:
 * React 
 * React Router
 * Flask
 * Python
 
## Buddy related endpoints

Each endpoint manipulates or displays information related to the User whose Token is provided with the request:

* [Show all buddies](user/get.md) : `GET /buddy`
* [Show buddies by zip code](user/get.md) : `GET /buddy/zip/<zip>`
* [Show buddy email](user/get.md) : `GET /buddy/email/<email>`
* [Show buddy id](user/get.md) : `GET /buddy/<buddy_id>`
* [Show buddy zip and time preference](user/get.md) : `GET /buddy/zip/<zip>/morning/<morning>/afternoon/<afternoon>/evening/<evening>`
* [Show buddy JSON](user/get.md) : `GET /buddy/JSON`

* [Update info](user/get.md) : `PUT /buddy/<buddy_id>`
* [Create buddy](user/put.md) : `POST /buddy`
* [Register buddy](user/put.md) : `POST /buddy/register`
* [Create buddy email](user/get.md) : `POST /buddy/email/<email>`
* [Delete buddy info](user/get.md) : `DELETE /buddy/<buddy_id>`

### Show all buddies

Get the details of buddies.

**URL** : `/buddy`

**Method** : `GET`

**Auth required** : No

**Permissions required** : None

#### Success Response

**Code** : `200 OK`

**Content examples**

For a User with ID 1234 on the local database where that User has saved an email address and name information.

```json
[
    {
        "buddy_id": 1,
        "first_name": "Percy",
        "last_name": "Walker",
        "address": "Discovery Park" ,
        "apt": "Apt #4",
        "city": "Seattle",
        "state": "WA",
        "zipcode": "98177",
        "email": "percy@gmail.com",
        "morning": true,
        "afternoon": true,
        "evening": true,
        "bio": "I like to play catch"
    }
]
```

### Show buddies in zip code

Get the details of buddies by zip code.

**URL** : `/buddy/zip/<zip>`

**Method** : `GET`

**Auth required** : No

**Permissions required** : None

#### Success Response

**Code** : `200 OK`

**Content examples**

For a User with ID 1234 on the local database where that User has saved an email address and name information.

```json
[
    {
        "buddy_id": 1,
        "first_name": "Percy",
        "last_name": "Walker",
        "address": "Discovery Park" ,
        "apt": "Apt #4",
        "city": "Seattle",
        "state": "WA",
        "zipcode": "98177",
        "email": "percy@gmail.com",
        "morning": true,
        "afternoon": true,
        "evening": true,
        "bio": "I like to play catch"
    }
]
```
### Show all buddies

Get the details of buddies.

**URL** : `/buddy`

**Method** : `GET`

**Auth required** : No

**Permissions required** : None

#### Success Response

**Code** : `200 OK`

**Content examples**

For a User with ID 1234 on the local database where that User has saved an
email address and name information.

```json
[
    {
        "buddy_id": 1,
        "first_name": "Percy",
        "last_name": "Walker",
        "address": "Discovery Park" ,
        "apt": "Apt #4",
        "city": "Seattle",
        "state": "WA",
        "zipcode": "98177",
        "email": "percy@gmail.com",
        "morning": true,
        "afternoon": true,
        "evening": true,
        "bio": "I like to play catch"
    }
]
```






