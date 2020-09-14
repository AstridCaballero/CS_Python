def polysum(n, s):
    '''
    n, s: positive integers or floats

    returns: The sum of the area and square of the perimeter of the regular polygon, 
    rounded to 4 decimal places
    '''
    import math

    # Calculate area of polygon
    areaPol = (0.25 * n * math.pow(s, 2)) / (math.tan(math.pi/n))
    # Calculate perimeter of polygon
    perimeterPol = n * s
    # Calculate sum of the area and square of the perimeter of the regular polygon
    sumPol = areaPol + math.pow(perimeterPol, 2)
    return round(sumPol, 4)

y = polysum(3, 2)
