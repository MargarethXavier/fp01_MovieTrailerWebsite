import webbrowser

class Movie():
    # Documentation of the class Movie. 
    """ This class stores movies related information.

        Attributes:
            title - stores the movie's title.
            poster_image_url - stores the movie's poster URL
            trailer_youtube_url - stores the movie's trailer URL on the youtube
    """
    
    # Constructor of the class. It'll be called for each instance of the class 
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
