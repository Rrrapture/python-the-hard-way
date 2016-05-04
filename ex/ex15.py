# exercise 15 reading files
# system-specific import - argv command line arguments
# sys is a package. this gets the argv feature from package.
from sys import argv

# argv is a list expected to contain 2 values
# uses Python's unpacking notation you combine
#this will be ex15.py
# script = argv[0]
# and
# this will be ex15_sample.txt
# filename = argv[1]
# to one line

script, filename = argv

# txt is just a variable
# command - open the second argv parameter
# makes a file object. think dvd player is to dvd
# what file object is to file contents
txt = open(filename)

# prints the phrase with variable in phrase
print "Here's your file %r:" % filename
# prints the contents of the file
print txt.read()

print "Type the filename again:"
# variable that holds value from raw_input
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()