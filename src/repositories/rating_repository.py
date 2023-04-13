from src.models import *
class RatingRepository:

    def get_all_ratings(self):
        #Abstract
        return

    def get_ratings_by_prof(self, prof_name):
        #Abstract
        return

    def create_rating(self, class_name, prof_name, rating, desc):
        #Abstract
        return

    def get_ratings_by_class(self, class_name):
        #Abstract
        return


# Singleton to be used in other modules
rating_repository_singleton = RatingRepository()
