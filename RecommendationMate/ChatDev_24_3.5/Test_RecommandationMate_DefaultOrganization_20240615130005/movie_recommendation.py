'''
This file contains the MovieRecommendation class which provides personalized movie recommendations based on user preferences and historical data.
'''
class MovieRecommendation:
    def __init__(self):
        self.movies = {
            "Action": ["Movie A", "Movie B", "Movie C"],
            "Comedy": ["Movie D", "Movie E", "Movie F"],
            "Drama": ["Movie G", "Movie H", "Movie I"]
        }
    def get_recommendations(self, genre):
        '''
        Returns a list of movie recommendations based on the given genre.
        Args:
            genre (str): The genre of movies to recommend.
        Returns:
            list: A list of movie recommendations for the given genre.
        Raises:
            ValueError: If an invalid genre is entered.
        '''
        if genre in self.movies:
            return self.movies[genre]
        else:
            raise ValueError("Invalid genre entered.")