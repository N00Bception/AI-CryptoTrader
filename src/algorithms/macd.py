import pandas as pd
import numpy as np


### Advanced approach

"""
This file contains the code for the MACD (Moving Average Convergence Divergence) indicator algorithm.
"""

def macd(df, n_fast=12, n_slow=26, n_signal=9):
  """
  Compute the MACD (Moving Average Convergence Divergence) indicator.
  Args:
    df (pandas.DataFrame): Dataframe containing the price data.
    n_fast (int): Number of periods for the fast EMA.
    n_slow (int): Number of periods for the slow EMA.
    n_signal (int): Number of periods for the signal line.

  Returns:
    pandas.DataFrame: Dataframe containing the MACD line, signal line and histogram.
"""

  # Compute the MACD line
  ema_fast = df['close'].ewm(span=n_fast, min_periods=n_fast).mean()
  ema_slow = df['close'].ewm(span=n_slow, min_periods=n_slow).mean()
  macd_line = ema_fast - ema_slow

  # Compute the signal line
  signal_line = macd_line.ewm(span=n_signal, min_periods=n_signal).mean()

  # Compute the MACD histogram
  macd_histogram = macd_line - signal_line

  # Combine the MACD line, signal line and histogram into a single dataframe
  macd_df = pd.DataFrame({'MACD': macd_line, 'Signal': signal_line, 'Histogram': macd_histogram})

  return macd_df


### Complex approach

"""
This file contains the code for the MACD (Moving Average Convergence Divergence) indicator algorithm.
"""
def macd(df, n_fast=12, n_slow=26, n_signal=9):
  """
  Compute the MACD (Moving Average Convergence Divergence) indicator.
  Args:
    df (pandas.DataFrame): Dataframe containing the price data.
    n_fast (int): Number of periods for the fast EMA.
    n_slow (int): Number of periods for the slow EMA.
    n_signal (int): Number of periods for the signal line.

  Returns:
    pandas.DataFrame: Dataframe containing the MACD line, signal line and histogram.
  """

  # Compute the exponential moving averages
  ema_fast = pd.Series(df['close']).ewm(span=n_fast).mean()
  ema_slow = pd.Series(df['close']).ewm(span=n_slow).mean()

  # Compute the MACD line
  macd_line = ema_fast - ema_slow

  # Compute the signal line
  signal_line = macd_line.ewm(span=n_signal).mean()

  # Compute the MACD histogram
  macd_histogram = macd_line - signal_line

  # Combine the MACD line, signal line and histogram into a single dataframe
  macd_df = pd.concat([macd_line, signal_line, macd_histogram], axis=1)
  macd_df.columns = ['MACD', 'Signal', 'Histogram']

  return macd_df


### State-of-art approach 

"""
This file contains the code for the MACD (Moving Average Convergence Divergence) indicator algorithm.
"""
def macd(df, n_fast=12, n_slow=26, n_signal=9):
   """
  Compute the MACD (Moving Average Convergence Divergence) indicator for a given dataframe.

  Args:
  df (pandas.DataFrame): The input dataframe containing the OHLC (Open, High, Low, Close) data of a cryptocurrency.
  n_fast (int, optional): The number of periods to use for the fast EMA calculation. Defaults to 12.
  n_slow (int, optional): The number of periods to use for the slow EMA calculation. Defaults to 26.
  n_signal (int, optional): The number of periods to use for the signal line calculation. Defaults to 9.

  Returns:
  pandas.DataFrame: A new dataframe containing the MACD line, signal line, and histogram values.

  """
  # Compute the EMA (Exponential Moving Average) values for the fast and slow EMAs
  ema_fast = df['close'].ewm(span=n_fast, min_periods=n_fast).mean()
  ema_slow = df['close'].ewm(span=n_slow, min_periods=n_slow).mean()
  
  # Compute the MACD line
  macd_line = ema_fast - ema_slow
  
  # Compute the signal line as a 9-period EMA of the MACD line
  signal_line = macd_line.ewm(span=n_signal, min_periods=n_signal).mean()
  
  # Compute the histogram as the difference between the MACD line and the signal line
  histogram = macd_line - signal_line
  
  # Create a new dataframe containing the MACD line, signal line, and histogram values
  macd_df = pd.DataFrame({'MACD': macd_line, 'Signal Line': signal_line, 'Histogram': histogram}, index=df.index)

  return macd_df
  
