import hashlib

from flask import *

from ..db import *

from ..decorators import admin_only, root_only

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/panel", methods=["GET", "POST"])
@admin_only
def render_panel():
    if request.method == "POST":
        if not g.user["username"] == "root":
            return render_template("not_admin.html")

        newpwd = request.form["new_password"]

        if not newpwd:
            return render_template("not_found.html")

        pwdhash = hashlib.sha256(newpwd.encode("utf-8")).hexdigest()

        db = get_db()

        db.execute("UPDATE users SET hash = ? WHERE username = 'root'", (pwdhash,))
        db.commit()

        session.clear()

        return redirect("/")

    db = get_db()

    queue = db.execute("SELECT * FROM queue").fetchall()
    return render_template("/admin/panel.html", queue=queue, is_root=g.user["username"]=="root")

@admin_bp.route("/reject", methods=["GET"])
@admin_only
def reject():
    db = get_db()

    username = request.args.get("username")

    if not username:
        return render_template("error.html", error="Не указан username.")

    db.execute("DELETE FROM queue WHERE username = ?", (username,))
    db.commit()

    return redirect(url_for("admin.render_panel"))

@admin_bp.route("/accept", methods=["GET"])
@admin_only
def accept():
    db = get_db()

    username = request.args.get("username")

    if not username:
        return render_template("error.html", error="Не указан username.")

    q = db.execute("SELECT * FROM queue WHERE username = ?", (username,)).fetchone()
    pwdhash = q["hash"]

    db.execute("DELETE FROM queue WHERE username = ?", (username,))
    db.execute("INSERT INTO users VALUES (?, ?, 0, ?, 0)", (username, pwdhash, ""))

    db.commit()

    return redirect(url_for("admin.render_panel"))
