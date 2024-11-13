import requests

API_KEY = 'your_api_key'  # Replace with your OpenWeatherMap API Key
city = 'New Delhi'
url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat=28.6139&lon=77.2090&appid={API_KEY}'

response = requests.get(url)
data = response.json()

# Print the raw data to understand the structure
print(data)
import pandas as pd

# Sample data
data = {
    'datetime': ['2024-11-10 10:00', '2024-11-10 11:00', '2024-11-10 12:00'],
    'PM2.5': [120, 135, 110],
    'PM10': [150, 160, 155],
    'CO': [1.5, 1.7, 1.6],
    'NO2': [50, 55, 52],
    'SO2': [5, 6, 5],
    'O3': [60, 58, 61]
}

df = pd.DataFrame(data)

# Convert datetime column to proper datetime type
df['datetime'] = pd.to_datetime(df['datetime'])

# Check for missing values
print(df.isnull().sum())

# You can fill missing values, if any
df.fillna(method='ffill', inplace=True)

# Display the cleaned data
print(df.head())
# Basic statistics summary
print(df.describe())

# Correlation between pollutants
print(df.corr())

# Time-based trends (if datetime is available)
import matplotlib.pyplot as plt

# Plot PM2.5 levels over time
plt.plot(df['datetime'], df['PM2.5'], label='PM2.5', color='b')
plt.xlabel('Time')
plt.ylabel('PM2.5 Concentration (µg/m³)')
plt.title('PM2.5 Levels Over Time')
plt.legend()
plt.show()
import seaborn as sns

sns.pairplot(df[['PM2.5', 'PM10', 'CO', 'NO2', 'SO2', 'O3']])
plt.suptitle('Pollutant Pair Plot', size=16)
plt.show()
# Multiple pollutants over time
plt.figure(figsize=(10, 6))

plt.plot(df['datetime'], df['PM2.5'], label='PM2.5', color='b')
plt.plot(df['datetime'], df['PM10'], label='PM10', color='g')
plt.plot(df['datetime'], df['CO'], label='CO', color='r')
plt.plot(df['datetime'], df['NO2'], label='NO2', color='y')

plt.xlabel('Time')
plt.ylabel('Concentration (µg/m³ / ppm)')
plt.title('Air Quality Trends in New Delhi')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
import seaborn as sns
import numpy as np

# Plot heatmap for correlation between pollutants
corr_matrix = df[['PM2.5', 'PM10', 'CO', 'NO2', 'SO2', 'O3']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of Pollutants')
plt.show()
