from .articles import articles_bp
from ..decorators import *

from ..database import *

@articles_bp.route("/discussion", methods=["GET", "POST"])
@user_only
def discussion():
    article = request.args.get("article")
    if not article:
        return render_template("error.html", error="Не указан query-параметр article.")
    if not Article.query.filter_by(title=article).first():
        return render_template("error.html", error="Статья не найдена.")

    if request.method == "POST":
        data = request.form["data"]
        if not data:
            return render_template("error.html", error="Не указан form-параметр data.")

        d = Discuss(article, g.user.username, data)
        db.session.add(d)
        db.session.commit()

    abart = Discuss.query.filter_by(article=article).all()
    return render_template("articles/discussion.html", articles=abart, title=article)
