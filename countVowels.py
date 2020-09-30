def countVowels(word):
    '''
    input: string
    output: integer number representing the count of vowels in the string
    '''
    count = 0
    for i in word:
        if i.lower() in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count