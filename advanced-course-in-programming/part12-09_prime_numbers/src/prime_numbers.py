# Write your solution here
def prime_numbers():
    number=2
    while True:
        isprime=True
        for i in range(2,number):
            if number%i==0:
                isprime=False
                break
        if isprime:
            yield number
    
        number+=1
