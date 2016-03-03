from flask import Blueprint
from flask import jsonify
from flask import request
from notebook.models import Note

notebook_api = Blueprint("notebook_api", __name__)

@notebook_api.route("/", methods=['GET'])
def index():
    # return api discovery string
    return "You've discovered notebook api!"

@notebook_api.route("/about/", methods=['GET'])
def about():
    return "simple notebook app"

@notebook_api.route("/notes/", methods=["GET"])
def get_notes():
    notes = Note.get_sample_notes()
    return jsonify(notes)

@notebook_api.route("/notes/", methods=["POST"])
def post_product_builds():
    data = request.json['data']
    # create new note
    note = {'id': 5, 'data': data}
    return jsonify(note)

@notebook_api.route("/notes/<int:note_id>/", methods=["GET"])
def get_product_build(note_id):
    note = {'id':note_id, 'data': 'this is note with id {}'.format(note_id)}
    return jsonify(note)

@notebook_api.route("/notes/<int:note_id>/", methods=["PUT"])
def put_product_build(note_id):
    note = request.json
    return jsonify(note)

@notebook_api.route("/notes/<int:note_id>/", methods=["DELETE"])
def delete_product_build(note_id):
    return jsonify({"result" : True})

