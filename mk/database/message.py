from .db import *

class Message(db.Model):
    def __init__(self, from_user: str, to_user: str, topic: str, data: str):
        self.from_user = from_user
        self.to_user = to_user

        self.topic = topic
        self.data = data

    msgid = db.Column(db.Integer, primary_key=True, autoincrement=True)

    from_user = db.Column(db.String(32), nullable=False)
    to_user = db.Column(db.String(32), nullable=False)

    topic = db.Column(db.String(32), nullable=False)

    data = db.Column(db.Text, nullable=False)
