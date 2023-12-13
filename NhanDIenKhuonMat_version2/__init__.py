from flask import Flask
from NhanDIenKhuonMat_version2.extension import db
import os
from flask_sse import sse


def create_db(app):
    if not os.path.exists("xla.db"):
        with app.app_context():
            db.create_all()
            print("Created DB!")


def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)


    db.init_app(app)
    create_db(app)

    create_db(app)

    return app
