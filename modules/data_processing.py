import pandas as pd

def load_data(file):

    if (file.name.endswith('.csv')):
        return pd.read_csv(file)
    elif (file.name.endswith('.json')):
        return pd.read_json(file)
    elif (file.name.endswith('.xlsx')):
        return pd.read_excel(file)
    elif (file.name.endswith('.xls')):
        return pd.read_excel(file)
    else:
        raise Exception("File type not supported")
    

def get_data_info(data):
    # returns the dictionary of the data columns with their data types

    data_info = {}
    data_head = {}
    for column in data.columns:
        data_info[column] = str(data[column].dtype)
        data_head[column] = data[column].head()

    return data_info, data_head