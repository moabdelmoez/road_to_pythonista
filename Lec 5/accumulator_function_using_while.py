def sumTo(num):
    """Return the sum of 1+2+3 ... n"""
    result = 0
    x_num = 1
    while x_num <= num:
        result = result + x_num
        x_num = x_num + 1

    return result

print(sumTo(4))
