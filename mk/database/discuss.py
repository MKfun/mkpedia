from .db import *

class Discuss(db.Model):
    def __init__(self, art: str, aut: str, dat: str):
        self.article = art
        self.author = aut
        self.data = dat

    msgid = db.Column(db.Integer, primary_key=True, autoincrement=True)

    article = db.Column(db.String(32))

    author = db.Column(db.String(32))
    data = db.Column(db.Text)
