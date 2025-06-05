import json

from .articles import articles_bp
from ..decorators import *
from ..database import *

def get_commit(title: str, n: int):
    art = Article.query.filter_by(title=title).first()
    if not art:
        return ""

    arts = art.to_json()

    if n < 0 or n > len(arts)-1:
        return ""

    our_art = arts[n] # our - не опечатка

    with open(our_art["body"]) as f:
        return f.read()

@articles_bp.route("/getcommit")
def get_commit_page():
    article = request.args.get("article")
    n = request.args.get("n")

    if not article or not n:
        return render_template("error.html", error="Не указан один из или оба параметра (article && n).")

    return render_template("articles/article.html", article=get_commit(article, int(n)), title=article, wayback_id=n)
