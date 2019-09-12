data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

#find the @ position
at_pos = data.find('@')

#find the space after the @ position
space_pos = data.find(' ', at_pos)

#string slicing to extract the portion
hostname = data[at_pos+1:space_pos]

print(hostname)
