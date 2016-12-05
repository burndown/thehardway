#assign string to x#
x = "There are %d types of people." % 10
#assign string binary to binary#
binary = "binary"
#assign don't to do_not#
do_not = "Don't"
#assign binary to y#
y = "Those who know %s and those who %s." % (binary, do_not)

#print x#
print x
#print t#
print y

#print x#
print "I said: %r." % x
print "I also said: '%s'." % y

hilairous = False
joke_evaluation = "Isn't that joke so funny?# %r"

print joke_evaluation % hilairous

w = "This is the left side of..."
e = "a string with a right side."

print w + e
