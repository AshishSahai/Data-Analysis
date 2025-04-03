sales_data = {
    "2025-03-25": {"Laptop": 5, "Smartphone": 10, "Tablet": 3},
    "2025-03-26": {"Laptop": 8, "Smartphone": 7, "Tablet": 6},
    "2025-03-27": {"Laptop": 4, "Smartphone": 12, "Tablet": 5}
}
product_totals = {"Laptop": 0, "Smartphone": 0, "Tablet": 0}
daily_sales = {}

for date, product in sales_data.items():
    total_daily_sales = sum(product.values())
    #print(total_daily_sales)
    daily_sales[date] = total_daily_sales

    for products, quantity in product.items():
        #print(products,quantity)
        product_totals[products] += quantity
        #print(product_totals)


best_sale_day = max(daily_sales,key=daily_sales.get)
print(f"Day with highest sale : {best_sale_day}")
print(f"Total sales : {sum(daily_sales.values())}")
for product, total in product_totals.items():

   print(f"Total sale of {product} across all day: {total} ")
