# Exercise 13: Parameters, Unpacking, Variables
# you can call sys a "feature" - it's officially called a module. aka library.
from sys import argv# this is an import statement
# argv is the argument variable

script, first, second, third = argv# unpacks the argument variables

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
