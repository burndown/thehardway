#load argv!
from sys import argv

# assign script and filename to argv!
script, filename = argv

#txt equal to the txt that open from the argv
txt = open(filename)
#print filename
print "Here is your file %r:" % filename
#print the txt
print txt.read()
#print the filename
print "Type the filename again:"
#new input from terminal
file_again = raw_input("> ")
#open the file again
txt_again = open(file_again)
#print the txt_again
print txt_again.read()
