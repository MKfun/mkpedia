from flask import *

import os

TAGS_FILE=os.path.join(os.path.dirname(__file__), "tags_blacklist.txt")

def permittable(article: str) -> bool:
    with open(TAGS_FILE) as f:
        blacklist = f.read()

        for tag in blacklist.split("\n"):
            if ("<" + tag in article or tag + ">" in article or "<" + tag + ">" in article or tag in article or "</" + tag in article) and len(tag) > 0:
                return (False, tag)
    return (True, "")
