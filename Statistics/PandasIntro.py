import numpy as np
import pandas as pd


def create_series():
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)


def create_data_frame():
    dates = pd.date_range("20100101", periods=6)
    print(dates)

    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    print(df)


def driver():
    create_data_frame()
