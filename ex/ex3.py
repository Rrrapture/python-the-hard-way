print "I will now count my chickens:"

# 30 divided by 6 is 5, plus 25 is 30
print "Hens", 25 + 30 / 6
# Why isn't it times first, then modulus, 
# then 100 minus the result?
# 100 minus 25 is 75. 75 times 3 is 225. 225 divided by 4 is 
# 56 with 1 left over
# The remainder of 225 divided by 4 is 1.
# version 2:
# 25 times 3 is 75. 75 divided by 4 is 18 remainder 3
# OOOOH 100 - 3 is 97. I get it!
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

# 1/4 is .25 hmm floating point numbers?
# 3 plus 2 plus 1 is 6. 6 minus 5 is 1. 1 plus 4 is 5.
# 5 divided by 2 is remainder 1. 1 minus .25 is .75 plus 6 is
# 6.75. Does python just round this? How can the answer be 7?
# turns out 1 / 4 in python is 0.
# to be more accurate, use a floating point number,
# for instance 1.0 / 4, which evaluates to .25.
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

# 3 plus 2  is 5. 5 minus 7 is negative 2. 5 is NOT less than 
# negative 2. Therefore, this expression evaluates to False.
print 3 + 2 < 5 - 7

# this expression will print 5.
print "What is 3 + 2?", 3 + 2
# This expression will print negative 2.
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
