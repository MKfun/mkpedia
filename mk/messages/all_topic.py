from flask import *

from ..db import *
from ..decorators import user_only

from .messages import *

@messages_bp.route("/all_topic", methods=["GET"])
@user_only
def all_msgs():
    topic = request.args.get("topic")

    db = get_db()

    if not topic:
        return render_template("error.html", error="Не указан параметр topic.")

    messages = db.execute("SELECT * FROM messages WHERE topic = ? AND (from_user = ? OR to_user = ?)", (topic, g.user["username"], g.user["username"])).fetchall()

    return render_template("messages/all_topic.html", messages=messages)
