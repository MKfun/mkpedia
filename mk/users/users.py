from flask import *

from ..database import *
from ..decorators import *

from .getcommitsform import *

user_bp = Blueprint("users", __name__, url_prefix="/users")

def set_admin(v: bool):
    username = request.args.get("username")

    if not username:
        return render_template("not_found.html")

    user = User.query.filter_by(username=username).first()

    if not user:
        return render_template("error.html", error="Пользователь не найден!")
    elif user.username == "root":
        return render_template("error.html", error="Пошёл нахуй уёбище, ты куда лезешь падла блять очкастая нахуй.")

    user.admin = v
    db.session.commit()

    return redirect(url_for("users.user_list"))

@user_bp.route("/getlist")
@user_only
def user_list():
    return render_template("users/user_list.html", users=User.query.all())

@user_bp.route("/getuser")
@user_only
def get_user():
    username = request.args.get("username")

    if not username:
        return render_template("not_found.html")

    user = User.query.filter_by(username=username).first()

    return render_template("users/user.html", user=user, formatted_commits=getcommitsform(user.commit_n))

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

    User.query.filter_by(username=username).delete()
    db.session.commit()

    return redirect(url_for("users.user_list"))
