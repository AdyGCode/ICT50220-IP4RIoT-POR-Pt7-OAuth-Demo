import os

from flask import Flask, redirect, render_template, session, url_for
from flask_cors import CORS
from datetime import timedelta, date, datetime
import dateutil
from dotenv import load_dotenv
from authlib.integrations.flask_client import OAuth

load_dotenv(".env")

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET")
app.config["SERVER_NAME"] = os.environ.get("APP_SERVER")
oauth = OAuth(app)

# CORS(app, supports_credentials=True)

LOGGED_IN = "Logged in"
LOGGED_OUT = "Goodbye.. see you soon"


@app.route('/')
@app.route('/index')
def index():
    profile = session.get('profile')
    status = session.get('login_status')
    return render_template("index.html",
                           profile=profile,
                           login_status=status, )


@app.route('/logout')
def logout():
    session.pop('profile', None)
    session['login_status'] = LOGGED_OUT
    return redirect(url_for('index'))


@app.route('/github/login')
def github_login():
    # GitHub OAuth Client settings
    GITHUB_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID')
    GITHUB_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET')
    GITHUB_BASE_URL = os.environ.get('GITHUB_BASE_URL')
    GITHUB_API_URL = os.environ.get('GITHUB_API_URL')

    oauth.register(
        name="github",
        client_id=GITHUB_CLIENT_ID,
        client_secret=GITHUB_CLIENT_SECRET,
        access_token_url=GITHUB_API_URL + 'access_token',
        access_token_params=None,
        authorize_url=GITHUB_API_URL + 'authorize',
        authorize_params=None,
        api_base_url=GITHUB_BASE_URL,
        client_kwargs={
            'scope': 'user:email'
        },
    )
    redirect_uri = url_for('github_auth', _external=True)
    return oauth.github.authorize_redirect(redirect_uri)


@app.route('/github/authorize')
def github_auth():
    GITHUB_BASE_URL = os.environ.get('GITHUB_BASE_URL')
    token = oauth.github.authorize_access_token()
    response = oauth.github.get('user', token=token)
    profile = response.json()
    if profile:
        profile['since'] = str(datetime.today() -
                               datetime.strptime(profile['created_at'],
                                                 "%Y-%m-%dT%H:%M:%SZ"))
        session['profile'] = profile
        session['login_status'] = LOGGED_IN
        return redirect(url_for('index', _external=True))

    return redirect(url_for('index', _external=True))
