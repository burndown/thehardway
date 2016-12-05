#import argv from sys!

from sys import argv

script, input_file = argv

f = open(input_file)
print f.readline()
print f.readline()
print f.readline()
