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
def get_single_movie(rating_id):
    single_rating = rating_repository_singleton.get_rating_by_id(rating_id)
    return render_template('get_single_rating.html', rating=single_rating)

@app.get('/ratings/new')
def create_movies_form():
    return render_template('create_ratings_form.html')

@app.post('/ratings')
def create_rating():
    class_name = request.form.get('class', '')
    prof_name = request.form.get('professor', '')
    rating = request.form.get('rating', 1, type=int)
    semester = request.form.get('semeseter', '')
    desc = request.form.get('desc', '', type=str)
    if class_name == '' or prof_name == '' or rating < 1 or rating > 5 or semester == '':
        abort(400)
    created_rating = rating_repository_singleton.create_movie(class_name, prof_name, rating, semester, desc)
    return redirect(f'/movies/{created_rating.rating_id}')

if __name__ == '__main__':
    app.run(debug=True)
