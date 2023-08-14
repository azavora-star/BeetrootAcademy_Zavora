# Exercise 5: Movie Database
# Create a Movie class that represents a movie in a movie database. 
# The class should have various fields to store information about the movie, 
# such as its title, director, genre, release year, duration, and ratings. 
# Use public, private, and protected access modifiers appropriately. 
# Implement methods to update movie details, calculate average ratings, and display movie information.

class Movie:
    def __init__(self, title, director, genre, year, dur, rate):
        self.title = title
        self.director = director
        self.genre = genre
        self.year = year
        self.dur = dur
        self.rate = rate
         
    def display_info(self):
         print(f"Title: {self.title}, director: {self.director}, genre: {self.genre}, year: {self.year}, duration: {self.dur}, rating: {self.rate}")
         
    def update_info(self, title, director, genre, year, dur, rate):
        self.title = title
        self.director = director
        self.genre = genre
        self.year = year
        self.dur = dur
        self.rate = rate
        print(f"Title: {self.title}, director: {self.director}, genre: {self.genre}, year: {self.year}, duration: {self.dur}, rating: {self.rate}")
        
    def get_rate(self):
        return self.rate
    
my_movie = Movie("Titanic", "Cameron", "Drama", 1997, "2:45", 9)
# my_movie.display_info()
my_movie.update_info("Titanic", "Petro Cameron", "Drama", 1997, "2:48", 9)
# ​
# mov1 = Movie("Great Gatsby", "Lurmann", "Drama", 2013, "2:32", 8)
# mov2 = Movie("Barbie", "Del Toro", "Comedy", 2023, "1:48", 7)