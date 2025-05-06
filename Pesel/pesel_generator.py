import random
from datetime import datetime, timedelta

def generate_pesel(birth_date=None, gender=None):
    """
    Generuj poprawny numer PESEL.
    """
    if birth_date is None:
        # Generate random date between 1900-01-01 and 2099-12-31
        start_date = datetime(1900, 1, 1)
        end_date = datetime(2099, 12, 31)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        birth_date = start_date + timedelta(days=random_number_of_days)
    
    # Generate random 4-digit number
    random_number = random.randint(0, 9999)
    
    # Format the random number with leading zeros
    random_str = f"{random_number:04d}"
    
    # Determine century marker
    year = birth_date.year
    if 1900 <= year <= 1999:
        century_marker = 0
    elif 2000 <= year <= 2099:
        century_marker = 2
    elif 2100 <= year <= 2199:
        century_marker = 4
    elif 2200 <= year <= 2299:
        century_marker = 6
    elif 1800 <= year <= 1899:
        century_marker = 8
    else:
        raise ValueError("Year must be between 1800 and 2299")
    
    # Format date parts
    year_str = str(year % 100).zfill(2)
    month_str = str(birth_date.month + century_marker).zfill(2)
    day_str = str(birth_date.day).zfill(2)
    
    # Generate gender digit (odd for male, even for female)
    if gender is None:
        gender_digit = random.randint(0, 9)
    else:
        if gender.upper() == 'M':
            gender_digit = random.choice([1, 3, 5, 7, 9])
        elif gender.upper() == 'K':
            gender_digit = random.choice([0, 2, 4, 6, 8])
        else:
            raise ValueError("Gender must be 'M' or 'K'")
    
    # Create PESEL without control digit
    pesel_without_control = year_str + month_str + day_str + random_str[:3] + str(gender_digit)
    
    # Calculate control digit
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    sum_ = sum(int(pesel_without_control[i]) * weights[i] for i in range(10))
    control_digit = (10 - (sum_ % 10)) % 10
    
    # Return complete PESEL
    return pesel_without_control + str(control_digit)

def validate_pesel(pesel):
    """
    Validate if a given PESEL number is correct.
    
    Args:
        pesel (str): PESEL number to validate
    
    Returns:
        bool: True if PESEL is valid, False otherwise
    """
    if len(pesel) != 11 or not pesel.isdigit():
        return False
    
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    sum_ = sum(int(pesel[i]) * weights[i] for i in range(10))
    control_digit = (10 - (sum_ % 10)) % 10
    
    return control_digit == int(pesel[10])
