##f = open('mbox-short.txt', 'r')
##
##file_contents = f.read()
##
##f.close()

#by using context managers, no need to remember to
#close the file, it will be handled for you
with open('mbox-short.txt', 'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_count = len(words)

print(word_count)
