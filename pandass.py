# pip install pandas

import pandas as pd

#series
s = pd.Series([10, 20, 30])
print(s)

#Dataframe
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)
print(df)


#Read and write files
df = pd.read_csv('data.csv')
df.to_csv('output.csv', index=False)

# Excel
df = pd.read_excel('data.xlsx')
df.to_excel('output.xlsx', index=False)

#View and explore data
df.head()        # First 5 rows
df.tail()        # Last 5 rows
df.shape         # Rows, Columns
df.info()        # Summary
df.describe()    # Stats
df.columns       # Column names

#Data selection
df['Name']              # Single column
df[['Name', 'Age']]     # Multiple columns
df.iloc[0]              # First row (by index)
df.loc[0, 'Name']       # Specific value

#Filtering Rows
df[df['Age'] > 25]                 # Age > 25
df[(df['Age'] > 25) & (df['Age'] < 35)]  # Age between

#Adding/Modifying columns
df['Salary'] = [50000, 60000, 70000]    # New column
df['Age in 5 Years'] = df['Age'] + 5    # Derived column

#Sorting and Grouping
df.sort_values(by='Age', ascending=False)

df.groupby('Name')['Age'].mean()

#Handling missing data
df.isnull()            # Check for NaN
df.dropna()            # Drop rows with NaN
df.fillna(0)           # Replace NaN with 0

#Merge or join DF
# pd.merge(df1, df2, on='id')        # SQL-like joins
# pd.concat([df1, df2], axis=0)      # Stack vertically
# pd.concat([df1, df2], axis=1)      # Combine side by side



#Load and clean CSV/Excel data

# Analyze sales data, user logs, stock prices

# Prepare datasets for machine learning

# Generate statistical reports

