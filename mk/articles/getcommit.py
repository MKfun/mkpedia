import json

from .articles import articles_bp
from ..decorators import *
from ..db import *

def get_commit(title: str, n: int):
    db = get_db()

    art = db.execute("SELECT * FROM articles WHERE title = ?", (title,)).fetchone()
    if not art:
        return ""

    arts = json.loads(art["data"])

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
