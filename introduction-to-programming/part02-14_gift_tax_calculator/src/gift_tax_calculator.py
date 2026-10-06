value = int(input("Value of gift: "))

if value < 5000:
    print("No tax!")
else:
    if value < 25000:
        TALL = 100
        percentile = 0.08
        change = value - 5000
    elif value < 55000:
        TALL = 1700
        percentile = 0.1
        change = value - 25000
    elif value < 200000:
        TALL = 4700
        percentile = 0.12
        change = value - 55000
    elif value < 1000000:
        TALL = 22100
        percentile = 0.15
        change = value - 200000
    else:
        TALL = 142100
        percentile = 0.17
        change = value - 1000000

    finallythetax = float(TALL + change * percentile)
    print(f"Amount of tax: {finallythetax} euros")