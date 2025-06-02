from flask import *

from ..db import *
from ..decorators import user_only

from .messages import *

@messages_bp.route("/send", methods=["GET", "POST"])
@user_only
def send_message():
    db = get_db()

    if request.method == "POST":
        to_user = request.form["to_user"]
        topic = request.form["topic"]
        data = request.form["data"]

        if not to_user or not topic or not data:
            return render_template("error.html", error="Переданы неправильные данные!")

        db.execute("INSERT INTO messages(from_user, to_user, topic, data, answer_to) VALUES(?, ?, ?, ?, NULL)", (g.user["username"], to_user, topic, data))
        db.commit()

        return redirect("/messages/inbox")
    else:
        answering_to = request.args.get("answering_to")

        if not answering_to:
            return render_template("messages/send.html", answering_to=None)
        else:
            try:
                answering_to = int(answering_to)
                msg = db.execute("SELECT * FROM messages WHERE msgid = ? AND from_user = ? OR to_user = ?", (answering_to, g.user["username"], g.user["username"])).fetchone()

                if not msg:
                    return render_template("error.html", error="Сообщение не ваше или не найдено.")

                return render_template("messages/send.html", answering_to=msg)
            except ValueError:
                return render_template("error.html", error="answering_to должен быть числом.")
