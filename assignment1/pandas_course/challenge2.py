import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def preprocess(filename = "1_assignment/pandas_course/olympics_1896_2004.csv"):
  """Preparing and transforming dataframe"""
  print(f"Preprocessing {filename} ...\n")
  ordered_medals = pd.api.types.CategoricalDtype(categories=["Bronze", "Silver", "Gold"], ordered=True)
  dtype_mapper = {"Year": "int64",
                "City": "string",
                "Sport": "string",
                "Discipline": "string",
                "Athlete Name": "string",
                "NOC": "string",
                "Gender": "category",
                "Event": "string",
                "Event_gender": "category",
                "Medal": ordered_medals}
  df = (pd.read_csv(filename, skiprows=5, dtype=dtype_mapper)
        .drop('Position', axis=1)
  )
  df["Event Gender"] = df["Event Gender"].astype("category")
  df.loc[24676, "Gender"] = "Women"
  df.Sport = df.Sport.str.lower()
  df.Discipline = df.Discipline.str.lower()
  df.Event = df.Event.str.lower()
  df.NOC = df.NOC.str.upper()
  return df


def preprocess_2008(filename="1_assignment/pandas_course/olympics_2008.csv"):
  print(f"Preprocessing {filename} ...\n")
  df = pd.read_csv(filename)
  df.columns = ['City', 'Year', 'Sport', 'Discipline', 'Athlete Name', 'NOC',
       'Gender', 'Event', 'Event Gender', 'Medal', 'Result']
  df = df.drop("Result", axis=1)
  df.City = df.City.fillna(value="Beijing")
  df.Year = df.Year.fillna(value=2008)
  df = df.dropna(subset=['Sport', 'Discipline', 'Athlete Name', 'NOC', 'Gender',
       'Event', 'Event Gender', 'Medal'], how="all")
  df = df.drop_duplicates()
  df.Sport = df.Sport.str.lower()
  df.Discipline = df.Discipline.str.lower()
  df.Event = df.Event.str.lower()
  df.NOC = df.NOC.str.upper()
  df.Medal = df.Medal.str.capitalize()
  df.City = df.City.astype("string")
  df.Year = df.Year.astype(int)
  df.Sport = df.Sport.astype("string")
  df.Discipline = df.Discipline.astype("string")
  df["Athlete Name"] = df["Athlete Name"].astype("string")
  df.NOC = df.NOC.astype("string")
  df.Gender = df.Gender.astype("category")
  df.Event = df.Event.astype("string")
  df['Event Gender'] = df['Event Gender'].astype("category")
  medal_order = ["Bronze", "Silver", "Gold"]
  df.Medal = pd.Categorical(df.Medal, categories=medal_order, ordered=True)

  return df

oo = preprocess()
nw = preprocess_2008()
up = pd.concat([oo, nw])
up.sample(3)

usa_data = up[up['NOC'] == 'USA']
usa_data['mens_gold'] = np.where((usa_data['Gender'] == 'Men') & (usa_data['Medal'] == 'Gold'), 1, 0)
usa_data['womens_gold'] = np.where((usa_data['Gender'] == 'Women') & (usa_data['Medal'] == 'Gold'), 1, 0)
usa_data['mens_gold_cumsum'] = usa_data['mens_gold'].cumsum()
usa_data['womens_gold_cumsum'] = usa_data['womens_gold'].cumsum()
usa_data = usa_data.drop_duplicates('Year', keep='last')

# Count the number of each medal type for each athlete
medal_count = up.groupby(['Athlete Name', 'Medal']).size().unstack(fill_value=0)

# Sort by Gold first, then Silver, then Bronze
medal_count = medal_count.sort_values(by=['Gold', 'Silver', 'Bronze'], ascending=False)

# Get the top 5 athletes
top_5_athletes = medal_count.head(5)


fig, axes = plt.subplots(2, 1, figsize=(10, 12))

axes[0].set_title("USA Olympic Gold Medals")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Number of Gold Medals")
axes[0].plot(usa_data['Year'], usa_data['mens_gold_cumsum'], label="Men's Gold Medals", color='blue')
axes[0].plot(usa_data['Year'], usa_data['womens_gold_cumsum'], label="Women's Gold Medals", color='pink')
axes[0].legend()

top_5_athletes[['Gold', 'Silver', 'Bronze']].plot(kind='bar', stacked=True, ax=axes[1], color=['gold', 'silver', 'darkgoldenrod'])
axes[1].set_title("Top 5 Athletes with the Most Gold Medals")
axes[1].set_xlabel('Athlete Name')
axes[1].set_ylabel('Number of Medals')

plt.tight_layout()
plt.show()


