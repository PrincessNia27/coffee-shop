"""
Program: Coffee Shop.py
8/31/2026
Simple command-line ordering system for a coffee shop. The program asks the customer their name, what items they want and calculates then displays the total.

""" 
# Variables
COFFEE_PRICE = 4.50
PASTRY_PRICE = 3.00

# Input Phase
customer_name = input("Please enter your name!;) >>")

coffee_quantity = int(input("How many cups of coffee would you like? >>"))

pastry_quantity = int(input("How many pastries would you like? >>"))

# Processing Phase
coffee_total = coffee_quantity * COFFEE_PRICE

pastry_total = pastry_quantity * PASTRY_PRICE

final_total = coffee_total + pastry_total

# Output Phase
print(customer_name, "your total is $", format(final_total, ".2f"))