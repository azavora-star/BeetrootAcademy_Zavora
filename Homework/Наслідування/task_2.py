# Mathematician

# Implement a class Mathematician which is a helper class for doing math operations on lists

# The class doesn't take any attributes and only has methods:

#     square_nums (takes a list of integers and returns the list of squares)
#     remove_positives (takes a list of integers and returns it without positive numbers
#     filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'


class Mathematician:
    pass
    
    def square_nums(self, input_list: list):
        result = []
        for value in input_list:
            result.append(value **2)
        return result
    
    def remove_positives(self, input_list: list):
        result = [value for value in input_list if value <= 0]
        return result
    
    def filter_leaps(self, input_list: list):
        result = [year for year in input_list if year % 4 == 0]
        return result

 
m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
