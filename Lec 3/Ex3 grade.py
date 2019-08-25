score = input('Enter score: ')

try:
    score = float(score)
    if 0<=score<=100 and score >= 90:
        print('A')
    elif 0<=score<=100 and score >= 80:
        print('B')
    elif 0<=score<=100 and score >= 70:
        print('C')
    elif 0<=score<=100 and score >= 60:
        print('D')
    else:
        print('F')
except:
    print('Bad Score')
