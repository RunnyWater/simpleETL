import pandas as pd


def delete_column(df : pd.DataFrame, column : str) -> pd.DataFrame:
    """
    Deletes column from DataFrame

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    column : str
        The name of the column to delete.
    
        
    Returns
    --------
    pd.DataFrame
        DataFrame without the deleted column
    """
    return df.copy().drop(columns=[column])