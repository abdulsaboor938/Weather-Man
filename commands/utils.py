from config import MONTH_NAMES


def convert_to_int(data_list):
    """Convert all elements in a list to integers."""
    return list(map(int, data_list))


def remove_empty_strings(data_list, default_value=0):
    """Replace empty strings in a list with a default value."""
    return [default_value if x == "" else x for x in data_list]


def calculate_average(data_list):
    """Calculate the average of a list of numbers."""
    return int(sum(data_list) / len(data_list))


def find_extreme_value_and_date(
    data: list[str], pkt: list[str], find_max: bool = True
) -> dict[str, str]:
    """Find the extreme (max or min) value and its corresponding date."""
    func = max if find_max else min
    extreme_value = func(data)
    extreme_date = pkt[data.index(extreme_value)]
    return {"value": extreme_value, "date": extreme_date}


def format_date(date_str: str) -> str:
    """Format the date string."""
    month, day = date_str.split("-")[1:]
    return f"{MONTH_NAMES[int(month)]} {day}"
