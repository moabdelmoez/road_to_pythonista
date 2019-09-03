def square(x):
    y = x * x
    return y #y is local variable

number = 10

result = square(number)

print("the result of", number, "squared is", result)
