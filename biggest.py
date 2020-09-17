def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    myFreqs = {}
    for k in aDict:
        # Get number/frequency of values in each key
         myFreqs[k] = len(aDict[k])
    # Get only values from myFreqs
    values = myFreqs.values()
    # Get max number from 'values'
    best = max(values)    
    # Will store the key with the highest frequency
    letter = ''
    for k in myFreqs:
        if myFreqs[k] == best:
            letter = k
    return letter



animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

y = biggest(animals)