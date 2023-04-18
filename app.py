from flask import Flask, abort, redirect, render_template, request

from src.repositories.rating_repository import rating_repository_singleton

from src.models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=\
    'mysql://root:password@localhost:3306/sqlalchemy?charset=utf8mb4'
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
    #TODO: Get more info from Eric about user_id and how works with google login
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

if __name__ == '__main__':
    app.run(debug=True)
