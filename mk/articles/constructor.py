import os
import time

import datetime

from .articles import articles_bp
from ..decorators import *
from ..database import *

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

        art = Article.query.filter_by(title=title).first()
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

            p = [{"fpath": fpath, "body": fullpath, "last_edit_by": g.user.username, "editdate": datetime.datetime.now().strftime("%I:%M%p в %B %d %Y"), "comment": comment}]

            article = Article(title, json.dumps(p), g.user.username)
            user = User.query.filter_by(username=g.user.username).first()

            user.commit_n += 1

            db.session.add(article)
            db.session.commit()
        else:
            if not comment:
                return render_template("error.html", error="При редактировании статьи комментарий обязателен.")

            artdata = art.to_json()
            body = os.path.join(artdata[-1]["fpath"], str(int(time.time())) + ".html",)
            b = {"fpath": artdata[-1]["fpath"], "body": body, "last_edit_by": g.user.username, "editdate": datetime.datetime.now().strftime("%I:%M%p в %B %d %Y"), "comment": comment}
            artdata.append(b)
            with open(body, "w") as f:
                f.write(data)

            c_article = Article.query.filter_by(title=title).first()
            user = User.query.filter_by(username=g.user.username).first()

            user.commit_n += 1
            c_article.data = json.dumps(artdata)

            db.session.commit()
        return redirect("/")
    else:
        return render_template("articles/constructor_modern.html")
