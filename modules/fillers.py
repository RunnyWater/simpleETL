import pandas as pd
from sklearn.impute import KNNImputer


def fill_na(df: pd.DataFrame, approach: str = 'mean', **args) -> pd.DataFrame:
    """
    Completes missing values in a DataFrame with chosen approach.

    Parameters
    ----------

    df : pd.DataFrame
        The DataFrame containing the data.

    approach : {'knn', 'hist'}, default='mean'
        An approach that will be used to fill in missing values. Possible values:
        - 'knn' -> Completing missing values using k-Nearest Neighbors
        - 'mean' -> Completing missing values using column's mean
    column : str
        Only write if there is a need to fill a specific column.
    n_neighbors : int, default=5
        Number of neighboring samples to use for imputation.
    
    ----------
    
    Returns
    -------
    pd.DataFrame
        DataFrame with completed missing values
    """
    
    if df.empty or df.shape[1] == 0:
        raise ValueError("DataFrame has no columns.")
    
    # value_as_nan = args.get('value_as_nan')    
    
    approaches = {
        'knn': fill_na_knn(df, columns=args.get('columns'), n_neighbors=args.get('n_neighbors', 5)),
        'mean': fill_na_mean(df, column=args.get('column', None))
    }
    if approach in approaches:
        return approaches[approach]
    else:
        raise ValueError(f"Unknown approach: {approach}")

def fill_na_mean(df : pd.DataFrame, column : str | None) -> pd.DataFrame:
    """
    Fills missing values using mean

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    column : str
        The column with missing values
    
    
    Returns
    -------
    pd.DataFrame 
        DataFrame with completed missing values

    """
    if not isinstance(column, str):
        raise ValueError("Column must be a string")
    elif isinstance(column, str) and column not in df.columns:
        raise KeyError(f"Column '{column}' does not exist in DataFrame.")
    
    mean_value = df[column].mean()
    column_filled = df.copy()[column].fillna(mean_value)
    df[column] = column_filled
    return df


def fill_na_knn(df:pd.DataFrame, columns: str | list[str] | None = None, n_neighbors : int = 5) -> pd.DataFrame:
    """
    Fills missing values using k-Nearest Neighbors.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    columns : str | list[str], default=None
        Specific columns to fill in.
    n_neighbors : int, default=5
        Number of neighboring samples to use for imputation.
    
    
    Returns
    -------
    pd.DataFrame 
        DataFrame with completed missing values
    """
    if df.empty or df.shape[1] == 0:
        raise ValueError("DataFrame has no columns for KNN imputation.")
    
    df_filled = df.copy()
    df_numerical = df_filled.select_dtypes(include=['int64', 'float64'])
    
    if df_numerical.empty or df_numerical.shape[1] == 0:
        raise ValueError("No numerical columns available for KNN imputation.")
    
    # Validate columns
    if columns is not None:
        if isinstance(columns, str):
            if columns not in df_numerical.columns:
                raise ValueError(f"Column '{columns}' not found in numerical columns.")
        elif isinstance(columns, list):
            missing_cols = [col for col in columns if col not in df_numerical.columns]
            if missing_cols:
                raise ValueError(f"Columns {missing_cols} not found in numerical columns.")
        else:
            raise ValueError("Columns must be a string, list of strings, or None.")
    
    imputer = KNNImputer(n_neighbors=n_neighbors)
    df_array = imputer.fit_transform(df_numerical)
    
    
    df_imputed = pd.DataFrame(df_array, index=df_numerical.index, columns=df_numerical.columns)
    if columns:
        df_filled[columns] = df_imputed[columns]
    else:
        df_filled.update(df_imputed)
    return df_filled