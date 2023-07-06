def count_lines(name):
    with open(name) as file:
         print("The number of lines - " + str(len(file.readlines())))

def count_chars(name):
     with open(name) as file:
          print("The number of characters - " + str(len(file.read())))

def test(name):
     with open(name) as file:
          count_lines(name)
          count_chars(name)