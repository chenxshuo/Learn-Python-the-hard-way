from sys import argv

script, filename = argv

print "We are going to erase %r" % filename
print "If you don't want that hit CTRL-c"
print "If you do want that hit ENTER"

raw_input("?")

print "Opening file......"
target = open(filename, "w")

print "Turncating the file."
target.truncate()

print "Now i'm going to ask you for three lines"

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "I'm gonna to write these to the file. "

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "Finally we close it "
target.close()


