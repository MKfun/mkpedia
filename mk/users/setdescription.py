from flask import *

from .users import user_bp
from ..decorators import *
from ..database import *

@user_bp.route("/setdescription", methods=["POST"])
@user_only
def set_description():
    description = request.form["description"]

    if not description:
        return render_template("error.html", error="Не указано описание.")

    if len(description) > 512:
        return render_template("error.html", error="Слишком длинное описание.")

    user = User.query.filter_by(username=g.user.username).first()
    user.profile_description = description

    db.session.commit()

    return redirect(url_for("users.get_me"))
