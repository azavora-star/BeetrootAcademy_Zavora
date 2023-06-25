# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,


values= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
keys= [1, 2, 3, 4, 5, 6, 7]

dictionary = dict(zip(keys, values))
print(dictionary)

dictionary_reverted = dict(zip(values, keys))
print(dictionary_reverted)