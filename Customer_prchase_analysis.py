customer_purchases = {
    "Alice": {"Groceries": 120, "Electronics": 300, "Clothing": 150},
    "Bob": {"Groceries": 80, "Electronics": 500, "Clothing": 200},
    "Charlie": {"Groceries": 100, "Electronics": 250, "Clothing": 180}
}
purchases = {}
customer_spending = {}
product_totals = {"Groceries": 0, "Electronics": 0, "Clothing": 0}
category = {}
for name, products in customer_purchases.items():
    total_spending = sum(products.values())
    customer_spending[name] = total_spending

    print(f"Total spending of {name}: {total_spending}")
    for product, quantity in products.items():
        #print(product)
        product_totals[product]+= quantity


highest_customer_spending = max(customer_spending, key=customer_spending.get)
print(f"Highest Customer Spending : {highest_customer_spending}")
#print(product_totals)
highest_total_sales = max(product_totals, key=product_totals.get)
print(f"Category with the highest total sales: {highest_total_sales}" )
