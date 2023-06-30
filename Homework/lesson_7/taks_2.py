# Task 2

# Creating a dictionary.
# Create a function called make_country, which takes in a country’s name and capital as parameters. 
# Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. 
# Make the function print out the values of the dictionary to make sure that it works as intended.


# defining function
def make_country(names, capitals):
    country = dict(zip(names, capitals))
    print(country)

# lists of input
country_names = ['Croatia', 'Spain']
capitals = ['Zagreb', 'Madrid']

# calling funciton
make_country(country_names, capitals)