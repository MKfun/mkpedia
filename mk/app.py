import os
import secrets
import dotenv

from flask import *

from .db import *

from .auth import *
from .admin_panel import *
from .articles import *
from .users import *
from .uploader import *
from .random import *
from .messages import *

dotenv.load_dotenv()
def getarticleform(count):
    if count % 100 in (11, 12, 13, 14): return f"{count} статей"
    if count % 10 == 1: return f"{count} статья"
    if count % 10 in (2, 3, 4): return f"{count} статьи"
    return f"{count} статей"
    
    
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY=os.getenv("SECRET_KEY"), DATABASE=os.path.join(app.instance_path, "mkpedik.db"), ARTICLE_DIR=os.path.join(app.instance_path, "article_data"))

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    app.config["MAX_CONTENT_LENGTH"] = 50 * 1000 * 1000 # максимальный вес файла - 50 мегабайт.

    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db)

    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(articles_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(uploader_bp)
    app.register_blueprint(random_bp)
    app.register_blueprint(messages_bp)

    @app.route("/")
    def home():
        articlecount = len(get_db().execute("SELECT * FROM articles").fetchall())
        formatted_count = getarticleform(articlecount)
        return render_template("home.html", formatted_count=formatted_count)
        
    return app

app = create_app()
