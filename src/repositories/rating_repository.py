from src.models import *
from flask import session

class RatingRepository:

    def get_all_ratings(self):
        ratings = db.session.query(Ratings, Professors.first_name, Professors.last_name, Courses.subject, Courses.course_num)\
                       .join(Professors, Ratings.professor_id == Professors.professor_id)\
                       .join(Courses, Ratings.course_id == Courses.course_id)\
                       .all()
        return ratings
    
    def search_ratings(self, q):
        ratings = db.session.query(Ratings, Professors.first_name, Professors.last_name, Courses.course_num, Courses.subject, Ratings.rating_id, Ratings.rating, Ratings.user_id, Ratings.semester, Ratings.comments)\
                        .join(Professors, Ratings.professor_id == Professors.professor_id)\
                        .join(Courses, Ratings.course_id == Courses.course_id)\
                        .filter(Professors.first_name == q)\
                        .all()
        return ratings
    
    def get_rating_by_id(self, rating_id):
        single_rating = db.session.query(Ratings, Professors.first_name, Professors.last_name, Courses.course_num, Courses.subject, Ratings.rating_id, Ratings.rating, Ratings.user_id, Ratings.comments)\
                        .join(Professors, Ratings.professor_id == Professors.professor_id)\
                        .join(Courses, Ratings.course_id == Courses.course_id)\
                        .filter(Ratings.rating_id == rating_id)\
                        .first()
        return single_rating

    def get_ratings_by_prof_course(self,prof_id, course_id):
        ratings = Ratings.query.filter_by(prof_id=prof_id, course_id=course_id).all()
        return ratings        

    def create_rating(self, first_name, last_name, subject, course_num, rating, semester, comments, email):

    # Get the professor_id
        professor_id = self.get_prof_id_by_name(first_name, last_name)        
    # Get the course_id       
        course_id = self.get_course_id_by_subj_num(subject, course_num)
    # Get user_id
        user_id = self.get_user_id_by_email(email)
    # Create a new Rating object
        new_rating = Ratings(user_id=user_id, professor_id=professor_id, course_id=course_id, rating=rating, semester=semester, comments=comments)
    # Add the new rating to the session and commit to the database
        db.session.add(new_rating)
        db.session.commit()        
    # Return the new rating object
        return new_rating    

    def get_prof_id_by_name(self, first_name, last_name):
        professor = Professors.query.filter_by(first_name=first_name, last_name=last_name).first()
        if professor:
            return professor.professor_id
        else:
            new_professor = Professors(first_name=first_name, last_name=last_name)
            db.session.add(new_professor)
            db.session.commit()
            return new_professor.professor_id
    
    def get_course_id_by_subj_num(self, subject, course_num):
        course = Courses.query.filter_by(subject=subject, course_num=course_num).first()
        if course is None:
            course = Courses(subject=subject, course_num=course_num)
            db.session.add(course)
            db.session.commit()
        course_id = course.course_id
        return course_id

    def get_user_id_by_email(self, email):
        user = Users.query.filter_by(email=email).first()
        user_id = user.user_id
        return user_id
    
    def create_user(self, first_name, last_name, email):
        new_user = Users(first_name=first_name, last_name=last_name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    def get_course_id(self, subject, course_num):
        course = Courses.query.filter_by(subject=subject, course_num=course_num).first()
        course_id = course.course_id
        return course_id
    

    



# Singleton to be used in other modules
rating_repository_singleton = RatingRepository()