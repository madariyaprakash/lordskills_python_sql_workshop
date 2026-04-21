employees = {
    "Ravi": 50000,
    "Anita": 65000,
    "Kiran": 45000,
    "Meena": 70000
}

# 1. Increase salary
for name in employees:
    employees[name] *= 1.10

print("Updated Salaries:", employees)

# 2. Highest paid
highest = max(employees, key=employees.get)
print("Highest Paid:", highest)

# 3. Total payroll
total_payroll = sum(employees.values())
print("Total Payroll:", total_payroll)