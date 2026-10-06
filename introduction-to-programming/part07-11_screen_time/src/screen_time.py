from datetime import datetime, timedelta

file_name = input("Filename: ")
start_date = input("Starting date: ")
the_date = datetime.strptime(start_date, "%d.%m.%Y")
amount_days = int(input("How many days: "))
end_date = the_date + timedelta(days=amount_days-1)
data = []
print("Please type in screen time in minutes on each day (TV computer mobile):")
total_minutes = 0

for i in range(amount_days):
    current_date = (the_date + timedelta(days=i)).strftime("%d.%m.%Y")
    screen_time = input(f"Screen time {current_date}: ")
    parts = screen_time.split()
    tv = int(parts[0])
    pc = int(parts[1])
    mob = int(parts[2])
    total_minutes += tv + pc + mob
    data.append((tv, pc, mob))

print(f"Data stored in file {file_name}")

with open(file_name, "w") as myfile:
    myfile.write(
        f"Time period: {the_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}\n")
    myfile.write(f"Total minutes: {total_minutes}\n")
    myfile.write(f"Average minutes: {total_minutes / amount_days}\n")
    for i in range(amount_days):
        current_date = (the_date + timedelta(days=i)).strftime("%d.%m.%Y")
        myfile.write(f"{current_date}: {data[i][0]}/{data[i][1]}/{data[i][2]}\n")