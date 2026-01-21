import pandas as pd


def change_cell_value(df : pd.DataFrame, column : str, row_id : int, new_value : str | int | float) -> pd.DataFrame:
    """
    Changes cell's value in a DataFrame with a new value

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    column : str
        The name of the column to change.
    row_id : int
        The index of the row to change.
    new_value : str/int/float
        The new value to assign to the cell.
    
    
    Returns
    --------
    pd.DataFrame 
        DataFrame with the assigned new value
    """
    df_changed = df.copy()
    df_changed.loc[column,row_id] = new_value
    return df_changed
