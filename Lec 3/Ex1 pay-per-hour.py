hours = int(input('Enter hours: '))
rate = int(input('Enter rate: '))
                
if hours > 40:
    pay = ((40 * rate) + ((hours - 40) * (rate * 1.5)))
else:
    pay = hours * rate

print(pay)
