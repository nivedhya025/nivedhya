import pandas as pd
import matplotlib.pyplot as mp
weather=pd.read_csv("BangaloreCity.csv")
print(weather.isnull().sum())
weather['tavg']=weather['tavg'].fillna(weather['tavg'].mean())
weather['tmin']=weather['tmin'].fillna(weather['tmin'].min()) 
weather['tmax']=weather['tmax'].fillna(weather['tmax'].mean()) 
print(weather.isnull().sum())
weather['time']=pd.to_datetime(weather['time'],format=("%d-%m-%Y"))
weather['Year']=weather['time'].dt.year
weather['month']=weather['time'].dt.month
print(weather)
yearly=weather.groupby('Year')["tavg"].mean().reset_index()
print(yearly)
mp.figure(figsize=(9,5))
mp.plot(yearly['Year'],yearly["tavg"],marker='o',color='red')
mp.title('Yearly Average Temperature in Bangalore (1990-2022)')
mp.xlabel('Year')
mp.ylabel('Average Temperature (°C)')
mp.show()


