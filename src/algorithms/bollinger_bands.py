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

def compute_bollinger_band_indicator(dataframe, n=20, dev=2):
  """
  Computes the Bollinger Bands indicator for a given dataframe.
  :param dataframe: Pandas dataframe containing OHLC data.
  :param n: Number of periods to compute the moving average.
  :param dev: Number of standard deviations to use for the bands.
  :return: Pandas dataframe containing the Bollinger Bands indicator.
  """
  # Compute rolling mean and standard deviation
  rolling_mean = dataframe['close'].rolling(window=n).mean()
  rolling_std = dataframe['close'].rolling(window=n).std()

  # Compute upper and lower bands
  upper_band = rolling_mean + dev * rolling_std
  lower_band = rolling_mean - dev * rolling_std

  # Compute indicator
  indicator = (dataframe['close'] - rolling_mean) / (dev * rolling_std)

  return indicator


def compute_talib_bollinger_bands(dataframe, n=20, dev=2):
  """
  Computes the upper and lower Bollinger Bands for a given dataframe using the TA-Lib library.
  :param dataframe: Pandas dataframe containing OHLC data.
  :param n: Number of periods to compute the moving average.
  :param dev: Number of standard deviations to use for the bands.
  :return: Pandas dataframe containing the original OHLC data and the upper and lower Bollinger Bands.
  """
  # Compute upper and lower bands using TA-Lib
  upper_band, middle_band, lower_band = talib.BBANDS(dataframe['close'], timeperiod=n, nbdevup=dev, nbdevdn=dev)

  # Add bands to dataframe
  dataframe['upper_band'] = upper_band
  dataframe['middle_band'] = middle_band
  dataframe['lower_band'] = lower_band

  return dataframe


### Advanced Approach

def compute_bollinger_bands_with_volatility(dataframe, n=20):
  """
  Computes the upper and lower Bollinger Bands for a given dataframe, using a dynamic volatility factor.
  :param dataframe: Pandas dataframe containing OHLC data.
  :param n: Number of periods to compute the moving average.
  :return: Pandas dataframe containing the original OHLC data and the upper and lower Bollinger Bands.
   """
   # Compute rolling mean and ATR
    rolling_mean = dataframe['close'].rolling(window=n).mean()
    atr = talib.ATR(dataframe['high'], dataframe['low'], dataframe['close'], timeperiod=n)

    # Compute upper and lower bands with dynamic volatility
    upper_band = rolling_mean + 2 * atr
    lower_band = rolling_mean - 2 * atr

    # Add bands to dataframe
    dataframe['upper_band'] = upper_band
    dataframe['lower_band'] = lower_band

    return dataframe


