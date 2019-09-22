txt = 'but soft what light in yonder window breaks'

words = txt.split()

t = list()

for word in words:
    t.append((len(word), word)) #to list the len and word
    #print(t)

t.sort(reverse=True) #tells sort to go in decreasing order
#print(t)

res = list() #to list only the words

for length, word in t:
    res.append(word)

print(res)
