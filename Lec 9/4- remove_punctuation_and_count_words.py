import string

fname = input("Please enter the file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opend!")
    exit()

counts = dict()

for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation)) #remove the puncuation from the line
##    print(line)
    line = line.lower()
    words = line.split()

    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)
