from src.models import *
class ReviewRepository:

    def get_all_reviews(self):
        #Abstract
        return

    def get_reviews_by_prof(self, prof_name):
        #Abstract
        return

    def create_review(self, class_name, prof_name, rating, desc):
        #Abstract
        return

    def get_reviews_by_class(self, class_name):
        #Abstract
        return


# Singleton to be used in other modules
review_repository_singleton = ReviewRepository()
