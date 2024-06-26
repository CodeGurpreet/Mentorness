# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KQ5pbaBtl8cdTBWJmvUBnAUBEK79CE8l
"""

import pandas as pd

# Load the data with explicit encoding
data = pd.read_csv("/content/Super_Store_data.csv", encoding="latin-1")

# Display the first few rows to understand the structure
print(data.head())

import matplotlib.pyplot as plt

# Convert the date column to datetime format
data['Order Date'] = pd.to_datetime(data['Order Date'])

# Group by Order Date and sum the Sales
daily_sales = data.groupby('Order Date')['Sales'].sum().reset_index()

# Plot the time series data
plt.figure(figsize=(12, 6))
plt.plot(daily_sales['Order Date'], daily_sales['Sales'])
plt.title('Daily Furniture Sales')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Split data into train and test sets
train = daily_sales[:len(daily_sales)-365]
test = daily_sales[len(daily_sales)-365:]

# Fit the Exponential Smoothing model
model = ExponentialSmoothing(train['Sales'], trend='add', seasonal='add', seasonal_periods=7)
fit_model = model.fit()

# Forecast for the next year
forecast = fit_model.forecast(365)

# Plot the forecast
plt.figure(figsize=(12, 6))
plt.plot(train['Order Date'], train['Sales'], label='Train')
plt.plot(test['Order Date'], test['Sales'], label='Test')
plt.plot(test['Order Date'], forecast, label='Forecast')
plt.title('Exponential Smoothing Forecast')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()

# Decompose the time series into trend, seasonal, and residual components
from statsmodels.tsa.seasonal import seasonal_decompose

decomposition = seasonal_decompose(daily_sales['Sales'], model='additive', period=7)
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# Plot the components
plt.figure(figsize=(12, 10))

plt.subplot(411)
plt.plot(daily_sales['Order Date'], daily_sales['Sales'], label='Original')
plt.title('Original Time Series')

plt.subplot(412)
plt.plot(daily_sales['Order Date'], trend, label='Trend')
plt.title('Trend Component')

plt.subplot(413)
plt.plot(daily_sales['Order Date'], seasonal, label='Seasonal')
plt.title('Seasonal Component')

plt.subplot(414)
plt.plot(daily_sales['Order Date'], residual, label='Residual')
plt.title('Residual Component')

plt.tight_layout()
plt.show()

# Decompose the time series into trend, seasonal, and residual components
from statsmodels.tsa.seasonal import seasonal_decompose

decomposition = seasonal_decompose(daily_sales['Sales'], model='additive', period=7)
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# Plot the components
plt.figure(figsize=(12, 10))

plt.subplot(411)
plt.plot(daily_sales['Order Date'], daily_sales['Sales'], label='Original')
plt.title('Original Time Series')

plt.subplot(412)
plt.plot(daily_sales['Order Date'], trend, label='Trend')
plt.title('Trend Component')

plt.subplot(413)
plt.plot(daily_sales['Order Date'], seasonal, label='Seasonal')
plt.title('Seasonal Component')

plt.subplot(414)
plt.plot(daily_sales['Order Date'], residual, label='Residual')
plt.title('Residual Component')

plt.tight_layout()
plt.show()