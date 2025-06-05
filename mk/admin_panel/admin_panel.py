import hashlib

from flask import *

from ..db import *

from ..decorators import admin_only, root_only

from ..database import *

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/panel", methods=["GET", "POST"])
@admin_only
def render_panel():
    if request.method == "POST":
        if not g.user.username == "root":
            return render_template("not_admin.html")

        newpwd = request.form["new_password"]

        if not newpwd:
            return render_template("not_found.html")

        pwdhash = hashlib.sha256(newpwd.encode("utf-8")).hexdigest()

        root = User.query.filter_by(username="root").first()
        root.pwdhash = pwdhash

        db.session.commit()

        session.clear()

        return redirect("/")

    queue = Queue.query.all()
    return render_template("/admin/panel.html", queue=queue, is_root=g.user.username=="root")

@admin_bp.route("/reject", methods=["GET"])
@admin_only
def reject():
    username = request.args.get("username")

    if not username:
        return render_template("error.html", error="Не указан username.")

    Queue.query.filter_by(username=username).delete()
    db.session.commit()

    return redirect(url_for("admin.render_panel"))

@admin_bp.route("/accept", methods=["GET"])
@admin_only
def accept():
    username = request.args.get("username")

    if not username:
        return render_template("error.html", error="Не указан username.")

    q = Queue.query.filter_by(username=username).first()

    user = User(q.username, q.pwdhash, False, alreadyhash_pwd=True)

    print(user.pwdhash)

    Queue.query.filter_by(username=username).delete()
    db.session.add(user)

    db.session.commit()

    return redirect(url_for("admin.render_panel"))
