inventory = {
    (101, "Laptop"): 5,
    (102, "Mouse"): 0,
    (103, "Keyboard"): 10
}

# 1. Out of stock
out_of_stock = [product for product, qty in inventory.items() if qty == 0]
print("Out of Stock:", out_of_stock)

# 2. Total stock
total_stock = sum(inventory.values())
print("Total Stock:", total_stock)

# 3. Add new product
inventory[(104, "Monitor")] = 7
print("Updated Inventory:", inventory)