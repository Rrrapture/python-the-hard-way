#https://learnpythonthehardway.org/book/ex18.html
#def makes a function in python!
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I don't have anything."

print_two("Ahmed", "Honey Belle")
print_two_again("Ahmed", "Honey Belle")
print_one("Single!")
print_none();