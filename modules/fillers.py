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
        - 'mean' -> Compleating missing values using column's mean
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
    

    column = args.get('column')
    # value_as_nan = args.get('value_as_nan')
    if column is not None and column not in df.columns:
        raise KeyError(f"Column '{column}' does not exist in DataFrame.")
    
    approaches = {
        'knn': fill_na_knn(df, column=column, n_neighbors=args.get('n_neighbors', 5)),
        'mean': fill_na_mean(df, column) if column else df
    }
    if approach in approaches:
        return approaches[approach]
    else:
        raise ValueError(f"Unknown approach: {approach}")

def fill_na_mean(df : pd.DataFrame, column : str) -> pd.DataFrame:
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
    mean_value = df[column].mean()
    column_filled = df.copy()[column].fillna(mean_value)
    df[column] = column_filled
    return df

def fill_na_knn(df:pd.DataFrame, column: str | None = None, n_neighbors : int = 5) -> pd.DataFrame:
    """
    Fills missing values using k-Nearest Neighbors.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    column : str, default=None
        The column with missing values.
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
    if (df_numerical.empty or df_numerical.shape[1] == 0) or (column and column not in df_numerical.columns):
        raise ValueError("No numerical columns available for KNN imputation.")
    
    imputer = KNNImputer(n_neighbors=n_neighbors)
    df_array = imputer.fit_transform(df_numerical)
    
    
    df_imputed = pd.DataFrame(df_array, index=df_numerical.index, columns=df_numerical.columns)
    if column:
        df_filled[column] = df_imputed[column]
    else:
        df_filled.update(df_imputed)
    return df_filled