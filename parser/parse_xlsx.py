import pandas as pd


def parse_xlsx_file(file_path, params):
    retrieved_data = {
        param: [] for param in params
    }  # Create a dictionary with keys as the parameters and empty arrays to store the data

    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Check if all requested params exist in the DataFrame columns
    for param in params:
        if param not in df.columns:
            raise ValueError(f"Parameter '{param}' not found in the Excel file columns")

    # Extract the data for each parameter and store in the respective arrays
    for param in params:
        retrieved_data[param] = df[param].tolist()

    return retrieved_data
