"""
Scenario: Inventory Tracking (TUPLE + DICTIONARY)
==============================================

Scenario
- Each product has fixed Product ID and Name (cannot change → tuple).
- Stock quantity changes over time.

inventory = {
    (101, "Laptop"): 5,
    (102, "Mouse"): 0,
    (103, "Keyboard"): 10
}

Tasks:

- Find out-of-stock items.
- Calculate total stock.
- Add new product.
"""