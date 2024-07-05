from parser.parse_tsv import parse_tsv_file
from parser.parse_txt import parse_txt_file
from parser.parse_xlsx import parse_xlsx_file


def parse_file(file_path, params):
    """
    This function parses a file based on the extension of the file and returns the data

    Params:
    - file_path: path to the file to be parsed
    - params: parameters to be extracted from the file
    """

    try:
        if file_path.endswith(".tsv"):
            return parse_tsv_file(file_path, params)
        elif file_path.endswith(".txt"):
            return parse_txt_file(file_path, params)
        elif file_path.endswith(".xlsx"):
            return parse_xlsx_file(file_path, params)
        else:
            raise ValueError("Invalid file extension")

    except Exception:
        return "File not found or invalid file extension"
