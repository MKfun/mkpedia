from flask import *

from ..db import *
from ..decorators import user_only

from .messages import *

@messages_bp.route("/inbox", methods=["GET"])
@user_only
def get_inbox():
    db = get_db()

    inbox = db.execute("SELECT * FROM messages WHERE from_user = ? OR to_user = ? AND NOT from_user == to_user", (g.user["username"], g.user["username"])).fetchall()

    return render_template("messages/inbox.html", inbox=inbox)
