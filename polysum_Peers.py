def polysum(n, s):
    '''
    n, s: positive integers or floats

    returns: a positive float, The sum of the area and square of the perimeter of the regular polygon
    rounded to 4 decimal places
    '''
    import math

    # Calculate area of polygon
    myarea = areaPol(n, s)
    # Calculate perimeter of polygon
    myperimeter = perimeterPol(n, s)
    # Calculate sum of the area and square of the perimeter of the regular polygon
    sumPol = myarea + math.pow(myperimeter, 2)
    # round number to 4 decimal places
    return round(sumPol, 4)

def areaPol(n, s):
    '''
    n, s: positive integers or floats

    returns: a positive float, the area of polygon.
    '''
    import math
    areaPol = (0.25 * n * math.pow(s, 2)) / (math.tan(math.pi/n))
    return areaPol

def perimeterPol(n, s):
    '''
    n, s: positive integers or floats

    returns: a positive float, the perimeter of polygon.
    '''
    import math
    perimeterPol = n * s
    return perimeterPol