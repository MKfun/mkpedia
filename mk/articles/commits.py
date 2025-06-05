import json

from .articles import articles_bp
from ..decorators import *
from ..database import *

@articles_bp.route("/commits")
@user_only
def get_commits():
    article = request.args.get("article")

    if not article:
        return render_template("not_found.html")

    art = Article.query.filter_by(title=article).first()
    if not art:
        return render_template("not_found.html")

    arts = art.to_json()

    return render_template("/articles/commits.html", article=art, commit_list=arts)
