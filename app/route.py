from app.models.buddy import Buddy
from flask import Blueprint, jsonify,request
from app.models.buddy import Buddy
from app import db

buddy_bp = Blueprint("buddy", __name__, url_prefix='/buddy')

@buddy_bp.route("",methods=["POST"])
def create_buddy():
    request_body = request.get_json()
    buddy = Buddy(
        name = request_body["name"],
        zipcode = request_body["zipcode"],
        email = request_body["email"],
        morning = request_body["morning"],
        afternoon = request_body["afternoon"],
        evening = request_body["evening"]
    )
    db.session.add(buddy)
    db.session.commit()
    my_response = "Successfully created new user"
    return jsonify(my_response),200

@buddy_bp.route('', methods=["GET"])
def get_all_users():
    buddies = Buddy.query.all()
    response = []
    for buddy in buddies:
        response.append(buddy.to_json())
    return jsonify(response),200


@buddy_bp.route('/JSON', methods=["GET"])
def walking_json():
    return {
        "name": "Gloria",
        "message": "Heya!",
        "hobbies": ["Coding", "Writing"],
    }, 200


