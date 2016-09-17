text = "X-DSPAM-Confidence:     0.8475"
pos = text.find(':')
nstr = text[pos+1:]
num = float(nstr) 
print num