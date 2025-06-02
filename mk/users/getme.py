from flask import *

from .users import user_bp
from ..decorators import *
from ..db import *

@user_bp.route("/getme", methods=["GET", "POST"])
@user_only
def get_me():
    db = get_db()

    if request.method == "POST":
        pass
    else:
        user = db.execute("SELECT * FROM users WHERE username = ?", (g.user["username"],)).fetchone()
        return render_template("users/me.html", user=user)
