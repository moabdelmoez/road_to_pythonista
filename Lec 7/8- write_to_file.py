fout = open('output.txt', 'w')
print(fout)

line1 = "My name is Mostafa\n"
fout.write(line1)

line2 = "I have a dream\n"
fout.write(line2)

fout.close()
