from app.models.buddy import Buddy
from flask import Blueprint, jsonify,request
from app import db

buddy_bp = Blueprint("buddy_bp", __name__, url_prefix='/buddy')

@buddy_bp.route("",methods=["POST"])
def create_buddy():
    request_body = request.get_json()
    buddy = Buddy(
        first_name = request_body["first_name"],
        last_name = request_body["last_name"],
        address = request_body["address"],
        apt = request_body["apt"],
        city = request_body["city"],
        state = request_body["state"],
        zipcode = request_body["zipcode"],
        email = request_body["email"],
        morning = request_body["morning"],
        afternoon = request_body["afternoon"],
        evening = request_body["evening"],
        bio = request_body["bio"]
    )
    db.session.add(buddy)
    db.session.commit()
    my_response = "Successfully created new user"
    return jsonify(my_response),200

@buddy_bp.route('', methods=["GET"])
def get_all_users():
    buddies = Buddy.query.all()
    if buddies == None:
        return jsonify({"Error:": "No Buddies found!"},404)
    else:
        response = []
        for buddy in buddies:
            response.append(buddy.to_json())
        return jsonify(response),200

@buddy_bp.route('/zip/<zip>', methods=["GET"])
def get_all_users_zip(zip):

    # get sort query param
    
    
    buddies = Buddy.query.filter_by(zipcode=zip)
    print("buddies",buddies)
    print(buddies.count())
    if buddies.count() == 0:
        return jsonify({"No Buddies found!"},204)
    else:
        response = []
        for buddy in buddies:
            response.append(buddy.to_json())
        return jsonify(response),200

@buddy_bp.route('/email/<email>', methods=["GET"])
def get_user_email(email):

    # get sort query param
    
    
    buddies = Buddy.query.filter_by(email=email)
    print("buddies",buddies)
    print(buddies.count())
    if buddies.count() == 0:
        return jsonify({"message": "User not found"},404)
    else:
        response = []
        for buddy in buddies:
            response.append(buddy.to_json())
        return jsonify(response),200

#Get Specific Buddy
# @buddy_bp.route('/<buddy_id>', methods = ['GET','PUT', 'DELETE'])  
# def handle_goal(buddy_id):
#     buddy = Buddy.query.get(buddy_id)
#     if not buddy:
#         return "", 404

#     if request.method == 'GET':
#         #check expected output in test
#         return({
#             'goal':
#                 goal.serialize()
            
#         })
#     elif request.method == 'PUT':
#         request_body = request.get_json()
#         if 'title' in request_body:
#             goal.title = request_body['title']
#         db.session.commit()
#         return({
#             'goal': goal.serialize()
#         },200)
    
#     elif request.method =='DELETE':
#         db.session.delete(goal)
#         db.session.commit()
#         return({
#             "details": f'Goal {goal_id} "{goal.title}" successfully deleted'
#         },200)

# make this zip === zip and morning === morning or afternoon === afternoon or evening === evening
# @buddy_bp.route('/zip/<zip>', methods=["GET"])
# def get_all_users_zip(zip):

#     # get sort query param
    
    
#     buddies = Buddy.query.filter_by(zipcode=zip)
#     print("buddies",buddies)
#     print(buddies.count())
#     if buddies.count() == 0:
#         return jsonify({"No Buddies found!"},204)
#     else:
#         response = []
#         for buddy in buddies:
#             response.append(buddy.to_json())
#         return jsonify(response),200

@buddy_bp.route('/JSON', methods=["GET"])
def walking_json():
    return {
        "name": "Gloria",
        "message": "Heya!",
        "hobbies": ["Coding", "Writing"],
    }, 200


# @buddy_bp.route('/<buddy_id>', methods = ['GET','PUT', 'DELETE'])  
# def handle_buddy(buddy_id):
#     buddy = Buddy.query.get(buddy_id)
#     if not buddy:
#         return "", 404

#     if request.method == 'GET':
#         #check expected output in test
#         return({
#             'buddy':
#                 buddy.to_json()
            
#         })
#     elif request.method == 'PUT':
#         # # ?????? What do I need to put in request body
#         # request_body = request.get_json()
#         # if 'name' in request_body:
#         #     buddy.name = request_body['name']
#         # db.session.commit()
#         # return({
#         #     'buddy': buddy.to_json()
#         # },200)
#         pass
    
#     elif request.method =='DELETE':
#         db.session.delete(buddy)
#         db.session.commit()
#         return({
#             "details": f'Buddy {buddy_id} "{buddy.name}" successfully deleted'
#         },200)
