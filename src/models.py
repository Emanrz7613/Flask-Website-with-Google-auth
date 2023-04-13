from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Professors(db.Model):
    professor_id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.department_id'), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    

class Departments(db.Model):
    department_id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String(50), nullable=False)

class Professor_course(db.Model):
    professor_id = db.Column(db.Integer, db.ForeignKey('professors.professor_id'), primary_key=True,  nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), primary_key=True, nullable=False)

class Courses(db.Model):
    course_id = db.Column(db.Integer, primary_key=True, nullable=False)
    subject = db.Column(db.String(4), nullable = False)
    course_num = db.Column(db.String(4), nullable=False)
    course_title = db.Column(db.String(50), nullable=False)

@staticmethod
def get_course_id(subject, course_num):
    course = Courses.query.filter_by(subject=subject, course_num=course_num).first()
    if course:
        return course.course_id
    return None

class Ratings(db.Model):
    rating_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.course_id'), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professors.professor_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.String(12), nullable=False)
    comments = db.Column(db.String(255), nullable=True)

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)