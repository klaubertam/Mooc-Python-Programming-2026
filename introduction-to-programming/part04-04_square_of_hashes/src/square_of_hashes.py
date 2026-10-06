def line(x,char):
    if char=="":
        print("*"*x)
    else:
        print(char[0]*x)
def square_of_hashes(size):
    i=0
    while i<size:
        line(size, "#")
        i+=1
if __name__ == "__main__":
    square_of_hashes(5)
