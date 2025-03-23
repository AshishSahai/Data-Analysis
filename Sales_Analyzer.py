sales_data = {}
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days:
        while True:
           try:
                sale = int(input(f"Enter sales for {day} : "))
                sales_data[day] = sale
                break
           except ValueError:
                print("Invalid input! Please enter a valid number")


        #print(Sales_data.values())
sales_value = sales_data.values()
sum_sale_data = sum(sales_value)
average_sale_data = round(sum_sale_data/len(sales_value),2)
best_sales_day = max(sales_value)
best_day = max(sales_data, key=sales_data.get)
lowest_day = min(sales_data, key=sales_data.get)
lowest_sales_day = min(sales_value)
print(f"Total Sales : ${sum_sale_data}")
print(f"Average Daily Sales : ${average_sale_data}")
print(f"Best Sales Day : {best_day} (${best_sales_day})")
print(f"Lowest Sales Day : {lowest_day} (${lowest_sales_day})")
