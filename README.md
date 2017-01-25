# nates-movie-picks
Server-side code that generates a website displaying some of Nate's top movie picks

Movie posters from some of Nate's favorite movies are displayed on flipping cards. When hovered-over, the cards turn to show detailed information about the movie. Clicking on a card loads a movie trailer viewable from within the current browser window.

This is a project created by Nathaniel Gindele for the **Udacity Full-Stack Web Development Nanodegree**. It is intended to satisfy the requirements for the project consumating _Programming Foundations with Python_. While making significant use of code from lecture videos and the provided version of `fresh-tomatoes.py`, Nate's Movie Picks has several important differences detailed in a subsequent section.

## Installation and Usage
After the file folder is copied to a local location, `entertainment_center.py` should be compiled. To guarantee full functionality, users should have installed Python 2.7, which may be downloaded [here](https://www.python.org/downloads/). This will generate a `nates_movie_picks.html` file which may be rendered using a web browser.

Movies may be added or *gasp* deleted by modifying `movie_list.txt`; however, all modifications to the movie list require written authorization from Nate. The first line of `movie_list.txt` must be blank and subsequent lines should contain information for only one film. Information should be entered in the following order:
1. Title
2. Release Date
3. Director
4. Tagline (put 'false' to leave blank)
5. Movie Poster URL
6. Movie Trailer URL
7. Genre
8. Rating (acceptable values: 'G', 'PG', 'PG-13', 'R', 'UR', 'NR')
9. Duration (in minutes)

Movie data are to be separated by a '*' followed by a space, and each line should conclude with a '|' (last entry excepted). Use the provided `movie_list.txt` for reference. Here are two sample entries, which, in the actual text file, should each only occupy a single line:

	American Movie* 1999* Chris Smith* false* https://upload.wikimedia.org/wikipedia/en/a/aa/Americanmovie.jpg* https://youtu.be/zMFZOu8rDUQ* Documentary* R* 107|

and
 
	Unforgiven* 1992* Clint Eastwood* It's a hell of a thing, killing a man* https://upload.wikimedia.org/wikipedia/en/4/4e/Unforgiven_2.jpg* https://youtu.be/H9NQz2GXGTg* Western* R* 141|

I believe that the use of copyrighted content in this program is considered Fair Use by the US Copyright Office; however, before uploading to a public server, one should take the time to acknowledge the authors of the original content. 

## Differences from Course-provided Content
##### `media.py`
Superfluous classes have been excised from `media.py`, while the Movie class has been expanded to include additional information. I would have liked to practice using inheritence concepts but decided it better to save this for a future project.
#### `entertainment_center.py`
This module was modified to accept a text file with stored movie information. This was done to maintain the readability of the Python file and make Nate's Movie Picks more user-friendly. The imported text file must be processed to remove markup characters and converted into a list of Movie objects which may be passed to `fresh_tomatoes.py`
#### `fresh_tomatoes.py`
This file now accepts modified Movie objects, which contain more information about the films. It also sorts the movies by title before rendering the tile grid. Formating changes made to the output file include:
+ Navagation bar color, font, shadow
+ Movie posters made into flippable cards
+ Box-shadows added to cards which move with animation
+ Additional film details provided on back of posters
