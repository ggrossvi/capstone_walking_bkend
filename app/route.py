from flask import Blueprint, jsonify

walking_buddy_bp = Blueprint("walking_buddy", __name__, url_prefix='/walking_buddy')

@walking_buddy_bp.route("",methods=["GET"])
def get_walking_buddy():
    my_response = "Hello,Walking Buddy!"
    return jsonify(my_response),200

@walking_buddy_bp.route('/JSON', methods=["GET"])
def walking_json():
    return {
        "name": "Gloria",
        "message": "Heya!",
        "hobbies": ["Coding", "Writing"],
    }, 200


