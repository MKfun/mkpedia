if [[ ! -d venv ]]; then
    python -m venv venv
    source venv/bin/activate
    pip install flask
    pip install python-dotenv
    pip install gunicorn
else
    source venv/bin/activate
fi

if [[ ! -d instance ]]; then
    cd mk
    flask --app app init_db
    cd ..
fi

gunicorn -w 16 mk:app
