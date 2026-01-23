import pandas as pd

def get_data(file_name:str) -> pd.DataFrame:
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

def save_data(df: pd.DataFrame, file_name: str, file_type: str = 'csv', index:bool = True) -> None:
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
