import pandas as pd

df = pd.read_excel("coronaNepal.xlsx")

# PART: 1.1
print(df.head())
print(df.info())
print(df.describe())
print(df.duplicated().sum())
print(df.isnull().sum())

# PART 1.2 Summarize data: total confirmed, deaths, recovered
print(df[['Confirmed Cases', 'Death', 'Recovered']].sum())