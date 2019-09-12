while True:
    line = input('>  ')

    """if we change the logic of the if condition
    for example to start with check #, the code will crash"""

    # to handle if the user did not enter anything but just press enter
    if len(line) == 0 or line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)

print('Done!')
