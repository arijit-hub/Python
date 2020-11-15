import math

def semiperimeter(side1,side2,side3):

    '''(number,number,number)->float

    Returns the semiperimeter of a triangle with sides side1, side2 and side3

    >>>semiperimeter(2,3,4)
    4.5
    '''

    return (side1+side2+side3)/2

def triangle_area(side1,side2,side3):

    '''(number,number,number)->float

    Returns area of a triangle with sides side1, side2 and side3

    >>>triangle_area(3,4,5)
    6.0
    '''

    s=semiperimeter(side1,side2,side3)
    return math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
