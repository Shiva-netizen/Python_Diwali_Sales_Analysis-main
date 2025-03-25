import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt  # visualizing data
import seaborn as sns

# Import CSV file
df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')
print(df.shape)
print(df.head())
print(df.info())

# Drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

# Check for null values
print(pd.isnull(df).sum())

# Drop null values
df.dropna(inplace=True)

# Change data type
df['Amount'] = df['Amount'].astype(int)
print(df['Amount'].dtypes)
print(df.columns)

# Rename column
df.rename(columns={'Marital_Status': 'Shaadi'}, inplace=True)

# Describe dataset
print(df.describe())
print(df[['Age', 'Orders', 'Amount']].describe())

# Plot bar chart for Gender count
plt.figure(figsize=(6, 4))
ax = sns.countplot(x='Gender', data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Gender vs Total Amount
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(6, 4))
sns.barplot(x='Gender', y='Amount', data=sales_gen)
plt.show()

# Age Group vs Gender count
plt.figure(figsize=(8, 5))
ax = sns.countplot(data=df, x='Age Group', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(8, 5))
sns.barplot(x='Age Group', y='Amount', data=sales_age)
plt.show()

# Top 10 states by number of orders
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
plt.figure(figsize=(15, 5))
sns.barplot(data=sales_state, x='State', y='Orders')
plt.show()

# Top 10 states by total sales
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
plt.figure(figsize=(15, 5))
sns.barplot(data=sales_state, x='State', y='Amount')
plt.show()

# Marital Status count
plt.figure(figsize=(7, 5))
ax = sns.countplot(data=df, x='Marital_Status')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Marital Status vs Gender vs Amount
sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(6, 5))
sns.barplot(data=sales_state, x='Marital_Status', y='Amount', hue='Gender')
plt.show()

# Occupation count
plt.figure(figsize=(20, 5))
ax = sns.countplot(data=df, x='Occupation')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Occupation vs Amount
sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
plt.figure(figsize=(20, 5))
sns.barplot(data=sales_state, x='Occupation', y='Amount')
plt.show()

# Product Category count
plt.figure(figsize=(20, 5))
ax = sns.countplot(data=df, x='Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Top 10 Product Categories by Amount
sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
plt.figure(figsize=(20, 5))
sns.barplot(data=sales_state, x='Product_Category', y='Amount')
plt.show()

# Top 10 Products by Orders
sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
plt.figure(figsize=(20, 5))
sns.barplot(data=sales_state, x='Product_ID', y='Orders')
plt.show()

# Top 10 most sold products
plt.figure(figsize=(12, 7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
plt.show()
