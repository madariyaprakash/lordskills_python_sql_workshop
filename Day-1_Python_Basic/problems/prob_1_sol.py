orders = [
    {"order_id": 101, "customer": "Ravi", "amount": 2500},
    {"order_id": 102, "customer": "Anita", "amount": 5000},
    {"order_id": 103, "customer": "Ravi", "amount": 1500}
]

# 1. Total Revenue
total_revenue = sum(order["amount"] for order in orders)
print("Total Revenue:", total_revenue)

# 2. Amount spent per customer
customer_total = {}

for order in orders:
    name = order["customer"]
    amount = order["amount"]
    
    if name in customer_total:
        customer_total[name] += amount
    else:
        customer_total[name] = amount

print("Customer Totals:", customer_total)

# 3. Highest value order
highest_order = max(orders, key=lambda x: x["amount"])
print("Highest Order:", highest_order)