if [[ ! -d venv ]]; then
    python -m venv venv
    source venv/bin/activate
    pip install flask
    pip install flask-sqlalchemy
    pip install python-dotenv
    pip install gunicorn
else
    source venv/bin/activate
fi

gunicorn -w 16 mk:app
