region_sales = {
    "North": {"Q1": 15000, "Q2": 18000, "Q3": 22000, "Q4": 25000},
    "South": {"Q1": 17000, "Q2": 19000, "Q3": 21000, "Q4": 23000},
    "East": {"Q1": 20000, "Q2": 22000, "Q3": 25000, "Q4": 27000}
}
total_region_sales = {}
quarterly_sales = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
for region, quarters in region_sales.items():
    total_region_sales[region] = sum(quarters.values())
    for quarter, sales in quarters.items():
        quarterly_sales[quarter] += sales


    #print(f"Total annual sales for {region} : {sum(quarter.values())}")
#print(total_region_sales)

print("Total annual sales per region: \n")
for region, total in total_region_sales.items():
    print(f"{region} : ${total}")

print(f"\nBest performing region: {max(total_region_sales, key=total_region_sales.get)}")
print(f"Worst performing region: {min(total_region_sales, key=total_region_sales.get)}\n")
for quarter, sales in quarterly_sales.items():
    print(f"{quarter}: {sales}")
print(f"\nBest Quarter: {max(quarterly_sales, key=quarterly_sales.get)}")
print(f"Worst Quarter: {min(quarterly_sales,key=quarterly_sales.get)}")
#print(total_region_sales)
#print(quarterly_sales)

