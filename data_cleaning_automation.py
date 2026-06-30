import pandas as pd

df = pd.read_excel('Sample_Data_Cleaning.xlsx', sheet_name='Raw_Data')
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
df['Name'] = df['Name'].str.strip()
df['City'] = df['City'].str.title()
df = df.drop_duplicates()
summary = df.groupby('City')['Sales'].sum()
print(summary)
df.to_excel('Cleaned_Output.xlsx', index=False)
