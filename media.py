"""This module contains only contains one class, Movie, used for handling movie
information. The media and TV_show classes were not implemented in the final
web page and were deleted
"""

class Movie(object):
    """This class provides a way to store movie related information"""
    def __init__(self, movie_title, release_date, movie_director,
                 movie_tagline, poster_image, trailer_youtube, genre, rating,
                 duration):
        #List of accepted ratings
        valid_ratings = ["G", "PG", "PG-13", "R", "UR", "NR"]
        # Initializes class properties
        self.title = movie_title
        self.date = release_date
        self.director = movie_director
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.genre = genre
        self.duration = duration
        # Give movies without taglines an empty string for this property
        if movie_tagline != "false":
            self.tagline = movie_tagline
        else:
            self.tagline = ""
        # Check if rating is valid
        if rating in valid_ratings:
            self.rating = rating
        else:
            print "Unrecognized rating for " + self.title
            self.rating = "?"
