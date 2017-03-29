#Python the Hard Way exercise 19
#this function takes two arguments, and prints the first argument value,
#then the second argument value, then an exclamation sentence, then a command
#sentence followd by an extra line break
#I forget what the "d" is.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Woman that's enough for a party!"
	print "Get a basket.\n"

#the following command prints a sentence, then
#calls our cheese and crackers function, 
#passing number values for our cheese count
#and boxes_of_crackers values
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#the following command prints a sentence, sets the value of two
#variables to numbers, then calls our cheese and crackers function
#referencing the variables we just defined.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We could also do math inside, too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)