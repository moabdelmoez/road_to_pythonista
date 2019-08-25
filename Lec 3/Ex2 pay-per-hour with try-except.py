hours = input('Enter Hourse: ')
rate = input('Enter rate: ')

try:
    hours = int(hours)
    rate = int(rate)
    if hours > 40:
        pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
    else:
        pay = (rate * hours)
    print(pay)
except:
    print('Error, please enter numeric number')
