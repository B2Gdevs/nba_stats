import pandas as pd
import nba_methods

df = pd.read_csv('data.csv')

print(df.columns)
unique_quarters = df['quarters'].unique()

print(unique_quarters)
nba_methods.save_binary('quarters.pkl', unique_quarters)
