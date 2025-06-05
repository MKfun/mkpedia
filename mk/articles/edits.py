from .articles import articles_bp
from ..decorators import *
from ..database import *

@articles_bp.route("/edits")
@user_only
def get_edits():
    article = request.args.get("article")

    if not article:
        return render_template("error.html", error="Не указан параметр article.")

    art = Article.query.filter_by(title=article).first()
    if not art:
        return render_template("not_found.html")

    arts = art.to_json()

    return render_template("articles/article_edits.html", edits=arts)
