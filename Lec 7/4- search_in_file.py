import time

##start = time.time()
##fhand = open('mbox-short.txt')
##count = 0
##
##for line in fhand:
##    line = line.rstrip() #to remove the extra newline
##    if line.startswith("From:"):
##        print(line)
##end = time.time()
##print(end - start)

# structure the loop to skip the uninteresting lines

start = time.time()

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    #skip the uninteresting lines
    if not line.startswith("From:"):
        continue
    #process our interesting line
    print(line)

end = time.time()
print(end - start)
