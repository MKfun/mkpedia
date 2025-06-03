import os

TAGS_FILE=os.path.join(os.path.dirname(__file__), "titles_blacklist.txt")

def secure_title(title: str) -> str:
    with open(TAGS_FILE) as f:
        ntitle = title
        blist = f.read().split('\n')
        for b in blist:
            ntitle = ntitle.replace(b, "")
        return ntitle
