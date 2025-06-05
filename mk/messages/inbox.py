from sqlalchemy import or_

from flask import *

from ..database import *
from ..decorators import user_only

from .messages import *

@messages_bp.route("/inbox", methods=["GET"])
@user_only
def get_inbox():
    inbox = Message.query.filter(or_(Message.from_user == g.user.username, Message.to_user == g.user.username)).all()
    return render_template("messages/inbox.html", inbox=inbox)
