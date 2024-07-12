import os
import sys

# Ensure the root directory is in the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATA_DIR, MONTH_NAMES, MAX_TEMP, MIN_TEMP, MEAN_HUMIDITY
from parser.parse_any import parse_file
from commands.utils import convert_to_int, remove_empty_strings


def handle_c_command(date, dir_path=DATA_DIR):
    """
    Parse files for given year and print graphs.

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
        print("No data found for the given date")
        return

    parsed_data = parse_file(
        os.path.join(DATA_DIR, file[0]),
        [MAX_TEMP, MIN_TEMP, MEAN_HUMIDITY],
    )

    # Remove empty strings and convert to integers
    parsed_data["Max TemperatureC"] = convert_to_int(
        remove_empty_strings(parsed_data["Max TemperatureC"])
    )
    parsed_data["Min TemperatureC"] = convert_to_int(
        remove_empty_strings(parsed_data["Min TemperatureC"])
    )

    min_temperature = min(parsed_data["Min TemperatureC"])

    return_dict = {}
    for i, (max_temp, min_temp) in enumerate(
        zip(parsed_data["Max TemperatureC"], parsed_data["Min TemperatureC"]), 1
    ):
        return_dict[i] = {
            "Max Temperature": f"{'+'*(max_temp-min_temperature)} {max_temp}C",
            "Min Temperature": f"{'+'*(min_temp-min_temperature)} {min_temp}C",
        }

    return {"Date": f"\n{MONTH_NAMES[int(month)]} {year}", "Data": return_dict}
