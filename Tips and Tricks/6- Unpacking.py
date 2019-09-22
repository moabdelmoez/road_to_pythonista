# Normal
items = (1, 2)

print(items)

# Unpacking

##a, b = (1, 2)
##
##print(a)
##print(b)

# if you are not going to use b variable, we can change it by
# underscore

#underscore means we are not going to use that value

##a, _ = (1,2)
##
##print(a)

##a, b, *c = (1, 2, 3, 4, 5)
##print(a)
##print(b)
##print(c)

a, b, *_ = (1, 2, 3, 4, 5)
print(a)
print(b)
