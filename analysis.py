import pandas as pd

# LOAD DATA

df = pd.read_csv("data/sales.csv", encoding='latin1')

print("Data Loaded Successfully\n")

# ]INITIAL INSPECTION

print("🔹 First 5 Rows:")
print(df.head(), "\n")

print("🔹 Data Info:")
print(df.info(), "\n")

print("🔹 Columns:")
print(df.columns, "\n")

# CHECK MISSING VALUES

print("🔹 Missing Values:")
print(df.isnull().sum(), "\n")

# DATA CLEANING

# Remove duplicates
df = df.drop_duplicates()

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%y')

print("✅ Data cleaned\n")

# FEATURE ENGINEERING

# Revenue
df['Revenue'] = df['Sales']

# Month & Year
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year

# Profit Margin
df['Profit Margin'] = df['Profit'] / df['Sales']

print("✅ New features created\n")

# DATA ANALYSIS

# Total Revenue & Profit
total_revenue = df['Revenue'].sum()
total_profit = df['Profit'].sum()

print("💰 Total Revenue:", total_revenue)
print("📈 Total Profit:", total_profit)

# Top 5 Products
top_products = df.groupby('Product Name')['Revenue'].sum().sort_values(ascending=False).head(5)
print("\n🏆 Top 5 Products:")
print(top_products)

# Top 5 States
state_sales = df.groupby('State')['Revenue'].sum().sort_values(ascending=False).head(5)
print("\n🌎 Top 5 States by Sales:")
print(state_sales)

# Sales by Segment
segment_sales = df.groupby('Segment')['Revenue'].sum()
print("\n👥 Sales by Segment:")
print(segment_sales)

# Monthly Sales
monthly_sales = df.groupby('Month')['Revenue'].sum()
print("\n📆 Monthly Sales:")
print(monthly_sales)

# Discount vs Profit
discount_impact = df.groupby('Discount')['Profit'].mean()
print("\n💸 Discount vs Profit:")
print(discount_impact.head())

# Loss-making products
loss_products = df.groupby('Product Name')['Profit'].sum().sort_values().head(5)
print("\n⚠️ Top 5 Loss-Making Products:")
print(loss_products)

# SAVE CLEANED DATA

df.to_csv("data/cleaned_data.csv", index=False)

print("\nCleaned data saved to CSV")