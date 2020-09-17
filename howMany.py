def how_many(aDict):
    count = 0
    for value in aDict.values():
        count += len(value)
        # print each letter of all values
        for element in value:
            for i in element:
                print(i) 
            print('\n')       
    return count


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

y = how_many(animals)