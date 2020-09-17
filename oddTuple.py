def oddTuples(aTup):
    # newTup = ()
    # for t in aTup:
    #     newTup = newTup + (t,)
    return aTup[::2]

y = oddTuples(('I', 'am', 'a', 'test', 'tuple'))
