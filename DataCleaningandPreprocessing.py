import pandas as pd

data = {'Name': ['Alice', 'Bob', None, 'Charlie', 'Dave'],
'Age': [25, None, 30, None, 45]}
df = pd.DataFrame(data)

# Identify missing data
print("Missing values:\n", df.isnull())

# Count missing values in each column
print("Missing values count:\n", df.isnull().sum())

# Drop rows with any missing values
df_no_missing = df.dropna()
print("DataFrame without missing values:\n", df_no_missing)

# Drop rows with any missing values
df_no_missing = df.dropna()
print("DataFrame without missing values:\n", df_no_missing)

# Fill missing values with the mean of the 'Age' column
df['Age'].fillna(df['Age'].mean(), inplace=True)
print("DataFrame with missing values filled:\n", df)


# Data Normalization and Scaling

from sklearn.preprocessing import MinMaxScaler
# Sample DataFrame
data = {'Score': [200, 300, 400, 500]}
df = pd.DataFrame(data)

# Apply Min-Max scaling
scaler = MinMaxScaler()
df['Score_scaled'] = scaler.fit_transform(df[['Score']])
print("Normalized DataFrame:\n", df)

from sklearn.preprocessing import StandardScaler
# Apply Standard scaling
scaler = StandardScaler()
df['Score_standardized'] = scaler.fit_transform(df[['Score']])
print("Standardized DataFrame:\n", df)

import numpy as np
# Sample DataFrame with skewed data
data = {'Income': [30000, 45000, 60000, 80000, 150000]}
df = pd.DataFrame(data)

# Apply log transformation
df['Income_log'] = np.log(df['Income'])
print("Log-transformed DataFrame:\n", df)

from sklearn.preprocessing import power_transform

# Apply power transformation (Box-Cox)
df['Income_boxcox'] = power_transform(df[['Income']], method='box-cox')
print("Power-transformed DataFrame:\n", df)


data = {'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
'Age': [25, 30, 25, 35, 30]}
df = pd.DataFrame(data)

# Identify duplicates
print("Duplicate Rows:\n", df[df.duplicated()])

# Remove duplicates
df_no_duplicates = df.drop_duplicates()
print("DataFrame without duplicates:\n", df_no_duplicates)



data = {'Name': ['Alice', 'Bob', 'Charlie'],
'Age': ['25', '30', '35']} # Age stored as string
df = pd.DataFrame(data)

# Convert 'Age' to integer
df['Age'] = df['Age'].astype(int)
print("Data types after conversion:\n", df.dtypes)


# Identifying Outliers

from scipy import stats

data = {'Sales': [200, 250, 300, 500, 10000]} # Outlier in Sales
df = pd.DataFrame(data)

# Identify outliers using Z-Score
df['z_score'] = stats.zscore(df['Sales'])
outliers = df[df['z_score'].abs() > 3]
print("Outliers:\n", outliers)

# Checking for Logical Consistency

data = {'Name': ['Alice', 'Bob', 'Charlie'],
'Age': [25, -5, 30]} # Invalid negative age
df = pd.DataFrame(data)

# Identify invalid ages
invalid_ages = df[df['Age'] < 0]
print("Rows with invalid ages:\n", invalid_ages)
