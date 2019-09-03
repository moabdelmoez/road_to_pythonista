##def new_square(x):
##    #y = x * x
##    count = 1
##    total = 0
##
##    while x >= count:
##        total = total + x
##        count = count + 1
##        #print(total)
##
##    return total

##print(new_square(4))

def square(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal + x

    return runningtotal

toSquare = 10
squareResult = square(toSquare)
print("The result of", toSquare, "squared is", squareResult)
