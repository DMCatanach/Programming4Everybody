#read through mbox-short.txt to find out who sent the most messages 
#"from" lines, second word of line is sender 
#Python dict maps sender to count of times appearing 
#max loop to find highest count 

name = raw_input('Enter the file name: ')
try: 
	fhand = open(name)
except: 
	print 'Sorry, could not open file ', name
	exit()
count = dict() 
for line in fhand: 
	line = line.rstrip()
	if not line.startswith('From '): continue #skip non-'from' lines and second occurences of 'from' so that each message counted only once
	#now we want to find the second word, that is, index 1, in each of the from lines and put them in a dictionary with the count 
	words = line.split() 
	count[words[1]] = count.get(words[1], 0) + 1 

bigcount = None 
bigword = None 
for word,count in count.items():  
	if bigcount is None or count > bigcount: 
		bigword = word 
		bigcount = count	
			
print bigword, bigcount		