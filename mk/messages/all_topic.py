from flask import *
from sqlalchemy import or_

from ..database import *
from ..decorators import user_only

from .messages import *

@messages_bp.route("/all_topic", methods=["GET"])
@user_only
def all_msgs():
    topic = request.args.get("topic")

    if not topic:
        return render_template("error.html", error="Не указан параметр topic.")

    messages = Message.query.filter_by(topic=topic).filter(or_(Message.from_user == g.user.username, Message.to_user == g.user.username)).all()
    return render_template("messages/all_topic.html", messages=messages)
