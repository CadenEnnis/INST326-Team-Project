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
    Validate that the container dimensions are reasonable sizes for the garden.
    
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


def validate_boolean_input(value: bool) -> bool:
    """
    Validate that the input is strictly a Python boolean (True or False).

    Parameters:
        value (bool): The value to check.

    Returns:
        bool: True if the value is a boolean, False otherwise.

    Raises:
        TypeError: If the input is not a boolean.
    """
    if not isinstance(value, bool):
        # Raising an error is robust, but for a "simple" utility,
        # often we just check and return False, but the assignment requires
        # robust error handling, so TypeError is appropriate here.
        raise TypeError("Input must be a standard boolean (True or False).")
    return True
#Sara Shokouhian

from datetime import datetime

def format_planting_date(date_str: str) -> str:
    """
    Formats a date string into a standard YYYY-MM-DD format.

    Parameters:
        date_str (str): The date string to format (e.g., '3/1/2025').

    Returns:
        str: The date formatted as YYYY-MM-DD.

    Raises:
        TypeError: If date_str is not a string.
        ValueError: If the date_str cannot be parsed into a valid date.
    """
    if not isinstance(date_str, str):
        raise TypeError("Date must be provided as a string.")
        
    try:
        # Attempt to parse common formats (m/d/y, m-d-y)
        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
    except ValueError:
        try:
            date_obj = datetime.strptime(date_str, '%m-%d-%Y')
        except ValueError:
            raise ValueError(f"Date format is invalid or unparsable: {date_str}")
            
    return date_obj.strftime('%Y-%m-%d')
#Sara Shokouhian

def parse_plant_species(full_name: str) -> str:
    """
    Extracts the Genus (the first word) from a scientific plant name.

    Parameters:
        full_name (str): The full scientific name (e.g., 'Solanum lycopersicum').

    Returns:
        str: The genus name.

    Raises:
        TypeError: If full_name is not a string.
        ValueError: If the name is empty or does not contain a space (unlikely to be a full species name).
    """
    if not isinstance(full_name, str):
        raise TypeError("Scientific name must be a string.")
        
    cleaned_name = full_name.strip()
    if not cleaned_name:
        raise ValueError("Scientific name cannot be empty.")
        
    # Split the name by spaces and take the first part
    name_parts = cleaned_name.split()
    if len(name_parts) == 0:
        # Should be caught by empty check, but as a safeguard
        raise ValueError("Could not parse genus from the provided name.")
        
    # Capitalize the genus for standard representation
    return name_parts[0].capitalize()
#Sara Shokouhian

def is_valid_ph_level(ph_value: float) -> bool:
    """
    Validate that a soil pH value is a number and is within the valid range of 0.0 to 14.0.

    Parameters:
        ph_value (float): The pH measurement to validate.

    Returns:
        bool: True if the pH is valid, False otherwise.

    Raises:
        TypeError: If ph_value is not an int or float.
    """
    if not isinstance(ph_value, (int, float)):
        raise TypeError("pH value must be a number.")
        
    # The pH scale ranges from 0 (most acidic) to 14 (most basic).
    if 0.0 <= ph_value <= 14.0:
        return True
    else:
        return False
#Sara Shokouhian

def calculate_plant_space(length, width = None, count = 1, shape = 'rectangle'):
    """
    Help to calculate what estimated amount of spacing is needed between plants in our containers.

    Parameters:
        length (float): Container length in inches
        width (float): Container width in inches
        count (int): Number of plants
        shape (str): 'rectangle' or 'circle'

    Returns:
        float: Needed space in inches.

    Raises:
        ValueError: If count invalid
        ValueError: Shape measurement is empty
        ValueError: Shape unknown
    """
    if count <= 0:
        raise ValueError("Count of plants must be a positive number.")

    #Calculate area based on shape
    if shape == 'rectangle':
        if width is None:
            raise ValueError("Width must be provided for rectangle.")
        area = length * width
    elif shape == 'circle':
        radius = length / 2
        area = math.pi * radius ** 2
    else:
        raise ValueError("Shape is not recognized.")

    #Divide area by number of plants to get the area per plant.
    area_per_plant = area / count

    #Estimated spacing as the square root of area per plant.
    spacing = math.sqrt(area_per_plant)
    return spacing
#Mai-Tien Pham

def calculate_compost_needed(soil_volume, target_ratio = 0.25):
    """
    Calculate the estimated amount of compost based on the volume of soil needed to maintain plants.

    Parameters:
        soil_volume (float): Total soil volume in cubic inches.
        target_ratio (float): Desired compost ratio wanted (range from 0.0 to 1.0, default ratio is 0.25)

    Returns:
        float: needed compost amount
        float: needed soil amount

    raises: 
        ValueError: If soil volume is negative
        ValueError: Target ratio is outside 0.0 and 1.0.
    """
    if soil_volume <= 0:
        raise ValueError("Soil volume must be a positive number.")
    if not (0.0 <= target_ratio <= 1.0):
        raise ValueError("Target ratio must be between 0.0 and 1.0.")

    compost_needed = soil_volume * target_ratio
    soil_needed = soil_volume - compost_needed

    return {
        'compost_ratio_needed': compost_needed
        'soil_ratio_needed': soil_needed
    }
#Mai-Tien Pham

def calculate_season_change(current_date = None):
    """
    Calculate the estimated amount of time (in days) before the season's change.

    Parameters:
        current_date: The current date of the user using the function. If none, default will be today's date.

    Returns:
        str: next_season
        int: days_remaining

    Raises:
        TypeError: If current_date is invalid
    """

    if current_date is none:
        current_date = datetime.today()
    elif not isinstance(current_date, datetime):
        raise TypeError("Date is invalid.")

    #Approximate of season start dates (year, month, day)
    year = current_date.year
    spring = datetime(year, 3, 20)
    summer = datetime(year, 6, 21)
    fall = datetime(year, 9, 22)
    winter = datetime(year, 12, 21)

    if current_date < spring:
            next_season = 'Spring'
            season_date = spring
        elif current_date < summer:
            next_season = 'Summer'
            season_date = summer
        elif current_date < fall:
            next_season = 'Fall'
            season_date = fall
        elif current_date < winter:
            next_season = 'Winter'
            season_date = winter
        else:
            # After winter starts, next season is Spring of next year
            next_season = 'Spring'
            season_date = datetime(year + 1, 3, 20)

    days_remaining = (season_date - current_date).days

    return {
        'current_date': current_date.strftime('%Y-%m-%d'),
        'next_season': next_season,
        'season_start_date': season_date.strftime('%Y-%m-%d'),
        'days_remaining': days_remaining
    }
#Mai-Tien Pham

def to_date(value):
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        parts = value.split("/")
        if len(parts) != 3:
            raise ValueError("Use MM/DD/YYYY format.")
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])
        return date(year, month, day)
    else:
        raise TypeError("Enter a date or a string in MM/DD/YYYY format.")
# Joshua Henderson

def days_until_frost(today: Dateish, first_frost_date: Dateish) -> int:
    """
    Calculate days until the first frost date.
    Returns 0 if the frost date is today or it has passed.
    """
    t = _to_date(today)
    f = _to_date(first_frost_date)
    delta_days = (f - t).days
    return delta_days if delta_days > 0 else 0
#Joshua Henderson

def is_safe_to_plant(plant_date, last_frost, tolerance="tender", extra_days=0):
    """ Check if it's safe to plant based on frost tolerance."""
    p = to_date(plant_date)
    l = to_date(last_frost)

    tolerance = tolerance.lower()

    if tolerance == "tender":
        offset = 0
    elif tolerance == "half-hardy":
        offset = -7    
    elif tolerance == "hardy":
        offset = -14  
    else:
        raise ValueError("Tolerance must be tender, half-hardy, or hardy.")

    safe_day = l + timedelta(days=offset + extra_days)
    if p >= safe_day:
        return True
    else:
        return False

# Joshua Henderson

def estimate_harvest_yield(plant_type, plant_count, avg_per_plant=None):
    """Estimate total harvest yield using simple defaults."""
    if plant_count < 0:
        raise ValueError("Plant count must be 0 or more.")

    plant_type = plant_type.lower()

    # Random amount of LB default  yields
    defaults = {
        "tomato": 8.0,
        "pepper": 3.0,
        "cucumber": 5.0,
        "zucchini": 6.0,
        "eggplant": 4.0,
        "lettuce": 1.0,
        "kale": 1.5,
        "bush bean": 2.0
    }

    if avg_per_plant is not None:
        per_plant = avg_per_plant
    elif plant_type in defaults:
        per_plant = defaults[plant_type]
    else:
        raise ValueError("Unknown plant type. Please give avg_per_plant value.")

    total = per_plant * plant_count

    return {
        "plant": plant_type,
        "plants": plant_count,
        "each": per_plant,
        "total": round(total, 2)
    }

#Joshua Henderson
