import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data/weatherfiles")
PKT = "PKT"
MAX_TEMP = "Max TemperatureC"
MIN_TEMP = "Min TemperatureC"
MAX_HUMIDITY = "Max Humidity"
MEAN_HUMIDITY = "Mean Humidity"
MONTH_NAMES = {
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
