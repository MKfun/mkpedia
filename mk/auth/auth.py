import hashlib
import functools
from flask import *
from ..db import *

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if request.cookies.get("has_an_account") is not None and request.cookies.get("has_an_account") == "1":
            return render_template("error.html", error="Доступно только пользователям без аккаунта.")

        username = request.form["username"]
        password = request.form["password"]

        db = get_db()

        if not username or not password:
            return render_template("error.html", error="Username AND password are required!")

        if len(username) > 32 or len(password) > 32:
            return render_template("error.html", error="Слишком длинное имя пользователя или пароль!")

        try:
            if db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone() is not None or db.execute("SELECT * FROM queue WHERE username = ?", (username,)).fetchone() is not None:
                return render_template("error.html", error="Имя пользователя уже занято!")

            db.execute("INSERT INTO queue VALUES(?, ?)", (username, hashlib.sha256(password.encode("utf-8")).hexdigest()))
            db.commit()

            r = make_response(redirect("/auth/login"))
            r.set_cookie("has_an_account", "1")

            return r
        except db.IntegrityError:
            return render_template("error.html", error="Имя пользователя уже есть в очереди! Попробуйте позже!")
    elif request.method == "GET":
        return render_template("/auth/register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()

        if not username or not password:
            return render_template("error.html", error="Username AND password are required!")

        if len(username) > 32 or len(password) > 32:
            return render_template("error.html", error="Слишком длинное имя пользователя или пароль!")

        user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

        if user is None:
            return render_template("error.html", error="User not found!")

        pwdhash = hashlib.sha256(password.encode("utf-8")).hexdigest()

        if user["hash"] == pwdhash:
            session.clear()
            session["username"] = username
            session["pwdhash"] = pwdhash

        else:
            return render_template("error.html", error="Passwords don`t match!")

        return redirect("/")
    else:
        return render_template("auth/login.html")

@auth_bp.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect("/")

@auth_bp.before_app_request
def load_user():
    username = session.get("username")
    pwdhash = session.get("pwdhash")

    if username is None or pwdhash is None:
        g.user = None
    else:
        user = get_db().execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        if not user:
            g.user = None
        elif user["hash"] == pwdhash:
            g.user = user

# todo: хэшировать пароли нах. СДЕЛАНО НАХ.
