def greatest_number(x,y,z):
    max=x
    if y>max:
        max=y
    if z>max:
        max=z
    return max
    
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)