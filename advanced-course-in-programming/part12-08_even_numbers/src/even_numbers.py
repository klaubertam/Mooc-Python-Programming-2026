# Write your solution here
def even_numbers(beginning: int, maximum: int):
    if beginning%2==0:
        number=beginning
    else:
        number=beginning+1
    while number<=maximum:
        yield number
        number+=2