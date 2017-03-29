# Learn Python the Hard Way, exercise 20
# https://learnpythonthehardway.org/book/ex20.html
#imports the argv parameter from the sys module which the
#interpreter uses
#fyi a module is a file consisting of Python code.
#a module can define functions (def), classes, and
#variables
#a module is a Python object that contains arbitrarily 
#defined attributes that you, you magic maker you,
# can bind and reference.
# the sys module provides access to command line arguments
# via sys.argv attribute
# the first argument is always the script name sys.argv[0]
from sys import argv

# set the `script` variable to the first argument,
# set the `input_file` variable to the second argument 
script, input_file = argv

print argv
print script
print argv[1]

#the function print_all() takes the variable f to mean a file
# think of a file in Python as a dvd player, or an old
# tape drive on a mainframe
# a file in Python has a "read head" and you can "seek" this
# read head to different positions and work from there.
# the print_all function executes the print command
# on the file object `f`
# read() is a method of file objects;
# so, take file object `f`, and read the entire contents (since
# the size isn't set as a numeric parameter), returning
# a string
# the print command outputs this string to the console.
# https://docs.python.org/2/tutorial/inputoutput.html
def print_all(f):
    print f.read()

# file.seek(0) in Python moves to the start of the file.
# `0` is the first byte, not the first line. The `seek` function
# works in bytes, not lines
def rewind(f):
    f.seek(0)

# file `readline` function reads a line from a file,
# Moving the read head to the right after `\n` ends that line
# define the print_a_line function, making it
# print the value of the line_count parameter followed
# by 
# the file object's readline() method reads a single line
# from a file, leaving a new line character `\n` at the end
# of the string. If readline() returns an empty string,
# the end of the file has been reached; a blank line
# is a string containing only  asingle new line. The return
# value of f.readline() is thus unambiguous.
def print_a_line(line_count, f):
    print line_count, f.readline()

# set a variable `current_file` to open the second 
# argument in the argv list
# interesting how it doesn't require setting the type
# open returns a file object
# so here the current_file variable is set to the 
# input_file object!
current_file = open(input_file)

# this print command writes this text and adds a new line
# to the console.
print "First let's print the whole file:\n"

# execute the print_all function, passing the current file
# to the 
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# executes our rewind function, which goes to the start
# of the file
rewind(current_file)

#print this line to our output (console)
print "Let's print three lines:"

#set variable `current_line` to the number 1
#execute our print_a_line function, passing the value
#of current line (1) and the current_file object (remember
# that's the input file we passed to the sys module argv list)
current_line = 1
print_a_line(current_line, current_file)

# set the current line variable to the it's existing value
# plus 1. 1+1 equals 2 
current_line = current_line + 1

# execute our print_a_line function now that the value of 
# current line is 2. Remember our print_a_line
# function runs the file object's readline() method
# I guess it just goes line by line? How does it know which
# line it's on?
print_a_line(current_line, current_file)

# set the current line value to its existing value - 2 -
# plus 1. 2 + 1 = 3
current_line = current_line + 1
# execute the print_a_line function again
print_a_line(current_line, current_file)