import os
import time

import datetime

from .articles import articles_bp
from ..decorators import *
from ..db import *

from .security import *

@articles_bp.route("/constructor", methods=["GET", "POST"])
@user_only
def constructor_new():
    if request.method == "POST":
        title = request.form["title"]
        comment = request.form["comment"]
        data = request.form["data"]

        if not title or not data:
            return render_template("error.html", error="Неверно переданы данные.")

        title = secure_title(title)
        if len(title) <= 0 or title == ".":
            return render_template("error.html", error="Недопустимое название статьи.")

        data = data.replace("`", '"')

        permittable, erroneus_tag = tags.permittable(data)
        if not permittable:
            return render_template("error.html", error=f"Статья содержит запрещённый элемент ({erroneus_tag})")

        db = get_db()
        art = db.execute("SELECT * FROM articles WHERE title = ?", (title,)).fetchone()

        if not art:
            if not comment:
                comment = "Статья создана."

            fpath = os.path.join(current_app.config["ARTICLE_DIR"], title)
            fname = str(int(time.time()))

            fullpath = os.path.join(fpath, fname)

            if not os.path.exists(fpath):
                os.makedirs(fpath)

            with open(fullpath, "w") as f:
                f.write(data)

            p = [{"fpath": fpath, "body": fullpath, "last_edit_by": g.user["username"], "editdate": datetime.datetime.now().strftime("%I:%M%p в %B %d %Y"), "comment": comment}]

            db.execute("INSERT INTO articles VALUES(?, ?, ?)", (title, json.dumps(p), g.user["username"]))
            db.execute("UPDATE users SET commit_n = commit_n+1 WHERE username = ?", (g.user["username"],))

            db.commit()
        else:
            if not comment:
                return render_template("error.html", error="При редактировании статьи комментарий обязателен.")

            artdata = json.loads(art["data"])
            body = os.path.join(artdata[-1]["fpath"], str(int(time.time())) + ".html",)
            b = {"fpath": artdata[-1]["fpath"], "body": body, "last_edit_by": g.user["username"], "editdate": datetime.datetime.now().strftime("%I:%M%p в %B %d %Y"), "comment": comment}
            artdata.append(b)
            with open(body, "w") as f:
                f.write(data)
            db.execute("UPDATE articles SET data = ? WHERE title = ?", (json.dumps(artdata), title))
            db.execute("UPDATE users SET commit_n = commit_n+1 WHERE username = ?", (g.user["username"],))

            db.commit()

        return redirect("/")
    else:
        return render_template("articles/constructor_modern.html")
