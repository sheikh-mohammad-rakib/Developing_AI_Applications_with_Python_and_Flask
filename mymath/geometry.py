import math

def area_of_rectangle(length, breadth):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        breadth (float): The breadth (width) of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * breadth

def area_of_circle(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * radius ** 2