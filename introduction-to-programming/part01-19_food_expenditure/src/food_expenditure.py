cafeteria_visits = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
weekly_groceries = float(input("How much money do you spend on groceries in a week? "))
weekly_total = weekly_groceries + lunch_price * cafeteria_visits
daily_average = weekly_total / 7
print("Average food expenditure:")
print(f"Daily: {daily_average} euros")
print(f"Weekly: {weekly_total} euros")
