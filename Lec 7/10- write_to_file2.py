infile = open('qbdata.txt', 'r')
outfile = open('qbnames.txt', 'w')

line = infile.readline()

while line:
    items = line.split()
    dataline = items[1] + ',' + items[0]
    #print(dataline)
    outfile.write(dataline + '\n') #must add newline in the line end
    
    line = infile.readline()

infile.close()
outfile.close()
