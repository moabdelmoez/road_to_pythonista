fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        
## Using the if else condition        
##        if word not in counts:
##            counts[word] = 1
##        else:
##            counts[word] += 1

## Using get method
        counts[word] = counts.get(word,0) + 1

print(counts)
