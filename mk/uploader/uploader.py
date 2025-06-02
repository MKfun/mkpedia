import os
import pathlib

import time

from flask import *
from ..db import *

from ..decorators import user_only

from werkzeug.utils import secure_filename

uploader_bp = Blueprint("uploader", __name__, url_prefix="/uploader")

ALLOWED_FILE_EXTS = [".png", ".jpg", ".gif"]

def file_is_allowed(filename: str):
    ext = pathlib.Path(filename).suffix
    return ext in ALLOWED_FILE_EXTS

@uploader_bp.route("/storage/<path:filename>")
@user_only
def storage(filename):
    p = os.path.join(current_app.instance_path, "storage")

    fullp = os.path.join(p, filename)

    print(fullp)

    if not os.path.exists(p):
        os.makedirs(p)
        return render_template("not_found.html")

    if os.path.exists(fullp):
        return send_from_directory(p, filename)
    else:
        return render_template("not_found.html")

@uploader_bp.route("/upload", methods=["GET", "POST"])
@user_only
def upload_file():
    if request.method == "POST":
        p = os.path.join(current_app.instance_path, "storage")

        if not "file" in request.files:
            return render_template("not_found.html")

        file = request.files["file"]

        if file.filename == "":
            return render_template("not_found.html")

        filename = secure_filename(file.filename)

        if file_is_allowed(filename):
            if not os.path.exists(p):
                os.makedirs(p)

            actual_filename = str(int(time.time())) + "_" + g.user["username"] + "_" + filename
            p = os.path.join(p, actual_filename)

            slash_path = "/uploader/storage/" + actual_filename

            file.save(p)
            return render_template("uploads/file_demonstration.html", img_src=slash_path)
        else:
            return render_template("not_found.html")

        return render_template("not_found.html")
    else:
        return render_template("uploads/uploader.html")
