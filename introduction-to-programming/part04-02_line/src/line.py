def line(x,char):
    if char=="":
        print("*"*x)
    else:
        print(char[0]*x)
if __name__ == "__main__":
    line(5, "x")