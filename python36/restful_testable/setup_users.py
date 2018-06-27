import json
import os
import sys
import argparse
from typing import List

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from auth.authenticate import authenticate, identity
from resources import Calculator
from auth import auth_db
from auth.models.user import User


def main(argv: List[str]) -> None:
    parser = argparse.ArgumentParser(description='Create and populate User DB')

    parser.add_argument('-c',
                        '--cfg-path',
                        required=True,
                        help="Path to the user configuration data to load.")

    parser.add_argument('-d',
                        '--db-path',
                        required=True,
                        help='Path to database file.')

    cfg = vars(parser.parse_args(argv))

    # Load the user configuration data.
    with open(cfg["cfg_path"], 'rt') as fp:
        users_cfg = json.load(fp=fp)

    # Delete the database file if it exists.
    if os.path.exists(cfg["db_path"]):
        os.remove(cfg["db_path"])

    # Create the Flask application as the container for the User object and database access.
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{cfg['db_path']}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the database
    auth_db.init_app(app)
    app.app_context().push()
    auth_db.create_all()

    # Create the users in the DB
    for user_data in users_cfg["users"]:
        user = User(**user_data)
        user.save()


if __name__ == '__main__':
    main(sys.argv[1:])
