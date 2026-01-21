import pandas as pd


def get_rows(df : pd.DataFrame, start_row : int, end_row : int) -> pd.DataFrame:
    """
    Gets a subset of rows from the DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    start_row : int
        The index of the first row to return (inclusive).
    end_row : int
        The index of the last row to return (exclusive).
    
    
    Returns
    --------
    pd.DataFrame 
        DataFrame containing the selected rows 
    """
    return df.iloc[start_row:end_row]


def delete_row(df : pd.DataFrame, row_id : int) -> pd.DataFrame:
    """
    Deletes a row from DataFrame

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    row_id : int
        The index of the row to delete.
    
        
    Returns
    --------
    pd.DataFrame 
        Dataframe without the deleted column
    """
    return df.copy().drop([row_id])