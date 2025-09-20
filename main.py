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

# PART: 1.3 Find top/bottom 5 districts by confirmed cases, deaths, recoveries
# TOP 5 districts by confirmed cases
confirmed_district = df.groupby('District').sum()['Confirmed Cases']
confirmed_district_sorted = confirmed_district.sort_values(ascending=False)
top3_confirmed_district = confirmed_district_sorted.head(5)
print(top3_confirmed_district)

# TOP 5 districts by death
death_district = df.groupby('District').sum()['Death']
death_district_sorted = death_district.sort_values(ascending=False)
top3_death_district = death_district_sorted.head(5)
print(top3_death_district)

# TOP 5 districts by recovery
recovered_district = df.groupby('District').sum()['Recovered']
recovered_district_sorted = recovered_district.sort_values(ascending=False)
top3_recovered_district = recovered_district_sorted.head(5)
# print(top3_recovered_district)

# Bottom 5 districts by recovery
recovered_district = df.groupby('District').sum()['Recovered']
recovered_district_sorted = recovered_district.sort_values(ascending=False)
top3_recovered_district = recovered_district_sorted.tail(5)
print(top3_recovered_district)

# Bottom 5 districts by death
death_district = df.groupby('District').sum()['Death']
death_district_sorted = death_district.sort_values(ascending=False)
top3_death_district = death_district_sorted.tail(5)
print(top3_death_district)

# Bottom 5 districts by confirmed cases
confirmed_district = df.groupby('District').sum()['Confirmed Cases']
confirmed_district_sorted = confirmed_district.sort_values(ascending=False)
top3_confirmed_district = confirmed_district_sorted.tail(5)
print(top3_confirmed_district)

# PART 1.4 Calculate recovery rate and death rate for each district
df['Recovery Rate'] = (df['Recovered'] / df['Confirmed Cases']) * 100
df['Death Rate'] = (df['Death'] / df['Confirmed Cases']) * 100
print(df['Recovery Rate'])
print(df['Death Rate'])
print(df[['District', 'Recovery Rate', 'Death Rate']])

# PART 1.5 Sort districts by severity 
df_sorted_cases = df.sort_values(by='Confirmed Cases', ascending=False)
print(df_sorted_cases[['District', 'Confirmed Cases']].head(10)) 