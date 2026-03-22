import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder if not exists
os.makedirs("charts", exist_ok=True)

# LOAD DATA

df = pd.read_csv("data/sales.csv", encoding='latin1')

print("✅ Data Loaded Successfully\n")

# CLEANING

df = df.drop_duplicates()
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%y')

# FEATURE ENGINEERING

df['Revenue'] = df['Sales']
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year
df['Profit Margin'] = df['Profit'] / df['Sales']

print("✅ Data prepared\n")

# ANALYSIS

total_revenue = df['Revenue'].sum()
total_profit = df['Profit'].sum()

print("💰 Total Revenue:", total_revenue)
print("📈 Total Profit:", total_profit)

top_products = df.groupby('Product Name')['Revenue'].sum().sort_values(ascending=False).head(5)
state_sales = df.groupby('State')['Revenue'].sum().sort_values(ascending=False).head(5)
segment_sales = df.groupby('Segment')['Revenue'].sum()
monthly_sales = df.groupby('Month')['Revenue'].sum()

# VISUALIZATION (SAVE THE CHARTS)

# Monthly Sales Trend
plt.figure()
monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.savefig("charts/monthly_sales.png")
plt.close()

# Top Products
plt.figure()
top_products.plot(kind='bar')
plt.title("Top 5 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.savefig("charts/top_products.png")
plt.close()

# Top States
plt.figure()
state_sales.plot(kind='bar')
plt.title("Top States by Sales")
plt.xlabel("State")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.savefig("charts/top_states.png")
plt.close()

# Segment Distribution
plt.figure()
segment_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales by Segment")
plt.ylabel("")
plt.savefig("charts/segment_sales.png")
plt.close()

# Discount vs Profit
plt.figure()
plt.scatter(df['Discount'], df['Profit'])
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.savefig("charts/discount_vs_profit.png")
plt.close()

print("\n📊 Charts saved in 'charts/' folder")

# SAVE CLEANED DATA

df.to_csv("data/cleaned_data.csv", index=False)

print("✅ Cleaned data saved")