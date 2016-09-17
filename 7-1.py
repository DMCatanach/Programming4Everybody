#write program that prompts for file name, opens that file, reads through the file, and prints contents uppercase
fname = raw_input("Enter file name: ")
try: 
	fh = open(fname)	
except: 
	print 'Could not open file:', fname
	exit()

#inp = fh.read()
#inp = inp.rstrip()
#print inp.upper()

#Alternately, for loop 
fhand = open(fname)
for line in fhand: 
	line = line.rstrip().upper()
	print line