#http://learnpythonthehardway.org/book/ex16.html
#exercise 16: Reading and Writing Files
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file. Goodbye!"
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

newLines = line1 + "\n" + line2 + "\n" + line3 + "\n"
target.write(newLines)

target.close()

# read the file you just wrote to
target = open(filename, 'r')
print target.read()


print "And finally, we close it."
target.close()

# notes
# close = closes the file
# read - Reads the contents of the file. You can assign
#        the result to a variable
# readline - Reads just one line of a text file
# truncate - Empties the file. Careful if it's not version controlled.
# write('stuff') - Writes "stuff" to the file