from flask import Flask, abort, redirect, render_template, request, url_for, session, flash
from flask_dance.contrib.google import  google
import os
from src.repositories.rating_repository import *
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from src.models import *
from authlib.integrations.flask_client import OAuth
from functools import wraps

app = Flask(__name__)

# Google OAuth2 Configuration
app.config['SECRET_KEY'] = 'ebade5ab48174feaae42e6f0e0eb8c77'
app.config['GOOGLE_OAUTH_CLIENT_ID'] = '619389714744-hb1q3g3opv4jb6dm9hligalpvik9ih9e.apps.googleusercontent.com'
app.config['GOOGLE_OAUTH_CLIENT_SECRET'] = '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'

oauth = OAuth(app)

google = oauth.register(
    name="google",
    client_id=app.config["GOOGLE_OAUTH_CLIENT_ID"],
    client_secret=app.config["GOOGLE_OAUTH_CLIENT_SECRET"],
    access_token_url="https://accounts.google.com/o/oauth2/token",
    access_token_params=None,
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    authorize_params=None,
    api_base_url="https://www.googleapis.com/oauth2/v1/",
    redirect_uri="http://localhost:5000/authorize",  # Make sure this matches the one in the Google Cloud Console
    client_kwargs={"scope": "openid email profile"},
)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

app.config['SQLALCHEMY_DATABASE_URI']=\
    'mysql://root:3186@localhost:3306/3155_final_project?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/ratings')
def list_all_ratings():
    all_ratings = rating_repository_singleton.get_all_ratings()
    return render_template('list_all_ratings.html', list_ratings_active=True, ratings=all_ratings)

@app.get('/ratings/<int:rating_id>')
def get_single_rating(rating_id):
    single_rating = rating_repository_singleton.get_rating_by_id(rating_id)
    return render_template('get_single_rating.html', rating=single_rating)

@app.get('/ratings/new')
def create_ratings_form():
    return render_template('create_ratings_form.html')

@app.post('/ratings')
def create_rating():
    #TODO: Get more info from Eric about user_id/first_name/last_name and how works with google login
    user_id = request.form.get('user_id', '')
    first_name = request.form.get('first_name', '')
    last_name = request.form.get('last_name', '')
    subject = request.form.get('subject', '')
    course_num = request.form.get('course_num', '')
    rating = request.form.get('rating', 1, type=int)
    semester = request.form.get('semeseter', '')
    desc = request.form.get('desc', '', type=str)
    if rating < 1 or rating > 5 or semester == '' or subject == '' or course_num == '':
        abort(400)
    created_rating = rating_repository_singleton.create_rating(user_id, first_name, last_name, subject, course_num, rating, semester, desc)
    return redirect(f'/ratings/{created_rating.rating_id}')

@app.get('/ratings/search')
def search_ratings():
    found_ratings = []
    q = request.args.get('q', '')
    if q != '':
        found_ratings = rating_repository_singleton.search_ratings(q)
    return render_template('search_ratings.html', search_active=True, ratings=found_ratings, search_query=q)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "google_id" not in session:
            return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/login")
def login():
    if "google_id" in session:
        return redirect(url_for("index"))
    return google.authorize_redirect(url_for("authorize", _external=True))

@app.route("/authorize")
def authorize():
    token = google.authorize_access_token()
    resp = google.get("userinfo")
    user_info = resp.json()
    session["google_id"] = user_info["id"]
    session["email"] = user_info["email"]
    flash(f"Logged in as {user_info['email']}", "success")
    return redirect('/')

@app.route("/logout")
@login_required
def logout():
    session.pop("google_id", None)
    session.pop("email", None)
    flash("You have been logged out.", "success")

if __name__ == '__main__':
    app.run(debug=True)
