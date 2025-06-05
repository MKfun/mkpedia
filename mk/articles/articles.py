import os
import time

import json

from flask import *
from ..database import *

from ..decorators import user_only

articles_bp = Blueprint("articles", __name__, url_prefix="/articles")

def get_list():
    allarts = Article.query.all()
    arts = []

    for i in allarts:
        arts.append({"title": i.title})

    return arts

@articles_bp.route("/getlist", methods=["GET"])
def listall():
    return render_template("articles/article_list.html", article_list=get_list())

@articles_bp.route("/rawlist", methods=["GET"])
def raw_list():
    return get_list()
