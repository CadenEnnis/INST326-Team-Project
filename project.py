import math


def calculate_area(length, width=None, shape='rectangle'):
    """
    Calculate the area of our containers.

    Parameters:
        length (float): Length in inches (for circle, treated as diameter)
        width (float|None): Width in inches (ignored for circle)
        shape (str): 'rectangle' or 'circle'

    Returns:
        float: area in square inches

    Raises:
        ValueError: if shape is unknown or required inputs are missing
    """
    if shape == 'rectangle':
        if width is None:
            raise ValueError("Width must be provided for rectangle.")
        return length * width
    elif shape == 'circle':
        radius = length / 2
        return math.pi * radius ** 2
    else:
        raise ValueError("The shape is not recognized.")


if __name__ == '__main__':
    # quick smoke tests
    print("rectangle 4x3 ->", calculate_area(4, 3))
    print("circle diameter 4 ->", calculate_area(4, shape='circle'))




