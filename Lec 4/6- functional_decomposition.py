#functions can call each other

def square(x):
    y = x * x
    return y

def sum_of_squares(x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)

    return a + b + c

num1 = -5
num2 = 2
num3 = 10

result = sum_of_squares(num1, num2, num3)

print(result)
