"""
=========================================
Mini Project 3 - NumPy Sales Analysis
Python Data Analyst Roadmap
=========================================

Project:
Analyze sales data of a retail company using NumPy.

Concepts Used:
--------------
1. Arrays
2. Indexing
3. Boolean Indexing
4. Filtering
5. Aggregation Functions
6. argmax()
7. argmin()
8. Array Operations
9. sort()
10. clip()

Author: Divya Devendrasingh
"""

import numpy as np

print("=" * 50)
print("NUMPY SALES ANALYSIS PROJECT")
print("=" * 50)

# ---------------------------------------
# Dataset
# ---------------------------------------

products = np.array([
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Printer",
    "Speaker",
    "Camera",
    "Headphones"
])

sales = np.array([
    45000,
    38000,
    22000,
    15000,
    5000,
    3500,
    18000,
    9000,
    27000,
    12000
])

# ---------------------------------------
# Display Dataset
# ---------------------------------------

print("\nProducts:")
print(products)

print("\nSales:")
print(sales)

# ---------------------------------------
# Basic Analysis
# ---------------------------------------

print("\n===== Basic Analysis =====")

print("Total Sales      : ₹", np.sum(sales))
print("Average Sales    : ₹", np.mean(sales))
print("Highest Sale     : ₹", np.max(sales))
print("Lowest Sale      : ₹", np.min(sales))

# ---------------------------------------
# Best Selling Product
# ---------------------------------------

best_index = np.argmax(sales)

print("\n===== Best Selling Product =====")
print("Product :", products[best_index])
print("Sales   : ₹", sales[best_index])

# ---------------------------------------
# Lowest Selling Product
# ---------------------------------------

lowest_index = np.argmin(sales)

print("\n===== Lowest Selling Product =====")
print("Product :", products[lowest_index])
print("Sales   : ₹", sales[lowest_index])

# ---------------------------------------
# Products with Sales Above ₹20,000
# ---------------------------------------

print("\n===== Products Above ₹20,000 =====")

print(products[sales > 20000])
print(sales[sales > 20000])

# ---------------------------------------
# Products with Sales Below ₹10,000
# ---------------------------------------

print("\n===== Products Below ₹10,000 =====")

print(products[sales < 10000])
print(sales[sales < 10000])

# ---------------------------------------
# Increase Sales by 10%
# ---------------------------------------

print("\n===== Sales After 10% Increase =====")

increased_sales = sales * 1.10

print(increased_sales)

# ---------------------------------------
# Sort Sales
# ---------------------------------------

print("\n===== Sorted Sales =====")

sorted_sales = np.sort(sales)

print(sorted_sales)

# ---------------------------------------
# Replace Sales Below ₹5,000
# ---------------------------------------

print("\n===== Sales After Applying Minimum Limit =====")

updated_sales = np.clip(sales, 5000, sales.max())

print(updated_sales)

# ---------------------------------------
# Products Above Average Sales
# ---------------------------------------

average_sales = np.mean(sales)

above_average_products = products[sales > average_sales]

# ---------------------------------------
# Business Insights
# ---------------------------------------

print("\n" + "=" * 50)
print("BUSINESS INSIGHTS")
print("=" * 50)

print("Total Revenue          : ₹", np.sum(sales))
print("Average Sales          : ₹", round(np.mean(sales), 2))
print("Best Selling Product   :", products[np.argmax(sales)])
print("Lowest Selling Product :", products[np.argmin(sales)])

print("\nProducts Above Average Sales:")
print(above_average_products)

print("\nRecommendation:")
print("- Increase marketing for low-selling products.")
print("- Maintain inventory for top-selling products.")
print("- Focus promotional offers on medium-performing products.")

print("\nProject Completed Successfully!")