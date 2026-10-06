def line(x,char):
    if char=="":
        print("*"*x)
    else:
        print(char[0]*x)
def square(size, character):
    i=0
    while i<size:
        line(size, character)
        i+=1

if __name__ == "__main__":
    square(5, "x")