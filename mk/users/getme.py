from flask import *

from .users import user_bp
from ..decorators import *
from ..db import *


def getcommitsform(count):
    if count % 100 in (11, 12, 13, 14): return f"о {count} правок"
    if count % 10 == 1: return f"а {count} правка"
    if count % 10 in (2, 3, 4): return f"о {count} правки"
    if count == 0: return "о правок... 0"
    return f"{count} правок"
    
    
@user_bp.route("/getme", methods=["GET", "POST"])
@user_only

def get_me():
    db = get_db()

    if request.method == "POST":
        pass
    else:
        user = db.execute("SELECT * FROM users WHERE username = ?", (g.user["username"],)).fetchone()
        formatted_commits = getcommitsform(user["commit_n"])
        return render_template("users/me.html", user=user, formatted_commits=formatted_commits)
