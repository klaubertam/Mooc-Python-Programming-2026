year=int(input("Year: "))
nextyear=year+4-year%4
if nextyear%100==0:
    if nextyear%400==0:
       print(f"The next leap year after {year} is {nextyear}")
    else:
        print(f"The next leap year after {year} is {nextyear+4}")
else:
    print(f"The next leap year after {year} is {nextyear}")