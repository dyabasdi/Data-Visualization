import pandas as pd

df = pd.read_csv("1_assignment/pandas_course/olympics_1896_2004.csv", skiprows=5)

init_time = df['Year'].iloc[0]
final_time = df['Year'].iloc[-1]
medals = df['Medal'].unique()
nocs = df['NOC'].unique()

print(f"1) {init_time} - {final_time}")
print(f"2) Due to the world wars during certain years.")
print(f"3) The medal types are {medals}")
print(f"4) {df['Medal'].value_counts()}")
print(f"5) Sometimes, people didn't complete the event.")
print(f"6) Same reason as 5, if only 1 player finished, there will be 1 gold medal and no silver or bronze medals.")
print(f"7) The NOCs are {nocs}")
print(f"8) A mixed team.")
