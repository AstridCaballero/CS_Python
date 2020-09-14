def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) > 0:
        middle = len(aStr) // 2
        if char == aStr[middle]:
            return True
        else:
            if char > aStr[middle]:
                return middle >= 1 and isIn(char, aStr[middle + 1:]) 
            else:
                return middle != 0 and isIn(char, aStr[:middle])
    else:
        return False
        
y = isIn('g', "acdef")