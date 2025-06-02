from .articles import articles_bp
from ..decorators import *
from ..db import *

@articles_bp.route("/edits")
@user_only
def get_edits():
    article = request.args.get("article")

    if not article:
        return render_template("error.html", error="Не указан параметр article.")

    db = get_db()

    art = db.execute("SELECT * FROM articles WHERE title = ?", (article,)).fetchone()
    if not art:
        return render_template("not_found.html")

    arts = json.loads(art["data"])

    return render_template("articles/article_edits.html", edits=arts)
