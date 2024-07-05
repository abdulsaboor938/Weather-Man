import os
import sys

# Ensure the root directory is in the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATA_DIR

from parser.parse_any import parse_file


def handle_e_command(year, dir_path=DATA_DIR):
    """
    This function parses files for given year and gives highest temperature, lowest temperature and max humiidty along with dates

    Params:
    - year: year for which data is to be displayed
    - dir_path: directory where data is stored
    """

    # list all files in the directory containing year in the name
    files = [f for f in os.listdir(dir_path) if year in f]

    # defining dictionaries to store data
    max_temp = {"date": [], "value": []}
    min_temp = {"date": [], "value": []}
    max_humidity = {"date": [], "value": []}

    # iterate and calculate metrics
    for i in files:
        parsed_data = parse_file(
            (DATA_DIR + "/" + i),
            ["PKT", "Max TemperatureC", "Min TemperatureC", "Max Humidity"],
        )

        # adding to datastructure
        max_temp["value"].append(max(parsed_data["Max TemperatureC"]))
        max_temp["date"].append(
            parsed_data["PKT"][
                parsed_data["Max TemperatureC"].index(max_temp["value"][-1])
            ]
        )

        min_temp["value"].append(min(parsed_data["Min TemperatureC"]))
        min_temp["date"].append(
            parsed_data["PKT"][
                parsed_data["Min TemperatureC"].index(min_temp["value"][-1])
            ]
        )

        max_humidity["value"].append(max(parsed_data["Max Humidity"]))
        max_humidity["date"].append(
            parsed_data["PKT"][
                parsed_data["Max Humidity"].index(max_humidity["value"][-1])
            ]
        )

    # defining dictionary for month names
    month_names = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec",
    }

    # returning the data
    max_temp_val = max_temp["date"][max_temp["value"].index(max(max_temp["value"]))]
    min_temp_val = min_temp["date"][min_temp["value"].index(min(min_temp["value"]))]
    max_humidity_val = max_humidity["date"][
        max_humidity["value"].index(max(max_humidity["value"]))
    ]

    return {
        "Highest": {
            "Temperature": f"{max(max_temp['value'])}C",
            "Date": f"{month_names[int(max_temp_val.split('-')[1])]} {max_temp_val.split('-')[2]}",
        },
        "Lowest": {
            "Temperature": f"{min(min_temp['value'])}C",
            "Date": f"{month_names[int(min_temp_val.split('-')[1])]} {min_temp_val.split('-')[2]}",
        },
        "Max Humidity": {
            "Humidity": f"{max(max_humidity['value'])}%",
            "Date": f"{month_names[int(max_humidity_val.split('-')[1])]} {max_humidity_val.split('-')[2]}",
        },
    }
