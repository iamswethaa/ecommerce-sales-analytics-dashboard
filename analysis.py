import pandas as pd

# LOAD DATA

df = pd.read_csv("data/sales.csv", encoding='latin1')

print("✅ Data Loaded Successfully\n")

# INITIAL INSPECTION

print("🔹 First 5 Rows:")
print(df.head(), "\n")

print("🔹 Data Info:")
print(df.info(), "\n")

print("🔹 Columns:")
print(df.columns, "\n")

# CHECK MISSING VALUES

print("🔹 Missing Values:")
print(df.isnull().sum(), "\n")

# HANDLE MISSING VALUES

# Fill Postal Code if missing
if 'Postal Code' in df.columns:
    df['Postal Code'] = df['Postal Code'].fillna(0)

# Drop rows where important values are missing
df = df.dropna(subset=['Sales', 'Profit'])

print("✅ Missing values handled\n")

# REMOVE DUPLICATES

df = df.drop_duplicates()

print("✅ Duplicates removed\n")

# FIX DATA TYPES

# Convert Order Date to datetime
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%y')
print("✅ Data types fixed\n")

# FEATURE ENGINEERING

# Revenue (same as Sales for now)
df['Revenue'] = df['Sales']

# Extract Month & Year
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year

# Profit Margin
df['Profit Margin'] = df['Profit'] / df['Sales']

print("✅ New columns created\n")

# FINAL OUTPUT

print("🔹 Cleaned Data Preview:")
print(df.head())

df.to_csv("data/cleaned_data.csv", index=False)
print("✅ Cleaned data saved to CSV")