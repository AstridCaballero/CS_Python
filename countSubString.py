def countSubString(s):
    '''
    input: string s
    output: integer number representing the number of times a substring
    appears in s
    '''

    count = 0    
    for i in range(len(s) - 2):
        if s[i] == 'b' and s[i + 1] == 'o' and s[i + 2] == 'b':   
            count += 1
    return count


y = countSubString('obobodbobobbebbob')