import hashlib

from .db import *
from sqlalchemy.orm import Mapped, mapped_column

class Queue(db.Model):
    def __init__(self, uname: str, pwd: str, alreadyhash_pwd: bool = False):
        self.username = uname
        self.pwdhash = pwd if alreadyhash_pwd else hashlib.sha256(pwd.encode("utf-8")).hexdigest()

    username = db.Column(db.String(32), primary_key=True)
    pwdhash = db.Column(db.String(256))
