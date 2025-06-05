import os
import sqlite3
import sys

from .user import *
from .queue import *
from .article import *
from .message import *

def migrate_from_v08(db_p: str, db):
    print("Обнаружен переход (<=v0.8 -> v0.9), переношу БД...")
    db_old = sqlite3.connect(db_p, detect_types=sqlite3.PARSE_DECLTYPES)
    db_old.row_factory = sqlite3.Row

    print("mkpedik.db/users -> mkpedia_alc/User")
    users_old = db_old.execute("SELECT * FROM users").fetchall()
    for user in users_old:
        user = User(user["username"], user["hash"], user["admin"], user["profile_description"], user["commit_n"], alreadyhash_pwd=True)
        if User.query.filter_by(username=user.username).first() is not None or user.username == "root":
            continue
        db.session.add(user)

    print("mkpedik.db/queue -> mkpedia_alc/Queue")
    queue_old = db_old.execute("SELECT * FROM queue").fetchall()
    for queue_m in queue_old:
        queue = Queue(queue_m["username"], queue_m["hash"], alreadyhash_pwd=True)
        if Queue.query.filter_by(username=queue.username).first():
            continue

        db.session.add(queue)

    print("mkpedik.db/articles -> mkpedia_alc/Articles")
    articles_old = db_old.execute("SELECT * FROM articles").fetchall()
    for article_o in articles_old:
        article = Article(article_o["title"], article_o["data"], article_o["made_by"])
        if Article.query.filter_by(title=article.title).first():
            continue
        db.session.add(article)

    print("mkpedik.db/messages -> mkpedia_alc/Messages")
    messages_old = db_old.execute("SELECT * FROM messages").fetchall()
    for message_o in messages_old:
        message = Message(message_o["from_user"], message_o["to_user"], message_o["topic"], message_o["data"])
        if Message.query.filter_by(msgid=message.msgid).first():
            continue
        db.session.add(message)

    for i in range(10):
        print("(Дублировано 10 раз): ЗАКРОЙТЕ ПРИЛОЖЕНИЕ И СДЕЛАЙТЕ БЕКАП instance/mkpedik.db (mkpediK (буква К)), САМ ФАЙЛ ОТТУДА УДАЛИТЕ!!!!!")

    db.session.commit()
