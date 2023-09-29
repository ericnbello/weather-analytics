# %% [markdown]
# # Analyzing Weather Data from OpenWeather.org
# 
# For this project, I analyzed weather data sourced from OpenWeather.org. This endeavor aimed to showcase my proficiency in data analysis, visualization, and communication of insights. I began by setting up my Python environment, leveraging essential libraries like requests, pandas, and matplotlib to ensure smooth data retrieval, manipulation, and visualization.

# %%
import requests
import pandas as pd
import matplotlib.pyplot as plt

# %% [markdown]
# To access the wealth of weather data provided by OpenWeather.org, I secured an API key. This unique identifier grants me the necessary authorization to query their API and obtain real-time weather information. Acquiring this API key involved registering on OpenWeather.org's platform.
# 
# Additionally, as it's important to keep it private, I placed it in a local file and used an environment variable to reference it throughout the project.

# %%
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get('OPENWEATHER_API_KEY')
city = 'Miami'
country_code = 'us'

# %%
# Forecast data
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city},{country_code}&cnt=40&appid={api_key}'
response = requests.get(url)
data = response.json()

# %% [markdown]
# By querying OpenWeather.org's API, I retrieved a 5-day forecast for Miami. This resulted in a JSON object containing a wealth of information about the upcoming weather. I then extracted key metrics such as temperature, humidity, and weather descriptions.

# %%
forecast_list = data['list']

# Initializing lists to store data
timestamps = []
temperatures = []
humidities = []
weather_descriptions = []

# Extracting data
for entry in forecast_list:
    timestamps.append(entry['dt'])
    temperatures.append(entry['main']['temp'])
    humidities.append(entry['main']['humidity'])
    weather_descriptions.append(entry['weather'][0]['description'])

# Creating a DataFrame to organize this data for further analysis and visualization
df = pd.DataFrame({
    'Timestamp': timestamps,
    'Temperature (K)': temperatures,
    'Humidity (%)': humidities,
    'Weather': weather_descriptions
})

df.head()

# %% [markdown]
# ### Clean and Explore Data
# 
# Before visualization, I took a moment to preprocess the data. This involved converting temperature from Kelvin to Celsius for easier interpretation. Additionally, I explored the dataset to understand the nature and scope of the information I had gathered.

# %%
# Convert temperature from Kelvin to Celsius
df['Temperature (C)'] = df['Temperature (K)'] - 273.15

# Explore the dataset
print(df.head())

# %% [markdown]
# ### Visualize the Data
# 
# With the data organized, it was time to breathe life into it through visualizations. I began with a line chart to display the temperature trends over the 5-day period.

# %%
# Plotting temperature trends
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['Temperature (C)'], marker='o')
plt.title('Temperature Trends over 5 Days')
plt.xlabel('Timestamp')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# %% [markdown]
# Additionally, I created a histogram to provide insights into the distribution of humidity levels over this period.

# %%
# Plotting histogram for humidity distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Humidity (%)'], bins=20, color='skyblue', edgecolor='black')
plt.title('Humidity Distribution')
plt.xlabel('Humidity (%)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# %% [markdown]
# In this phase, I meticulously documented my analysis. I began by providing context about the data source and the objectives of the project. I then detailed the steps taken in each phase, from data retrieval to visualization. Additionally, I highlighted key observations and insights gleaned from the weather data.

# %% [markdown]
# ### Conclusion
# 
# In this analysis, I retrieved weather data from OpenWeather.org for Miami. After obtaining the data, I performed data cleaning to convert temperatures from Kelvin to Celsius for better understanding.
# 
# The visualizations I created gave a clear overview of the forecasted temperature and humidity levels. These insights can be used to draw conclusions about the future weather conditions in Miami.
# 

# %% [markdown]
# ### Additional
# 
# This project complements the Django web app I created written in Python that shows current weather conditions, 48-hour and 7-day forecasts, local radar, and more for a user inputted location. View it [here](https://www.weather-forecast-ericnbello.herokuapp.com).


