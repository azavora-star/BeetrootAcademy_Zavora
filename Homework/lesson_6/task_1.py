'''Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values. 
'''

words = ()
word_occurency = {}
sentence = input('Please enter a sentence:\n')

# converting string to a list
words = sentence.split()

# iterating through the list and updating dictionary 
for word in words:
  occurency = words.count(word)
  word_occurency.update({word: occurency})
print(word_occurency)
