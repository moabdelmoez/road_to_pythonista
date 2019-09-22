class Person():
    pass

person = Person()

##person.first = 'Mostafa'
##person.last = 'Osama'
##
##print(person.first)
##print(person.last)

#setatter (Set attribute)
##setattr(person, 'first', 'Mostafa') #(object, attribute, value)

##first_key = 'first'
##first_val = 'Mostafa'
##
##setattr(person, first_key, first_val)
##
###getattr (Get attribute)
##first = getattr(person, first_key)
##print(first)

person_info = {
    'first': 'Mostafa',
    'last': 'Osama'
    }

for key, value in person_info.items():
    setattr(person, key, value)

print(person.first)
print(person.last)

for key in person_info.keys():
    print(getattr(person, key))
