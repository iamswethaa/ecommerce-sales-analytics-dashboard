-- TOTAL REVENUE & PROFIT

SELECT 
    SUM(Sales) AS total_revenue,
    SUM(Profit) AS total_profit
FROM sales;

-- TOP 5 PRODUCTS BY REVENUE

SELECT 
    [Product Name],
    SUM(Sales) AS revenue
FROM sales
GROUP BY [Product Name]
ORDER BY revenue DESC
LIMIT 5;

-- SALES BY STATE

SELECT 
    State,
    SUM(Sales) AS total_sales
FROM sales
GROUP BY State
ORDER BY total_sales DESC;

-- SALES BY SEGMENT

SELECT 
    Segment,
    SUM(Sales) AS total_sales
FROM sales
GROUP BY Segment;

-- MONTHLY SALES TREND

SELECT 
    MONTH([Order Date]) AS month,
    SUM(Sales) AS total_sales
FROM sales
GROUP BY month
ORDER BY month;

-- DISCOUNT VS PROFIT

SELECT 
    Discount,
    AVG(Profit) AS avg_profit
FROM sales
GROUP BY Discount
ORDER BY Discount;

-- LOSS-MAKING PRODUCTS

SELECT 
    [Product Name],
    SUM(Profit) AS total_profit
FROM sales
GROUP BY [Product Name]
ORDER BY total_profit ASC
LIMIT 5;