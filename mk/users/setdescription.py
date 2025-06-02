from flask import *

from .users import user_bp
from ..decorators import *
from ..db import *

@user_bp.route("/setdescription", methods=["POST"])
@user_only
def set_description():
    description = request.form["description"]

    if not description:
        return render_template("error.html", error="Не указано описание.")

    db = get_db()
    user = db.execute("UPDATE users SET profile_description = ? WHERE username = ?", (description, g.user["username"]))
    db.commit()

    return redirect(url_for("users.get_me"))
