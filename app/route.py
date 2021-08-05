from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route ('/hello-world', methods=["GET"])
def get_hello_world():
    my_response = "Hello,World!"
    return my_response
