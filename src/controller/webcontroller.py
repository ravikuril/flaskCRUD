
from flask import Blueprint

webcontroller = Blueprint('webcontroller', __name__)
@webcontroller.route('/api/v1/web/endpoint', methods=['GET'])
def show_doctor():
    return ("web controller testing")
