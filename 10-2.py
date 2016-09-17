#using mailbox files 
#count distribution of hour of the day 
#loop through From lines 
#find time string and split at colon
#print counts, one per line, sorted by hour - thus hour is the key, number of occurences is value 

#opening the file
name = raw_input("Enter the file name: ")
if len(name) < 1 : name = "mbox-short.txt" #this line comes from the starter code in the autograder. It defaults to mbox-short.txt if you just hit 'Enter'
try: 
	fhand = open(name)
except: 
	print 'Sorry, could not open file ', name
	exit()
count = dict()	
#loop time 
for line in fhand: 
	line = line.rstrip()
	if not line.startswith('From '): continue 
	data = line.split()
	hour = data[5].split(':')
	count[hour[0]] = count.get(hour[0], 0) + 1

#sorting 	
lst = list()
for count, hour in count.items(): 
	lst.append ( (count, hour) )

lst.sort(reverse=False)
for hour, count in lst:
	print hour, count 	