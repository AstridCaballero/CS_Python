def parenth(array):
    '''
    input an array of parenthesis
    output number of missing parenthesis
    '''
    open = 0
    close = 0   
    for e in array:
        # check if parenthsesis is closed
        if e == ')':
            #  check if close parenthesis is zero, which means is missing an open parenthesis
            # and the next elements won't be able to balance it.
            if close == 0:
                # increase the number of open parenthesis needed to get '( )'
                open += 1
            # if already we need a close parenthesis(because there are open ones) 
            # then decrease the number of close parenthesis needed to get '( )'
            else:
                close -= 1
        # if the parenthesis is opened
        else:
            # Increase the number of close parenthesis needed to get '( )'
            close += 1        
    return (close + open)  

x = [')','(',')',')',')']
y = parenth(x)