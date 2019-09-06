def checkout():
    '''asking the user for prices and keeping a running total and count of items'''
    total = 0
    count = 0
    moreItems = True

    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price < 0: #in case the user enters a negative number
            print("Please enter a positive number")
            continue
        elif price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)
        else:
            moreItems = False

    if count == 0: #handle if user enters first thing 0, to avoid divide by 0
        print("Please enter a right price")
    else:
        average = total / count

        print('Total items:', count)
        print('Total $', total)
        print('Average price per item: $', average)

checkout()
    
