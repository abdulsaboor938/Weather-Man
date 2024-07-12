import os
import sys
from typing import Dict, List

# Ensure the root directory is in the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATA_DIR, PKT, MAX_TEMP, MIN_TEMP, MAX_HUMIDITY, MONTH_NAMES
from parser.parse_any import parse_file
from commands.utils import find_extreme_value_and_date, format_date


def handle_e_command(year: str, dir_path: str = DATA_DIR) -> Dict[str, Dict[str, str]]:
    """
    Parse files for given year and return highest temperature, lowest temperature,
    and max humidity along with dates.

    Args:
    year (str): Year for which data is to be displayed
    dir_path (str): Directory where data is stored

    Returns:
    dict: Parsed data in a structured format
    """
    files = [f for f in os.listdir(dir_path) if year in f]

    max_temp = {"value": [], "date": []}
    min_temp = {"value": [], "date": []}
    max_humidity = {"value": [], "date": []}

    for file in files:
        parsed_data = parse_file(
            os.path.join(DATA_DIR, file),
            [PKT, MAX_TEMP, MIN_TEMP, MAX_HUMIDITY],
        )

        for data_type, data_dict in [
            (MAX_TEMP, max_temp),
            (MIN_TEMP, min_temp),
            (MAX_HUMIDITY, max_humidity),
        ]:
            extreme = find_extreme_value_and_date(
                parsed_data[data_type],
                parsed_data[PKT],
                find_max=(data_type != MIN_TEMP),
            )
            data_dict["value"].append(extreme["value"])
            data_dict["date"].append(extreme["date"])

    return {
        "Highest": {
            "Temperature": f"{max(max_temp['value'])}C",
            "Date": format_date(
                max_temp["date"][max_temp["value"].index(max(max_temp["value"]))]
            ),
        },
        "Lowest": {
            "Temperature": f"{min(min_temp['value'])}C",
            "Date": format_date(
                min_temp["date"][min_temp["value"].index(min(min_temp["value"]))]
            ),
        },
        "Max Humidity": {
            "Humidity": f"{max(max_humidity['value'])}%",
            "Date": format_date(
                max_humidity["date"][
                    max_humidity["value"].index(max(max_humidity["value"]))
                ]
            ),
        },
    }
