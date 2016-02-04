from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from notebook.models import Note

client_application = Blueprint("client_application", __name__, template_folder="templates", static_folder="static")

@client_application.route("/", methods=["GET"])
def index():
    return redirect(url_for(".notebook"))

@client_application.route("/notebook/", methods=["GET"])
def notebook():
    notes = Note.get_sample_notes()
    return render_template("main.jinja", notes=notes)
