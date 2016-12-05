#import argv from sys!
from sys import argv
#assign filename, input_file to argv!
script, input_file = argv
#define print_all function, pint the read file#
def print_all(f):
    print f.read()

#define rewind functon, seek from position
def rewind(f):
    f.seek(2)
#define print one line, print line, and
def print_a_line(line_count, f):
    print line_count, f.readline()
#assign the parameter from the cmd to current_file
current_file = open(input_file)

#print
print "First let's print the whole file: \n"

#print all
print_all(current_file)
#print one by one
print "Now let's rewind, kind of like a tape."
# why need rewind function
rewind(current_file)

print "Let's print three lines:"
#print line1
current_line = 1
print_a_line(current_line, current_file)
print current_line

#print line2
current_line += 1
print_a_line(current_line, current_file)
print current_line
#print line3
current_line += 1
print_a_line(current_line, current_file)
print current_line
