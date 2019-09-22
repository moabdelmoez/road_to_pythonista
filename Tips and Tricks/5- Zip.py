names = ['Peter Parker', 'Clark Kent', 'Wade Wilson',
          'Bruce Wayne']

heroes = ['Spiderman', 'Superman', 'Deadpool',
          'Batman']

##for index, name in enumerate(names):
##    hero = heroes[index]
##    print(f'{name} is actually {hero}')

#by using zip function

##for name, hero in zip(names, heroes):
##    print(f'{name} is actually {hero}')

#printing a tuple for all of these values
for value in zip(names, heroes):
    print(value)
