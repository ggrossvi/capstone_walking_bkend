from flask import Blueprint

walking_buddy_bp = Blueprint("walking_buddy", __name__, url_prefix='/walking_buddy')

@walking_buddy_bp.route("",methods=["GET"])
def get_walking_buddy():
    my_response = "Hello,Walking Buddy!"
    return my_response


