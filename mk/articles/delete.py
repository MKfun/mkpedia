import json
import shutil

from .articles import articles_bp
from ..decorators import *
from ..db import *

@articles_bp.route("/delete")
@admin_only
def delete_article():
    article = request.args.get("article")

    if not article:
        return render_template("error.html", error="Не указан параметри article.")

    db = get_db()

    art = db.execute("SELECT * FROM articles WHERE title = ?", (article,)).fetchone()
    if not art:
        return render_template("not_found.html"), 404

    arts = json.loads(art["data"])[-1]

    shutil.rmtree(arts["fpath"])

    db.execute("DELETE FROM articles WHERE title = ?", (article,))
    db.commit()

    return redirect(url_for("articles.listall"))
