import pandas as pd
import xlsxwriter

df = pd.read_csv("data.csv", index_col=None)

list_ = df.columns
list_ = list(list_)
list_[0] = "Index"
df.columns = list_


df = df.set_index("Index")

team_names = df["team_names"].unique()

# good stuff this works!
for idx, name in enumerate(team_names):
    df.loc[df["team_names"] == name, ("team_names")] = idx
    df.loc[df["opponent_names"] == name, ("opponent_names")] = idx
    