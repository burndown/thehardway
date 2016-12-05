from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
print line1
print line2
print line3
target.write("%s\n%s\n%s\n" % (line1,line2,line3))
s = line1 + '\n'
s2 = line2 + '\n'
s3 = line3 + '\n'
target.writelines([s, s2, s3])

print "And finally, we close it."
target.close()
