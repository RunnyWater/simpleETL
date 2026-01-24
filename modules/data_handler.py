import pandas as pd

def get_data(file_name:str) -> pd.DataFrame:
    """
    Gets data from a file to DataFrame.

    Parameters
    ---------
    file_name : str
        The name of the file containing the data.

    Returns
    ---------
    pd.DataFrame
        The DataFrame from the file in a pd.DataFrame format.

    Notes
    --------
    Possible file_types:
        - 'csv' -> pd.read_csv()
        - 'excel' -> pd.read_excel()
        - 'json' -> pd.read_json()
        - 'xml' -> pd.read_xml()
        - 'html' -> pd.read_html()
        - 'sql' -> pd.read_sql()
    """

    file_type = file_name.split('.')[-1]
    file_types = {
        'csv': pd.read_csv, 
        'excel':pd.read_excel, 
        'json': pd.read_json,
        'xml': pd.read_xml,
        'html': pd.read_html,
        'sql': pd.read_sql
        }

    if file_type.lower() in list(file_types.keys()):
        df = file_types[file_type.lower()](file_name)
        return df
    else: 
        raise TypeError(f'Try using one of the supported file types:\n{', '.join(list(file_types.keys()))}')

def save_data(df : pd.DataFrame, file_name : str, file_type : str = 'csv', index : bool = True) -> None:
    """
    Saves DataFrame to a file.

    Parameters
    ---------
    df : pd.DataFrame
        The DataFrame containing the data.
    file_name : str
        The DataFrame will be saved to the file with this name.
    file_type : str, default='csv'
        The type of the saved file. See notes for more options.
    index : bool, default=True
        If True, will save the DataFrame with the index. If False, saved file will not contain index.

    Notes
    --------
    Possible file_types:
        - 'csv' -> df.to_csv()
        - 'excel' -> df.to_excel()
        - 'json' -> df.to_json()
        - 'xml' -> df.to_xml()
        - 'html' -> df.to_html()
        - 'sql' -> df.to_sql()
    """
    file_types = {
        'csv': df.to_csv, 
        'excel':df.to_excel, 
        'json': df.to_json,
        'xml': df.to_xml,
        'html': df.to_html,
        'sql': df.to_sql
        }
    
    if file_type.lower() in list(file_types.keys()):
        file_types[file_type.lower()](file_name+f'.{file_type}', index=index)
    else: 
        raise TypeError(f'Try using one of the supported file types:\n{', '.join(list(file_types.keys()))}')
