import numpy as np
import matplotlib.pyplot as plt
import requests
import csv
import pandas as pd
import scipy.stats as stats
import os
import seaborn as sns


rng = 100

mu, sigma = 1, 3  # Mean and standard deviation
s = np.array([1,2,3,4])

def test_normality(rv, rv_name):
    alpha = 0.05
    stat, p_value = stats.shapiro(rv)
    if p_value > alpha:
        print(f'{rv_name}  is normal')
    else:
        print(f'{rv_name} is not normal')

def plot_rv(rv, rv_name, unit):
    counts, bins = np.histogram(rv)
    plt.stairs(counts, bins)
    plt.title(rv_name)
    plt.xlabel(f"{rv_name} ({unit})")
    plt.ylabel('Frequency')
    plt.show()


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
test_normality(bmw_i3_price,"bmw_i3_price")
plot_rv(bmw_i3_price,"bmw_i3_price","dollars")


#Odometer Reading
bmw_i3_odometer = df[(df["Make"] == "BMW")
                     & (df["Model"] == "i3")
                     & (df["Model Year"] == 2021)
                     & (df["Odometer Reading"] >5000 )
                    & (df["New or Used Vehicle"] == "Used")]["Odometer Reading"].values
test_normality(bmw_i3_odometer,"bmw_i3_odometer")
plot_rv(bmw_i3_odometer,"Bmw I3 odometer","miles")

print(f"mean odometer is {np.mean(bmw_i3_odometer)}")
print(f"std dev is {np.std(bmw_i3_odometer)}")

# check electric range Electric Range

bmw_i3_range = df[(df["Make"] == "BMW") &
                  (df["Model"] == "i3") &
                  (df["Model Year"] == 2021) &
                  (df["Electric Range"] >0 ) &
                  (df["New or Used Vehicle"] == "Used")]["Electric Range"].values

test_normality(bmw_i3_range,"bmw_i3_range")
plot_rv(bmw_i3_range,"BMW I3 range","miles")



# plot price vs odometer
price_vs_odom=df[(df["Make"] == "BMW")
                     & (df["Model"] == "i3")
                     & (df["Model Year"] == 2021)
                     & (df["Odometer Reading"] >500 )
                    & (df["New or Used Vehicle"] == "Used")]
print(np.corrcoef(price_vs_odom["Sale Price"].values,
                  price_vs_odom["Odometer Reading"].values))
#
# compute pair-wise correlalation of all columns to bmw_i3 range

# can't call correlation directly between string and float
# transform df string to float using one-hot encoding
price_vs_odom = pd.get_dummies(price_vs_odom)

corr_df = price_vs_odom.corr()
sns.heatmap(corr_df)
plt.show()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 9999)

# try to explain the electric range but apparently it static value coming from
corr_df[["Electric Range"]].sort_values(by="Electric Range")

pass


