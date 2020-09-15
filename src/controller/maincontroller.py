import os

from flask import jsonify, request, Flask
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "/.."))
from models.models import Doctor
from app import flask
from app import db

@flask.route('/test', methods=['GET'])
def show_doctor1():
    return ("testing")



@flask.route('/api/v1/doctors/<id>', methods=['GET'])
def show_doctor(id):
    try:
        doctor = Doctor.query.filter_by(id=id).first()
        return jsonify(doctor.serialize)
    except:
        return not_found("Doctor does not exist")

#endpoint of [post]
@flask.route('/api/v1/doctors/', methods=['POST'])
def create_doctor():
    if not request.is_json or 'name' not in request.get_json():
        return bad_request('Missing required data.')
    doctor = Doctor(id=request.get_json()['id'],name=request.get_json()['name'])
    db.session.add(doctor)
    db.session.commit()
    return jsonify({'doctor': doctor.serialize}), 201



# endpoint to update user
@flask.route("/api/v1/doctors/update/<id>", methods=["PUT"])
def user_update(id):
    doctor = Doctor.query.get(id)
    name = request.json['name']

    doctor.name = name
    db.session.commit()
    return jsonify(doctor.serialize)


# endpoint to delete doctor
@flask.route("/api/v1/doctors/delete/<id>", methods=["DELETE"])
def user_delete(id):
    #doctor = Doctor.query.get(id)
    record_obj = db.session.query(Doctor).filter(Doctor.id == id).first()
    db.session.delete(record_obj)
    db.session.commit()
    return '200'








# Custom Error Helper Functions
def bad_request(message):
    response = jsonify({'error': message})
    response.status_code = 400
    return response

def not_found(message):
    response = jsonify({'error': message})
    response.status_code = 404
    return response


if __name__ == '__main__':
    debug = False
    flask.run(host="0.0.0.0", port=8080, debug=debug)
