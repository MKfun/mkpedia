from flask import *

from ..db import *
from ..decorators import user_only

from .messages import *

@messages_bp.route("/showmessage", methods=["GET"])
@user_only
def show_message():
    next_answer = request.args.get("next_answer")
    msgid = request.args.get("msgid")

    if not msgid:
        return render_template("error.html", error="Не передан параметр msg_id")

    db = get_db()

    message = db.execute("SELECT * FROM messages WHERE msgid = ?", (msgid,)).fetchone()
    answers = db.execute("SELECT * FROM messages WHERE answer_to = ?", (msgid,)).fetchall()

    if not next_answer:
        if not message:
            return render_template("not_found.html")
        return render_template("messages/show_message.html", message=message, answer_count=len(answers))
    elif next_answer == "1":
        if not answers:
            return render_template("not_found.html")
        return render_template("messages/show_message.html", message=answers[0], answer_count=len(answers)-1)
