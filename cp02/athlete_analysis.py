import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


df = pd.read_csv('./files/athlete_events.csv')

# run 5 sanity checks
# print(df.shape)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())

# get rid of people who didn't get medals -> df called winners

winners = df.dropna(subset='Medal')
winners.info()

year_2016 = winners[winners['Year'] == 2016]
year_2016.info()

# medal count for each category in 2016
print(year_2016['Sport'].value_counts())