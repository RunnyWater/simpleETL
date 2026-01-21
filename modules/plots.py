import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_plot(
        df: pd.DataFrame, 
        column: str, 
        bins: int = 30, 
        kind: str = 'hist', 
        color: str = 'skyblue', 
        edgecolor: str = 'black', 
        alpha: float = 0.7, 
        kde: bool = False
    ) -> None:
    """
    Plots a histogram or a normal (KDE) plot for a DataFrame column.
    
    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing the data.
    column : str
        The column to plot.
    bins : int, default=30
        Number of bins for the plot.
    kind : {'hist', 'kde'}, default='hist'
        Kind of the plot. Possible values:
        - 'hist' -> histogram.
        - 'kde' -> kernel density estimate (normal curve).
    color : str, default='skyblue'
        Color of the bars/line.
    edgecolor : str, default='black'
        Color of the bar edges.
    alpha : float, default=0.7
        Transparency of the bars/line.
    kde : bool, default=False
        If True, overlays a KDE curve on the plot.
    ----------
    """
    data = df[column].dropna()
    plt.figure(figsize=(8, 5))
    if kind == 'hist':
        plt.hist(data, bins=bins, color=color, edgecolor=edgecolor, alpha=alpha, density=True)
        if kde:
            sns.kdeplot(data.to_numpy(), color='red', linewidth=2)
        plt.title(f"Histogram of {column}")
        plt.xlabel(column[0].upper() + column[1:])
        plt.ylabel("Density")
    elif kind == 'kde':
        sns.kdeplot(data.to_numpy(), color=color, linewidth=2, fill=True, alpha=alpha)
        plt.title(f"KDE (Normal Curve) of {column}")
        plt.xlabel(column[0].upper() + column[1:])
        plt.ylabel("Density")
    plt.show()

