"""
This module contains the implementation of the Bollinger Bands algorithm for AI CryptoTrader.
"""
import pandas as pd
import numpy as np
import talib

def compute_bollinger_bands(dataframe, n=20, dev=2):
  """
  Computes the upper and lower Bollinger Bands for a given dataframe.
  :param dataframe: Pandas dataframe containing OHLC data.
  :param n: Number of periods to compute the moving average.
  :param dev: Number of standard deviations to use for the bands.
  :return: Pandas dataframe containing the original OHLC data and the upper and lower Bollinger Bands.
  """
  # Compute rolling mean and standard deviation 
  rolling_mean = dataframe['close'].rolling(window=n).mean()
  rolling_std = dataframe['close'].rolling(window=n).std()

  # Compute upper and lower bands
  upper_band = rolling_mean + dev * rolling_std
  lower_band = rolling_mean - dev * rolling_std

  # Add bands to dataframe
  dataframe['upper_band'] = upper_band
  dataframe['lower_band'] = lower_band

  return dataframe

  
