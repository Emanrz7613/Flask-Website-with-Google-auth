from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#TODO: Implement ER Diagram tables here
class Professor(db.Model):
    professor_id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)

