# Write your solution here
# Remember the import statement
# from datetime import date
def list_years(dates: list):
    list_of_years=[]
    for element in dates:
        yearz=element.year
        list_of_years.append(yearz)
    return sorted(list_of_years)