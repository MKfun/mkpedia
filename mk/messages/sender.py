from flask import *
from sqlalchemy import or_

from ..database import *
from ..decorators import user_only

from .messages import *

@messages_bp.route("/send", methods=["GET", "POST"])
@user_only
def send_message():
    if request.method == "POST":
        to_user = request.form["to_user"]
        topic = request.form["topic"]
        data = request.form["data"]

        if not to_user or not topic or not data:
            return render_template("error.html", error="Переданы неправильные данные!")

        message = Message(g.user.username, to_user, topic, data)

        db.session.add(message)
        db.session.commit()

        return redirect("/messages/inbox")
    else:
        answering_to = request.args.get("answering_to")

        if not answering_to:
            return render_template("messages/send.html", answering_to=None)
        else:
            try:
                answering_to = int(answering_to)
                msg = Message.query.filter(or_(Message.from_user == g.user.username, Message.to_user == g.user.username)).filter_by(msgid=answering_to).first()

                if not msg:
                    return render_template("error.html", error="Сообщение не ваше или не найдено.")

                return render_template("messages/send.html", answering_to=msg)
            except ValueError:
                return render_template("error.html", error="answering_to должен быть числом.")
