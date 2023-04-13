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

#TODO: Implement more functions as we get html framework
@app.get('/ratings/<int:movie_id>')
def get_single_movie(movie_id):
    single_movie = movie_repository_singleton.get_movie_by_id(movie_id)
    return render_template('get_single_movie.html', movie=single_movie)

if __name__ == '__main__':
    app.run(debug=True)
