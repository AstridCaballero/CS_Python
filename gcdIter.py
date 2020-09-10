def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''    
    if a == 1 or b == 1:
        return 1
    if a <= b:
        small = a
        big = b
        original = a
    else:
        small = b
        big = a
        original = b
    while small > 1:
        if big % small == 0 and original % small == 0:
                return small
        else:
            small -= 1            
    return 1

y = gcdIter(10, 12)