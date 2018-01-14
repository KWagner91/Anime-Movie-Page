import webbrowser


class Movie(object):
    def __init__(self, movie_title, year, regisseur, movie_storyline, poster_image, trailer):
	"""Initialize the movie instance with different arguments:
		  movie_title: title of the movie
		  year: year of movie release
		  regisseur: who made the movie?
		  movie_storyline: short plot summary from IMDB
		  poster_image: image of the movie poster
		  trailer: link to movie trailer
  
		Returns: 
			None"""
		
        self.title = movie_title
        self.year_of_release = year
        self.regisseur = regisseur
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer


    def show_trailer(self):
		"""Function to open Movie URL with default Webbrowser.
		Expected Output: 
			Webbrowser with trailer URL"""
		webbrowser.open(self.trailer_url)
