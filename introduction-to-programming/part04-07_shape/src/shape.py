def line(x,char):
    if char=="":
        print("*"*x)
    else:
        print(char[0]*x)

def triangle(size, character):
    i=1
    while i<=size:
        line(i, character)
        i=i+1

def rectangle(row,column,char):
   while row>0:
    line(column, char)
    row-=1

def shape(size, char1, size2, char2):
    triangle(size, char1)
    rectangle(size2, size, char2)


if __name__ == "__main__":
    shape(5, "x", 2, "o")