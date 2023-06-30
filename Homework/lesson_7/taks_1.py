# Task 1

# A simple function. 
# Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. 
# The function should then print “My favorite movie is named {name}”.

# defining function
def favourite_movie(movie):
    print(f'My favourite movie is named {movie}')              

# input from user
movie = input('What is your favourite movie?\n')

# calling function
favourite_movie(movie)