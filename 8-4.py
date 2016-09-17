#download romeo file from www.py4inf.com/code/romeo.txt
#write program to read file line by line 
#split each line into word list using split function 
#check to see if each word is already in list, if not, add it 
#sort alphabetically and print 

fname = raw_input('Enter the file name: ')
try: 
	fhand = open(fname)
except: 
	print 'Sorry, could not open file ', fname
	exit()
words = list()
for line in fhand: 
	line = line.rstrip()
	line = line.split()
#	items = line.split()
	for word in line: 
		if not word in words: 
			words.append(word)	
words.sort() 

print words