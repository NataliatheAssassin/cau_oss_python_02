"""
This is a module named figure.
It can be used to calculate areas of various shapes.
"""

import math # Called this module to use PI and sqrt.

class Line:
    """
    It can be used to generate a valid line.
    """
    __length = 1
    def __init__(self, value=1):
        """
        Can set its length when instantiating.
        """
        if (value > 0 and (type(value) == int or type(value) == float)):
            self.__length = value
        else:
            value = 1

    def set_length(self, value):
        """
        Setter of length.
        """
        if (value > 0 and (type(value) == int or type(value) == float)):
            self.__length = value

    def get_length(self):
        """
        Getter of length.
        """
        return self.__length
    
def area_square(line):
    # Here is the way to use this function.
    """Calculates square's area.
    Args:
        line (int or float): refers to the side of the square.
    Returns:
        int or float: returns the area of square.
    """
    if (type(line) == Line):
        return line.get_length()**2
    else:
        return 0

def area_circle(line):
    # Here is the way to use this function.
    """Calculates circle's area.
    Args:
        line (int or float): refers to the radius of the circle.
    Returns:
        int or float: returns the area of circle.
    """
    if (type(line) == Line):
        return line.get_length()**2 * math.pi
    else:
        return 0

def area_regular_triangle(line):
    # Here is the way to use this function.
    """Calculates regular triangle's area.
    Args:
        line (int or float): refers to the side of the regular triangle.
    Returns:
        int or float: returns the area of regular triangle.
    """
    if (type(line) == Line):
        return line.get_length()**2 * math.sqrt(3)/4
    else:
        return 0