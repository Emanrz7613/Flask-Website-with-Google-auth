from flask import Flask, abort, redirect, render_template, request

from src.repositories.review_repository import review_repository_singleton

from src.models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=\
    'mysql://root:password@localhost:3306/sqlalchemy?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/reviews')
def list_all_reviews():
    all_reviews = review_repository_singleton.get_all_reviews()
    return render_template('list_all_reviews.html', list_reviews_active=True, reviews=all_reviews)

#TODO: Implement more functions as we get html framework

if __name__ == '__main__':
    app.run(debug=True)
