import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np

def get_columns_with_missing_values(
        df : pd.DataFrame, 
        column_types : str | list[str] | None = None
    ) -> pd.DataFrame:
    """
    Return a DataFrame containing only columns with missing values, optionally filtered by data types.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    column_types: str | list[str] | None, default=None
        The specific column_types needed to be included.

    Returns
    -------
    pd.DataFrame
        A DataFrame subset containing only the columns with missing values (and matching the specified types, if any).
    """
    missing_cols = df.columns[df.isnull().any()]
    if column_types is not None:
        return df[missing_cols].select_dtypes(include=column_types) # type: ignore
    else:
        return df[missing_cols]
    

def get_columns_by_type(df : pd.DataFrame, types : list[str], exclude : bool = False) -> pd.DataFrame:
    """
    Gets columns by provided types.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    types : list[str]
        A selection of types to be included/excluded.
    exclude : bool, default=False
        If True, excludes columns of the specified types; if False, includes them.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing only the columns matching the specified types.

    Notes (ref. df.select_dtypes())
    -----
    * To select all *numeric* types, use ``np.number`` or ``'number'``
    * To select strings you must use the ``object`` dtype, but note that this will return *all* object dtype columns. With ``pd.options.future.infer_string`` enabled, using ``"str"`` will work to select all string columns.
    * See the `numpy dtype hierarchy <https://numpy.org/doc/stable/reference/arrays.scalars.html>`__ * To select datetimes, use ``np.datetime64``, ``'datetime'`` or ``'datetime64'`` 
    * To select timedeltas, use ``np.timedelta64``, ``'timedelta'`` or ``'timedelta64'``
    * To select Pandas categorical dtypes, use ``'category'``
    * To select Pandas datetimetz dtypes, use ``'datetimetz'`` or ``'datetime64[ns, tz]'``
    """
    if exclude:
        chosen_columns = df.copy().select_dtypes(exclude=types) # type: ignore
    else:
        chosen_columns = df.copy().select_dtypes(include=types) # type: ignore
    return chosen_columns


def encode_columns(
        df : pd.DataFrame, 
        columns : list[str]|None = None, 
        types : list[str] = ['category'], 
        encode_null : bool = False, 
        embedded : bool = False
    ) -> dict:
    """
    Gets encoded columns with encoders.

    
    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    columns : list[str], default=None
        Specific columns that need encoding.
    encode_null : bool, default=False
        If True, it will encode missing values as well; If False, it will save missing values in encoded data.
    embedded : bool, default=False
        If True, the function will return encoded columns with the DataFrame; If False, it will only return encoded columns

    Returns
    --------
    dict : { 'encoded':pd.DataFrame, 'encoders':dict{column_name:LabelEncoder()} }
        Return a dictionary that consists of two key-value pairs:
        - 'encoded' : pd.DataFrame 
            The DataFrame containing the encoded data.
        - 'encoders' : dict{column_name:LabelEncoder()}
            The dictionary of columns as key and its' Encoder as value. Encoders can be used to decode columns with encoder.inverse_transform([encoded[column]]).
    """
    if columns is not None:
        chosen_columns = columns
    else:
        chosen_columns = get_columns_by_type(df, types).columns

    encoders = {}
    object_df = pd.DataFrame(index=df.index)

    df_temp = df.copy()
    for column in chosen_columns:
        if encode_null:
            series = df_temp[column]
        else: 
            series = df_temp[column].dropna()

        encoder = LabelEncoder()
        encoder.fit(series.dropna())
        encoders[column+'_encoded'] = encoder
        encoded = series.map(lambda x: encoder.transform([x])[0] if pd.notnull(x) else np.nan) # type: ignore

        if embedded:
            df_temp[column + '_encoded'] = encoded
        else:
            object_df[column + '_encoded'] = encoded
        
    if embedded:
        return {'encoded': df_temp, 'encoders': encoders}
    else: 
        return {'encoded': object_df, 'encoders': encoders}

def delete_column(df : pd.DataFrame, column : str) -> pd.DataFrame:
    """
    Deletes column from DataFrame.

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