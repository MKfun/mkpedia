import hashlib
import functools
from flask import *

from ..database import *

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if request.cookies.get("has_an_account") is not None and request.cookies.get("has_an_account") == "1":
            return render_template("error.html", error="Доступно только пользователям без аккаунта.")

        username = request.form["username"]
        password = request.form["password"]

        if not username or not password:
            return render_template("error.html", error="Username AND password are required!")

        if len(username) > 32 or len(password) > 32:
            return render_template("error.html", error="Слишком длинное имя пользователя или пароль!")

        if db.session.execute(db.select(User).filter_by(username=username)).first() is not None or db.session.execute(db.select(Queue).filter_by(username=username)).first() is not None:
            return render_template("error.html", error="Имя пользователя уже занято или есть в очереди!")

        q = Queue(username, password)

        db.session.add(q)
        db.session.commit()

        r = make_response(redirect("/auth/login"))
        r.set_cookie("has_an_account", "1")

        return r

    elif request.method == "GET":
        return render_template("/auth/register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not username or not password:
            return render_template("error.html", error="Username AND password are required!")

        if len(username) > 32 or len(password) > 32:
            return render_template("error.html", error="Слишком длинное имя пользователя или пароль!")

        h = User.query.filter_by(username=username).first()

        if h is None:
            return render_template("error.html", error="User not found!")

        pwdhash = hashlib.sha256(password.encode("utf-8")).hexdigest()

        if h.pwdhash == pwdhash:
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
        user = db.session.execute(db.select(User).filter_by(username=username)).first()
        if not user:
            g.user = None
        elif user[0].pwdhash == pwdhash:
            g.user = user[0]

# todo: хэшировать пароли нах. СДЕЛАНО НАХ.
