infile = open('qbdata.txt', 'r')
line = infile.readline() #read the first line

while line: #if the line is empty the bool will be False
    values = line.split()
    print('QB', values[0], values[1])
    line = infile.readline() #read the next line

infile.close()
