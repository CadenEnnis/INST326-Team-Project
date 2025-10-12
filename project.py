import math


def calculate_area(length, width=None, shape='rectangle'):
    """
    Calculate the area of our containers.

    Parameters:
        length (float): Length in inches
        width (float): Width in inches
        shape (str): 'rectangle' or 'circle'

    Returns:
        float: area in square inches

    Raises:
        ValueError: if shape is unknown
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
#Caden Ennis

def validate_container_dimensions(length, width, depth):
    """
    Validate that the container dimensions are reasonable sizes for the gardem.
    
    Parameters:
        length(float): Length in inches
        width(float): width in inches
        depth(float): depth in inches

    Returns:
        bool: True if the dimensions are reasonable
    
    Raises: 
        ValueError: if dimensions are not reasonable
    """
    #Checking if the dimensions are positive numbers
    if length <= 0:
        raise ValueError("Length must be positive.")
    if width <= 0:
        raise ValueError("Width must be positive.")
    if depth <= 0:
        raise ValueError("Depth must be positive.")
    # Check maximum horizontal dimensions (20 feet = 240 inches)
    if length > 240:
        raise ValueError("Length is larger than maximum limit (240 inches).")
    if width > 240:
        raise ValueError("Width is larger than maximum limit (240 inches).")
    #Check depth limits (min 2 inch, max 48 inch)
    if depth < 2:
        raise ValueError("Depth is smaller than minimum limit of 2 inches.")
    if depth > 48:
        raise ValueError("Depth is larger than maximum limit of 48 inches.")
    return True
#Caden Ennis

def measurement_conversion(value, from_unit, to_unit):
    """
    Convert measurements using units of inches, feet, and centimeters.
    Parameters:
        value(float): Value to convert
        from_unit(str): inches, feet, centimeters
        to_unit(str): Target unit of inches, feet, centimeters

    Returns:
        float: converted value
    
    Raises: 
        ValueError: if units are invalid
    """

    #Defining the conversion factors
    in_to_ft = 1/12
    in_to_cm = 2.54
    ft_to_in = 12
    ft_to_cm = 30.48
    cm_to_in = 1/2.54
    cm_to_ft = 1/30.48

    #Validate units
    validate_units = ['in', 'ft', 'cm']
    if from_unit not in validate_units:
        raise ValueError("Invalid from_unit. Must be 'in', 'ft', or 'cm'.")
    if to_unit not in validate_units:
        raise ValueError("Invalid to_unit. Must be 'in', 'ft', or 'cm'.")   
#Caden Ennis

def calculate_soil_volume(length, width, depth, shape='rectangle'):
    """
    Calculate the volume of soil needed for a container.

    Parameters:
        length (float): Length in inches
        width (float): Width in inches
        depth (float): Depth in inches
        shape (str): 'rectangle' or 'circle'
    Returns:
        float: volume in cubic inches
    """
    if shape == 'rectangle':
        volume = length * width * depth
    elif shape == 'circle':
        radius = length / 2
        volume = math.pi * radius ** 2 * depth
    else:
        raise ValueError("The shape is not a rectangle or circle.")
    return volume
#Caden Ennis

    


