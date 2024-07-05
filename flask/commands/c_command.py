import os
import sys

# Ensure the root directory is in the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATA_DIR

from parser.parse_any import parse_file


def handle_c_command(date, dir_path=DATA_DIR):
    """
    This function parses files for given year and prints graphs

    Params:
    - year: year for which data is to be displayed
    - dir_path: directory where data is stored
    """

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

    # find file
    year = date.split("/")[0]
    month = date.split("/")[1]

    # list all files in the directory containing year and month in the name
    file = [
        f for f in os.listdir(dir_path) if year in f and month_names[int(month)] in f
    ]


    if not file:
        print("No data found for the given date")
        return

    parsed_data = parse_file(
        (DATA_DIR+'/'+file[0]),
        ["Max TemperatureC", "Min TemperatureC", "Mean Humidity"],
    )

    # delete empty strings
    parsed_data["Max TemperatureC"] = [
        0 if x == "" else x for x in parsed_data["Max TemperatureC"]
    ]
    parsed_data["Min TemperatureC"] = [
        0 if x == "" else x for x in parsed_data["Min TemperatureC"]
    ]

    # convert array elements to int
    parsed_data["Max TemperatureC"] = list(map(int, parsed_data["Max TemperatureC"]))
    parsed_data["Min TemperatureC"] = list(map(int, parsed_data["Min TemperatureC"]))

    min_temperature = int(min(parsed_data["Min TemperatureC"]))

    return_dict ={}
    for i in range(len(parsed_data["Max TemperatureC"])):
        return_dict[i+1] ={
            "Max Temperature" : f"{'+'*(parsed_data["Max TemperatureC"][i]-min_temperature)} {parsed_data["Max TemperatureC"][i]}C",
            "Min_Temperature" : f"{'+'*(parsed_data["Min TemperatureC"][i]-min_temperature)} {parsed_data["Min TemperatureC"][i]}C"
        }

    return {"Date": f"\n{month_names[int(month)]} {year}", "Data": return_dict}