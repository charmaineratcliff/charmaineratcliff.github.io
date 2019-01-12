import webbrowser


class Movie(object):
    """ This class provides a way to store movie related information."""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """
        Initializes the movie instance.
        Arguments:
            title: title of the movies
            poster_image: image of the movie poster
            trailer: video of the movie trailer
        Returns:
        None
        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Opens browser with video of the movie trailer.
        Arguments:
            trailer: video of the movie trailer
        Returns:
            open browser with video of movie trailer
        """
        webbrowser.open(self.trailer_youtube_url)
