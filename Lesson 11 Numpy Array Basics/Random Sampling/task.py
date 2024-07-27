import numpy as np
import matplotlib.pyplot as plt
import requests
import csv
import pandas as pd
import scipy.stats as stats
import os

rng = 100

mu, sigma = 1, 3  # Mean and standard deviation
s = np.array([1,2,3,4])

if not (os.path.exists("electric_cars_title.csv")):
    response = requests.get("https://data.wa.gov/api/views/rpr4-cgyd/rows.csv?accessType=DOWNLOAD")

# Check if the request was successful
    if response.status_code == 200:
        # Decode the content to string
        data = response.content.decode('utf-8')
    else:
        print("failed to download data")

    f=open("electric_cars_title.csv","w")
    f.write(data)
    f.close()

df = pd.read_csv("electric_cars_title.csv",delimiter=",",encoding = "ISO-8859-1")
bmw_i3_price = df[(df["Make"] == "BMW") &
                  (df["Model"] == "i3") &
                  (df["Model Year"] == 2021) &
                  (df["Sale Price"] >0 ) &
                  (df["New or Used Vehicle"] == "Used") &
                  (df["Odometer Reading"] >5000 )]["Sale Price"].values

# Perform the Shapiro-Wilk test
stat, p_value = stats.shapiro(bmw_i3_price)

# Print the results
print('Shapiro-Wilk Test:')
print(f'Statistic: {stat}')
print(f'p-value: {p_value}')

# Interpret the result
alpha = 0.05
if p_value > alpha:
        print('bmw i3  is normal')
else:
        print('bmw i3 price is not normal')

counts, bins = np.histogram(bmw_i3_price)
plt.stairs(counts, bins)
plt.title("bmw i3 price")
plt.show()

#Odometer Reading
bmw_i3_odometer = df[(df["Make"] == "BMW")
                     & (df["Model"] == "i3")
                     & (df["Model Year"] == 2021)
                     & (df["Odometer Reading"] >5000 )
                    & (df["New or Used Vehicle"] == "Used")]["Odometer Reading"].values
stat, p_value = stats.shapiro(bmw_i3_odometer)

counts, bins = np.histogram(bmw_i3_odometer)
plt.stairs(counts, bins)
plt.title("bmw i3 odometer")
plt.show()


print('Shapiro-Wilk Test:')
print(f'Statistic: {stat}')
print(f'p-value: {p_value}')

# Interpret the result
alpha = 0.05
if p_value > alpha:
        print('bmw i3 odometer  is normal')
else:
        print('bmw i3 odometer is not normal')

print(f"mean odometer is {np.mean(bmw_i3_odometer)}")
print(f"std dev is {np.std(bmw_i3_odometer)}")

# check electric range Electric Range

bmw_i3_range = df[(df["Make"] == "BMW") &
                  (df["Model"] == "i3") &
                  (df["Model Year"] == 2021) &
                  (df["Electric Range"] >0 ) &
                  (df["New or Used Vehicle"] == "Used")]["Electric Range"].values
stat, p_value = stats.shapiro(bmw_i3_range)

counts, bins = np.histogram(bmw_i3_range)
plt.stairs(counts, bins)
plt.title("bmw i3 range")
plt.show()

print('Shapiro-Wilk Test:')
print(f'Statistic: {stat}')
print(f'p-value: {p_value}')

# Interpret the result
alpha = 0.05
if p_value > alpha:
        print('bmw i3 range  is normal')
else:
        print('bmw i3 range is not normal')

# plot price vs odometer
price_vs_odom=df[(df["Make"] == "BMW")
                     & (df["Model"] == "i3")
                     & (df["Model Year"] == 2021)
                     & (df["Odometer Reading"] >5000 )
                    & (df["New or Used Vehicle"] == "Used")][["Odometer Reading","Sale Price"]]
print(np.corrcoef(price_vs_odom["Sale Price"].values,
                  price_vs_odom["Odometer Reading"].values))
exit(0)




