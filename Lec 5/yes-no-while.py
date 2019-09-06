def get_yes_or_no(message):
    '''function that asks a yes-or-no question'''
    valid_input = False
    while not valid_input:
        answer = input(message)
        answer = answer.upper() # convert to upper case
        if answer == 'Y' or answer == 'N':
            valid_input = True
        else:
            print('Please enter Y for yes or N for no.')
    return answer

response = get_yes_or_no('Do you like lima beans? Y)es or N)o: ')
if response == 'Y':
    print('Great! They are very healthy.')
else:
    print('Too bad. If cooked right, they are quite tasty.')
