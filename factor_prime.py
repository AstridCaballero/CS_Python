def factor(x):
    '''
     input: integer number
     output: biggest factor number that is also a prime
    '''
    #  create a list to store the factors
    factors = []
    big_prime = 0
    for num in range(1,(x + 1)):        
        if x % num == 0:    
            a = x // num
            # finish looping as soon as it finds a value that is already in the list
            if (num in factors) or (a in factors):
                break
            # store both factors in the list
            else:
                factors.append(num)
                factors.append(a)
            # check if factors are prime
            if prime(a) == True:
                # update big_prime if a is greater than current big_prime
                if a > big_prime:
                    big_prime = a
    print(factors)
    return big_prime

def prime(x):
    '''
    input: integer number greater than one
    output: boolean representing True or False for a prime number. Number that
    only divides by itself and 1 (only has two factors)
    '''

    for num in range(2,((x//2) + 1)):
        if x % num == 0:
            return False
    
    return True

y = factor(230589765438)