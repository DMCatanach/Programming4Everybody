#uses mbox-short.txt from py4inf.com
#prints list of senders in file and keeps a count of how many lines containing the sender

fname = raw_input('Enter the file name: ')
try: #insurance for a bad file name
	fhand = open(fname)
except: 
	print 'Sorry, could not open file ', fname
	exit()
count = 0 
for line in fhand: 
	line = line.rstrip()
	if not line.startswith('From '): continue  #skip lines that don't start with "From" and the ones that start with "From:"
	words = line.split()
	count = count + 1 
	print words[1]
print "There were", count, "lines in the file with From as the first word"		

