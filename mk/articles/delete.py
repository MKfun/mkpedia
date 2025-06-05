import json
import shutil

from .articles import articles_bp
from ..decorators import *
from ..database import *

@articles_bp.route("/delete")
@admin_only
def delete_article():
    article = request.args.get("article")

    if not article:
        return render_template("error.html", error="Не указан параметр article.")

    art = Article.query.filter_by(title=article).first()
    if not art:
        return render_template("error.html", error="Статья не найдена.")

    shutil.rmtree(art.to_json()[-1]["fpath"])

    db.session.delete(art)
    db.session.commit()

    return redirect(url_for("articles.listall"))
