from flask import *

from ..db import *
from ..decorators import *

user_bp = Blueprint("users", __name__, url_prefix="/users")

def set_admin(v: bool):
    username = request.args.get("username")

    if not username:
        return render_template("not_found.html")

    db = get_db()

    user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

    if not user:
        return render_template("error.html", error="Пользователь не найден!")
    elif user["username"] == "root":
        return render_template("error.html", error="Пошёл нахуй уёбище, ты куда лезешь падла блять очкастая нахуй")

    db.execute("UPDATE users SET admin = ? WHERE username = ?", (v, username))
    db.commit()

    return redirect(url_for("users.user_list"))

@user_bp.route("/getlist")
@user_only
def user_list():
    db = get_db()
    return render_template("users/user_list.html", users=db.execute("SELECT * FROM users").fetchall())

@user_bp.route("/getuser")
@user_only
def get_user():
    username = request.args.get("username")

    if not username:
        return render_template("not_found.html")

    db = get_db()

    user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

    return render_template("users/user.html", user=user)

@user_bp.route("/promote")
@admin_only
def promote():
    return set_admin(True)

@user_bp.route("/demote")
@admin_only
def demote():
    return set_admin(False)

@user_bp.route("/delete")
@root_only
def delete():
    username = request.args.get("username")

    if not username:
        return render_template("not_found.html")
    elif username == "root":
        return render_template("error.html", error="IDI NAXUI")

    db = get_db()

    db.execute("DELETE FROM users WHERE username = ?", (username,))
    db.commit()

    return redirect(url_for("users.user_list"))
