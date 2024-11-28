import pandas as pd

df = pd.read_csv('dz.csv')
print(df)

df.fillna(0, inplace=True)
print(df)

df.drop(7, axis=0, inplace=True)
print(df)

salary_average = df.groupby('City')['Salary'].mean()
print(salary_average)