from flask import *

from .users import user_bp
from ..decorators import *
from ..db import *

from .getcommitsform import *

@user_bp.route("/getme", methods=["GET", "POST"])
@user_only
def get_me():
    if request.method == "POST":
        pass
    else:
        return render_template("users/me.html", user=g.user, formatted_commits=getcommitsform(g.user.commit_n))
