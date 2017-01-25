"""Renders a movie website displaying cards with movie posters on the front and
film details on the reverse side.
"""

import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Nate's Movie Picks</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link href="https://fonts.googleapis.com/css?family=Special+Elite" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin: 50px;
            perspective: 1000px;
            height: 342px;
            width: 220px; 
        }
        .movie-tile:hover {
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .container {
            position: relative;
        }
        .card {
            transition: 1s;
            transform-style: preserve-3d;
            height: 342px;
            width: 220px;
            background-color: #EEEEEE;
            box-shadow: 0px 4px 4px #BBBBBB;
        }
        .movie-tile:hover .card {
             transform: rotateY(180deg);
             box-shadow: 0px 6px 5px #BBBBBB;
         }
         .face {
             position: absolute;
             width: 100%;
             height: 100%;
             backface-visibility: hidden;
             display: block;
         }
        .face.back {
            display: block;
            transform: rotateY(180deg);
        }
        .rating_square {
            border: 1px solid #666666;
            padding: 2px 2px 2px 3px;
            font-weight: bold;
        }
        .first_line {
            display: inline;
            margin-bottom: 20px;
        }
        .first_line_container {
            width: 100%;
            margin: 10% 0 10% 0;
        }
        .movie_name {
            margin-top: 16px;
            font-weight: bold;
        }
        .release_date {
            margin: -6px; 
        }
        .tagline_text {
            font-size: 16px;
            margin: 20% 8px 20% 8px;
        }
        #top-bar {
            background-color: black;
            background-image: none;
            height: 64px;
            border: none;
            padding: 8px 0 16px 0;
            box-shadow: 0px 4px 15px hsla(0, 0%, 10%, .5);
        }
        .navbar-inverse .navbar-brand {
            font-family: 'Special Elite', courier;
            font-size: 46px;
            color: #D50000;
            font-weight: normal;
        }

        .navbar-inverse:hover .navbar-brand {
            color: #EF5350;
        }
        .top-part {
            height: 83%;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.face', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div id="top-bar" class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Nate's Movie Picks</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
# This has been changed from the Udacity provided file to accommodate
# additional information to be displayed and a flipping animation to be
# implemented.

movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <div class="card">
        <!-- Front of "flipping" card -->
        <div class="front face">
            <img src="{poster_image_url}" width="220" height="342">
        </div>
        <!-- Back of "flipping" card -->
        <div class="back face" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
            <div class="top-part">
                <h4 class="movie_name">{movie_title}</h4>
                <h5 class="release_date">({movie_date})</h5>
                <div class="first_line_container">
                    <h6 class="rating_square first_line">{rating}</h6>
                    <h6 class="first_line">&emsp;|&emsp;{genre}&emsp;|&emsp;{duration}min</h6>
                </div>
                <p class="tagline_text"><em>{tagline}</em></p>
            </div>
            <p>Directed by {director}</p>
        </div>
    </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        # Append the tile for the movie with its content filled in
        # Changed from original to accommodate additional movie information
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_date=movie.date,
            director=movie.director,
            tagline=movie.tagline,
            rating=movie.rating,
            duration=movie.duration,
            genre=movie.genre
        )
    return content


def open_movies_page(movies):
    #Sorts movies by title
    movies.sort(key=lambda x: x.title)

    # Create or overwrite the output file
    output_file = open('nates_movie_picks.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
