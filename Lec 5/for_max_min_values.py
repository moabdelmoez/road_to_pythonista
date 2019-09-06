largest = None #we did not put Zero because maybe there're negative numbers
print('Before:', largest)

for num in [3, 41, 12, 9, 74, 15]:
    if largest is None or num > largest:
        largest = num

    print('Loop:', num, largest)

print('Largest:', largest)
