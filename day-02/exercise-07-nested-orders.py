"Exercise 7: Nested Order Summary"

# Given
orders = {
    "ORD-001": {
        "customer": "Anisha",
        "amount": 2500,
        "status": "Completed"
    },
    "ORD-002": {
        "customer": "Ravi",
        "amount": 1800,
        "status": "Pending"
    },
    "ORD-003": {
        "customer": "Maya",
        "amount": 3200,
        "status": "Completed"
    }
}
print("==========All Orders =============")
# For every order ID and customer
for order_id, info in orders.items():
  print(f"Order: {order_id}, Customer: {info['customer']}")

print("==========Completed Orders =============")
# only for completed orders
for order_id, info in orders.items():
  if info["status"] == "Completed":
    print(f"Order: {order_id}, Amount: NPR {info['amount']}")

# Calculation of the total amount of completed orders and pending
total_completed_amount = 0
pending_count = 0

for order_id, info in orders.items():
  if info["status"] == "Completed":
    total_completed_amount = total_completed_amount + info["amount"]
         
  elif info["status"] == "Pending":
   pending_count = pending_count + 1

# Adding a new order to the dictionary
orders["ORD-004"] = {
        "customer": "Ayush",
        "amount": 1200,
        "status": "Completed"
}

# Output
print(f"Total Amount of Completed Orders: NPR {total_completed_amount}")
print(f"Total Number of Pending Orders: {pending_count}")    
print(f"New Order Added: ORD-004 for {orders['ORD-004']['customer']}")
