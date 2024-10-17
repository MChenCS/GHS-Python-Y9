"""
Retail Store
"""

customer_groups = {
    "A": ["Management", 0.3],
    "B": ["Staff", 0.2],
    "C": ["Account", 0.08],
    "D": ["Cash", 0.05],
    "E": ["Card", 0]

}

basket_total = float(input("What's the basket total? "))
customer_code = input("What's the customer's identification code? ")
discount_rate = customer_groups.get(customer_code)[1]

payable = basket_total * (1 - discount_rate)

print(payable)