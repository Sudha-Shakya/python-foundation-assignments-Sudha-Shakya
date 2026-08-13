"Exercise 4: Sales List Analysis"

# Given:
monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

# Sorted list from highest to lowest
sorted_sales = sorted(monthly_sales, reverse=True)

# List containing only values above 100,000
high_sales = [sales for sales in monthly_sales if sales > 100000]

# List where each amount has 13% tax added
tax_sales = [f"{sales * 1.13:.2f}" for sales in monthly_sales]

# Total sales amount
total_sales = sum(monthly_sales)

# Average sales amount
average_sales = total_sales / len(monthly_sales)

# Output
print(f"Sorted Sales (highest to lowest): {sorted_sales}")
print(f"Sales above 100000: {high_sales}")
print(f"Tax sales (13% tax): NPR {tax_sales}") 
print(f"Total sales: NPR {total_sales:.2f}")
print(f"Average sales: NPR {average_sales:.2f}")
