# This file helps to read the csv file and return the data in the form of a dataframe.

import pandas as pd

def read_file(file_path):
    """
    This function reads the csv file and returns the data in the form of a dataframe.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        return "File not found!"
    except Exception as e:
        return str(e)