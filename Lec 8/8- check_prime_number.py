def is_prime(num):
    """check prime number"""
    if num == 0 or num == 1:
        #print(num, 'is not a prime number')
        return False
    
    elif num in [2,3,5,7,11]:
        #print(num, 'is a prime number')
        return True
            
    elif not num % 2 == 0 and not num % 3 == 0 and not num % 5 == 0 and not num % 7 == 0 and not num % 11 == 0:
        #print(num, 'is a prime number')
        return True

    else:
        #print(num, 'is not a prime number')
        return False

def check_prime(upto_num):
    """store in a list only the prime numbers"""
    prime_list = []
    for i in range(upto_num):
        if is_prime(i):
            prime_list.append(i)

    return prime_list



        
            
    
