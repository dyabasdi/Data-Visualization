import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data Wranging - the process of getting the data into an analysis-ready stage

# read file into dataframe
df = pd.read_csv('./files/cars.csv')

# Sanity checks
df.shape
print(df.head(5))
print(df.tail(5))

# Check for nulls/NaNs:
df.info()
df.describe()

# detect missing data
# replace '?' with NaN
df.replace('?', np.nan, inplace= True)
df.info()

# price is a string, not a float or int like it should be

# find the missing data
missing_data = df.isnull()
print(missing_data.head(10))

# count the missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print(' ')

# replace categorical data with the mode, remove if no price
columns = ['normalized-losses', 'stroke', 'bore', 'horsepower', 'peak-rpm']
for column in columns:
    avg = df[column].astype('float').mean(axis=0)
    df[column].replace(np.nan, avg, inplace=True)

df.info()

# gives us the mode
mode = df['num-of-doors'].value_counts().idxmax()
df['num-of-doors'].replace(np.nan, mode, inplace= True)

# remove rows with missing prices
df.dropna(subset= ['price'], axis=0,  inplace=True)
df.reset_index(drop= True, inplace=True)
print(df.tail())

# Check Correct Data Format
print(df.dtypes)
# convert to correct data type
df[['bore', 'stroke', 'peak-rpm']] = df[['bore', 'stroke', 'peak-rpm']].astype('float')
df[['normalized-losses', 'price', 'horsepower']] = df[['normalized-losses', 'price', 'horsepower']].astype('int')

# drop duplicates
df_no_dup = df.drop_duplicates()
print(df.shape)
print(df_no_dup.shape)

# no duplicates -> good to use df