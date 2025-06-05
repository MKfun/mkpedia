from flask import *
from sqlalchemy import or_

from ..database import *

from ..decorators import user_only

from .messages import *

@messages_bp.route("/showmessage", methods=["GET"])
@user_only
def show_message():
    next_answer = request.args.get("next_answer")
    msgid = request.args.get("msgid")

    if not msgid:
        return render_template("error.html", error="Не передан параметр msg_id")

    message = Message.query.filter(or_(Message.from_user == g.user.username, Message.to_user == g.user.username)).filter_by(msgid=msgid).first()

    if not message:
        return render_template("error.html", error="Сообщение не найдено.")
    return render_template("messages/show_message.html", message=message)
