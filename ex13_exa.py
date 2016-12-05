from sys import argv

script, first, second, third = argv


print "The script is called:", script


print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

n1 = raw_input("the first one")
n2 = raw_input ("the second one")
n3 = raw_input ("the third one")
print "the %s, the %s, the %s" % (n1, n2, n3)
