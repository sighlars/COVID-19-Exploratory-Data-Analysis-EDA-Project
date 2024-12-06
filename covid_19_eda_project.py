import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_path = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(data_path)

# # Inspect the dataset
# print(df.head())
# print(df.info())

print(df.isnull().sum())

# Drop columns with too many missing values
df.drop(columns=['excess_mortality', 'excess_mortality_cumulative_absolute'], inplace=True)

# Fill missing values in numeric columns with 0 (for cases, deaths, etc.)
df.fillna(0, inplace=True)

# Retain only relevant columns for analysis
df = df[['date', 'location', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'population']]

# Ensure date is in datetime format
df['date'] = pd.to_datetime(df['date'])
df['date'].head()

global_df = df[df['location'] == 'World']

# Plot total cases over time
plt.figure(figsize=(10, 6))
plt.plot(global_df['date'], global_df['total_cases'], label="Total Cases", color='blue')
plt.title('Total COVID-19 Cases Over Time (Global)')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.grid(True)
plt.show()

# Plot new cases over time
plt.figure(figsize=(10, 6))
plt.plot(global_df['date'], global_df['new_cases'], label="New Cases", color='orange')
plt.title('Daily New COVID-19 Cases (Global)')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.grid(True)
plt.show()

# Group data by location
country_df = df[df['location'].isin(['United States', 'India', 'Brazil', 'Russia', 'United Kingdom'])]

# Compare total cases for select countries
sns.lineplot(data=country_df, x='date', y='total_cases', hue='location')
plt.title('Total COVID-19 Cases: Country-Wise Comparison')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()

top_countries = df.groupby('location')['total_cases'].max().sort_values(ascending=False).head(10)
print(top_countries)






