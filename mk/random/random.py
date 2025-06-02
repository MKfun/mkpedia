import os
import random

from flask import *
from ..db import *

random_bp = Blueprint("random", __name__, url_prefix="/random")

@random_bp.route("/404", methods=["GET"])
def fourofour():
    d = os.path.join(current_app.root_path, "static", "404_photos")
    if not os.path.exists(d):
        os.makedirs(d)

    flist = os.listdir(d)

    if len(flist) == 0:
        return send_from_directory("static", "404.png")

    return send_from_directory(d, random.choice(flist))

@random_bp.route("/error", methods=["GET"])
def error():
    d = os.path.join(current_app.root_path, "static", "error_photos")
    if not os.path.exists(d):
        os.makedirs(d)

    flist = os.listdir(d)

    if len(flist) == 0:
        return send_from_directory("static", "404.png")

    return send_from_directory(d, random.choice(flist))
