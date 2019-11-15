"""
Choose the number of coins, and flip between players to start pickup from 0 to 9 coins.
Try to avoid being the last player to play. The last one who picks the looser will be :)

Credit to: Hatem Gad
"""

n = int(input("Enter number of coins: "))

while True:
    print(n , "Coins")
   
    while True:
        x = int(input ("player 1 pick: "))
        if x > 9 or x < 1 or x > n:
            print("           Wrong Input! ")
            print("           You Will Enter Again! ")
        else:
            break
    n = n - x
    
    if n < 1:
        print ("PLAYER 2 WON")
        break
   
    print(n , "Coins")
   
    while True:
        x = int(input ("player 2 pick: " ))
        if x > 9 or x < 1 or x > n:
            print("           Wrong Input! ")
            print("           You Will Enter Again! ")
        else:
            break
    n = n - x
   
    if n < 1:
        print ("PLAYER 1 WON")
        break
