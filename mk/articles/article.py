from bs4 import BeautifulSoup, NavigableString
from os import system

from .articles import articles_bp
from ..decorators import *

from ..database import *

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

    if artname is None:
        return render_template("not_found.html")

    art = Article.query.filter_by(title=artname).first()

    if not art:
        return render_template("error.html", error="Статья не найдена!")

    arts = art.to_json()
    if n > len(arts) - 1:
        n = -1

    with open(arts[n]["body"]) as f:
        if construct is not None:
            return render_template("articles/constructor_modern.html", body=f.read(), title=art.title)
        else:
            if want_raw_body is not None and want_raw_body == "1":
                return f.read()
            else:
                file = f.read()
                soup = BeautifulSoup(file, "html.parser")

                wiki_imgs = [] # Массив с тэгами картинок (img)
                for img in soup.find_all("img"):
                    wiki_imgs.append(img.extract())
                # Удаление картинок из основного маркапа и сохранение
                # их в массив для дальнейших махинаций

                if len(wiki_imgs) > 0:
                # Проверка есть ли картинки
                    wiki_img = soup.new_tag("div", attrs={"class": "wiki_img"})
                    # Объект тэга панели картинок (div class="wiki_img")
                    
                    for img in wiki_imgs:
                        # img - непосредственно сам тэг картинки
                        if "alt" in img.attrs.keys():
                            desc = img.attrs["alt"]
                            del img.attrs["alt"]
                        else:
                            desc = ""

                        wiki_img.append(img)
                        wiki_img.append(soup.new_tag("p", string=desc))

                    wiki_img.contents[-1].attrs["class"] = "last_wiki_img"
                    # Добавить последнему объекту в панели этот класс,
                    # чтобы отключить ему margin

                    soup.insert(0, wiki_img)
                    # Соединение этого месива воедино
                    
                    html = str(soup)
                else:
                # Если картинок нет, то вакханалия отменяется и передаётся
                # просто файл как есть
                    html = file

                return render_template("articles/article.html", title=art.title, article=html, last_edit_by=arts[n]["last_edit_by"])
