"""This module converts movie data stored in a text file (movie_list.txt),
into a list of Movie objects, which are passed to fresh_tomatoes.py for
rendering.
"""

import media
import fresh_tomatoes


def load_movie_site():
    """Reads data from file, creates Movie list, passes to fresh_tomatoes"""
    # Import unformated string from file
    full_list_file = open(r"movie_list.txt")
    # Convert string into 2-D list
    full_list = full_list_file.read().split("|")
    itemized_list = list(map(lambda x: x.split("* "), full_list))
    #Create list of Movie objects
    movie_list = []
    for i in range(0, len(itemized_list)):
        itemized_list[i][0] = itemized_list[i][0][1:]
        movie_list.append(media.Movie(itemized_list[i][0],
                                      itemized_list[i][1],
                                      itemized_list[i][2],
                                      itemized_list[i][3],
                                      itemized_list[i][4],
                                      itemized_list[i][5],
                                      itemized_list[i][6],
                                      itemized_list[i][7],
                                      itemized_list[i][8]))
    # Pass list to rendering module
    fresh_tomatoes.open_movies_page(movie_list)

# Run the main code
load_movie_site()
