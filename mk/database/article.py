import json
from .db import *

#CREATE TABLE IF NOT EXISTS articles (
#    title TEXT UNIQUE NOT NULL,
#    data TEXT NOT NULL,
#    made_by TEXT NOT NULL
#);

class Article(db.Model):
    def __init__(self, title: str, data: str, made_by: str):
        self.title = title
        self.data = data
        self.made_by = made_by

    def to_json(self) -> str:
        return json.loads(self.data)

    def from_data(self, data: []):
        self.data = json.dumps(data)

    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.String(32), unique=True)
    data = db.Column(db.Text)
    made_by = db.Column(db.String(32))
