import json

from .articles import articles_bp
from ..decorators import *
from ..db import *

@articles_bp.route("/commits")
@user_only
def get_commits():
    article = request.args.get("article")

    if not article:
        return render_template("not_found.html")

    db = get_db()

    art = db.execute("SELECT * FROM articles WHERE title = ?", (article,)).fetchone()
    if not art:
        return render_template("not_found.html")

    arts = json.loads(art["data"])

    return render_template("/articles/commits.html", article=art, commit_list=arts)
