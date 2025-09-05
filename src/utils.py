import json

import pandas as pd


def read_excel_file(path):
    """ Чтение xlsx файла. """
    
    df = pd.read_excel(path)
    return df.to_dict(orient='records')