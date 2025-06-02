from .articles import articles_bp
from ..decorators import *
from ..db import *

@articles_bp.route("/article")
@user_only
def get_article():
    construct = request.args.get("construct")
    n = request.args.get("n")
    want_raw_body = request.args.get("raw_body")

    if not n:
        n = -1
    else:
        try:
            n = int(n)
            if n < 0:
                n = -1
        except:
            n = -1

    artname = request.args.get("article")
    db = get_db()

    if artname is None:
        return render_template("not_found.html")

    art = db.execute("SELECT * FROM articles WHERE title = ?", (artname,)).fetchone()
    if not art:
        return render_template("error.html", error="Статья не найдена!")

    arts = json.loads(art["data"])
    if n > len(arts)-1:
        n = -1

    if art is None:
        return render_template("error.html", error="Статья не найдена!")

    with open(arts[n]["body"]) as f:
        if construct is not None:
            return render_template("articles/constructor_modern.html", body=f.read(), title=art["title"])
        else:
            if want_raw_body is not None and want_raw_body == "1":
                return f.read()
            else:
                return render_template("articles/article.html", title=art["title"], article=f.read(), last_edit_by=arts[n]["last_edit_by"])
