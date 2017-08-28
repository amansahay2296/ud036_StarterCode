class Movie():
    """This class helps us to store movie related information """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        """  Constructor call for class Movie with instance variables
             title,poster_image_url,trailer_youtube_url"""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
