import hashlib

from .db import *

class User(db.Model):
    def __init__(self, user: str, pwd: str, adm: bool, profile_desc: str = "Нет описания...", com_n: int = 0, alreadyhash_pwd: bool = False):
        self.username = user

        self.pwdhash = pwd if alreadyhash_pwd else hashlib.sha256(pwd.encode("utf-8")).hexdigest()

        self.admin = adm
        self.profile_description = profile_desc
        self.commit_n = com_n

    username = db.Column(db.String(32), unique=True, primary_key=True)
    pwdhash = db.Column(db.String(256))
    admin = db.Column(db.Boolean)

    profile_description = db.Column(db.String(512))
    commit_n = db.Column(db.Integer)
