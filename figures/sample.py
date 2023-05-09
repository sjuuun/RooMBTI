import pandas as pd
import plotly.graph_objects as go


def _sample_fake_data() -> pd.DataFrame:
    """
    This is for DP4, and this function generates sample fake data.
    In DP4, we need fake data, so please write data generation function here.
    Also, this function should be related with figure function in same file.

    :return: Generated data.
    """
    return pd.DataFrame()


def sample(df: pd.DataFrame) -> go.Figure:
    """
    Sample function for drawing a figure.
    Please each file should contain one figure function, and have same name with file name.
    e.g. scatter_plot.py has the function called scatter_plot

    :param df: Dataframe which contains the required data.
    :return: Figure.
    """
    return go.Figure()
