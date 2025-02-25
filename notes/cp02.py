import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# read a csv
df = pd.read_csv('./files/fit.csv')

# # sanity checks
# df.shape
# print(df.head(5))
# print(df.tail(5))

# # Check for nulls/NaNs:
# df.info()

# df.describe()
pd.options.display.max_rows = 200

######################################
#             Clean Data             #
######################################
# Data wrangling (cleaning)

# 4 things that make data messy:
# 1) Missing data (NaNs)
# 2) Data may not be in the right format or unit
# 3) Data out of range
# 4) Duplicate lines of data

# For missing values, if it makes sense, you can replace the it with the mean, mode, or median value
# Ex. Address or Social Security Number --> do NOT replace, just drop that row

# drop NaNs
new_df = df.dropna()
new_df.info()

# find the median of Calories
x = df['Calories'].median()
print(f'Calories Median {x}')

# replace all of the missing values with the median
new_df = df.fillna({'Calories':x})
new_df.info()

# find duplicates
print(df.duplicated())

new_df = df.drop_duplicates()
new_df.info()

######################################
#            Simple Plots            #
######################################

# get data again
df = pd.read_csv('./files/fit.csv')

# Scatter plot with good correlation
# df.plot(kind= 'scatter', x = 'Duration', y = 'Calories')
# plt.show()

######################################
#              Activity              #
######################################

df = pd.read_csv('./files/diamonds.csv')

# run 5 sanity checks

print(df.shape)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

# Select ideal cuts
df_ideal = df.loc[df['cut'] == 'Ideal']
print(df_ideal.shape)
print(df_ideal.head())

df['price_per_carat'] = df['price']/df['carat']
df['price_greater_than_5000'] = np.where(df['price_per_carat'] > 5000, 1, 0)
new_df = df.loc[df['price_greater_than_5000'] == 1]

print(new_df.describe())

######################################
#      Application of Functions      #
######################################

# increase price by 30%
df['price'] = df['price'] * 1.3

# add math function to round the price
df['rounded_price'] = df['price'].apply(math.ceil)

# apply a lambda function
df['rounded_price_100'] = df['price'].apply(lambda x: math.ceil(x/100)*100)

# user defined function
def func(x):
    y = math.ceil(x / 100) * 100
    return y

df['rounded_price_100'] = df['price'].apply(func)
print(df.head())