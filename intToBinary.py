def intToBinary(x):
    '''
    input: integer number
    output: string. binary representation of integer number
    '''
    if x == 0:
        return str(0)
    elif x//2 == 0:
        return str(1)    
    else:
        return intToBinary(x//2) + str(x % 2)

y = intToBinary(3)