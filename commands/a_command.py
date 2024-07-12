import os
import sys

# Ensure the root directory is in the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATA_DIR, MONTH_NAMES, MAX_TEMP, MIN_TEMP, MEAN_HUMIDITY
from parser.parse_any import parse_file
from commands.utils import convert_to_int, remove_empty_strings, calculate_average


def handle_a_command(date, dir_path=DATA_DIR):
    """
    Parse files for given year and provide highest temperature,
    lowest temperature and max humidity along with dates.

    Args:
    date (str): Date in format "YYYY/MM"
    dir_path (str): Directory where data is stored

    Returns:
    dict: Parsed data in a structured format
    """
    year, month = date.split("/")

    # List all files in the directory containing year and month in the name
    file = [
        f for f in os.listdir(dir_path) if year in f and MONTH_NAMES[int(month)] in f
    ]

    if not file:
        return {"message": "No data found for the given date"}

    parsed_data = parse_file(
        os.path.join(DATA_DIR, file[0]),
        [MAX_TEMP, MIN_TEMP, MEAN_HUMIDITY],
    )

    # Remove empty strings and convert to integers
    for key in [MAX_TEMP, MIN_TEMP, MEAN_HUMIDITY]:
        parsed_data[key] = convert_to_int(remove_empty_strings(parsed_data[key]))

    # Calculate and return averages
    return {
        "Highest Average": f"{calculate_average(parsed_data[MAX_TEMP])}C",
        "Lowest Average": f"{calculate_average(parsed_data[MIN_TEMP])}C",
        "Mean Humidity": f"{calculate_average(parsed_data[MEAN_HUMIDITY])}%",
    }
