import pandas as pd
import matplotlib.pyplot as plt
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
df = pd.DataFrame(list(sales_data.items()), columns=["Day","Sales"])
print("\nWeekly Sales data")
print(df)

plt.figure(figsize=(10,5))
plt.bar(df["Day"], df["Sales"], color="skyblue")


plt.xlabel("Days of the week")
plt.ylabel("Sales in Dollars")
plt.title("Weekly Sales Performance")
plt.xticks(rotation=45)
plt.show()
