# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try: 
    fh = open(fname)
except:
    print 'Could not open file:', fname
    exit()

count = 0
total = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    colpos = line.find(':')
    conf = line[colpos+1:]
    fconf = float(conf)
    total = total + fconf
    count = count + 1 
    average = total/count
print 'Total:', total
print 'Count:', count
print 'Average spam confidence:', average

