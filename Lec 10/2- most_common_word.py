import string

fhand = open('romeo-full.txt')
counts = dict()

for line in fhand:
    #remove all the punctuation
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()

    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

#sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

#show the top common 10 words
for key, val in lst[:10]:
    print(key, val)

