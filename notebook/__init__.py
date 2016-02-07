from flask import Flask
from flask import current_app as app
from notebook.api import notebook_api
from notebook.frontend import client_application

API_VERSION='v1'

def load_config(app, cfgfile, cfgobj):
    if cfgfile is not None:
        app.config.from_pyfile(cfgfile)
    if cfgobj is not None:
        app.config.from_object(cfgobj)
    else:
        print("No config specified. Using Defaults!")

def create_app(cfgfile=None, cfgobj=None):
    app = Flask(__name__, static_folder=None)
    app.secret_key = '\xfe\x060|\xfb\xf3\xe9F\x0c\x93\x95\xc4\xbfJ\x12gu\xf1\x0cP\xd8\n\xd5'

    load_config(app, cfgfile, cfgobj)

    # register flask blueprints for front end and rest api
    app.register_blueprint(
            client_application,
            url_prefix="")

    app.register_blueprint(
            notebook_api,
            url_prefix="/api/{}".format(API_VERSION))

    return app
