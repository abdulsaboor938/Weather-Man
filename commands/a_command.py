import os
import sys

# Ensure the root directory is in the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATA_DIR

from parser.parse_any import parse_file


def handle_a_command(date, dir_path=DATA_DIR):
    """
    This function parses files for given year and gives highest temperature, lowest temperature and max humiidty along with dates

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

    # list all files in the directory containing year in the name
    file = [
        f for f in os.listdir(dir_path) if year in f and month_names[int(month)] in f
    ]

    if not file:
        print("No data found for the given date")
        return

    parsed_data = parse_file(
        "/Users/carbon/Desktop/Weather Man/data/weatherfiles/Murree_weather_2007_May.txt",
        ["Max TemperatureC", "Min TemperatureC", "Mean Humidity"],
    )

    # convert array elements to int
    parsed_data["Max TemperatureC"] = list(map(int, parsed_data["Max TemperatureC"]))
    parsed_data["Min TemperatureC"] = list(map(int, parsed_data["Min TemperatureC"]))
    parsed_data["Mean Humidity"] = list(map(int, parsed_data["Mean Humidity"]))

    print(
        f"\nHighest Average: {int(sum(parsed_data['Max TemperatureC'])/len(parsed_data['Max TemperatureC']))}C"
    )
    print(
        f'Lowest Average: {int(sum(parsed_data["Min TemperatureC"])/len(parsed_data["Min TemperatureC"]))}C'
    )
    print(
        f'Mean Humidity: {int(sum(parsed_data["Mean Humidity"])/len(parsed_data["Mean Humidity"]))}%'
    )
