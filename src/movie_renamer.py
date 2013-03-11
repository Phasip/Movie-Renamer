from movie import Movie
from imdbquery import ImdbQuery
import os
import sys

def rename(filename):
	filename_without_extension = filename
	extension = ""
	
	if os.path.isdir(filename) == False: 
		filename_without_extension, extension = os.path.splitext(filename)
	    
	query = ImdbQuery.create_query_from_filename(filename_without_extension)
	movie = Movie.create_movie_from_imdb_query(query)
	if movie.title == "None":
#		sys.stdout.write("Query Was: " + query + "\n")
		return "None"
		
	return unicode(movie).encode("utf-8") + extension
