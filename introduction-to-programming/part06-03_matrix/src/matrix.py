def read_matrix():
    with open("matrix.txt") as myfile:
        matrix=[]
        for line in myfile:
            parts=line.split(",")
            parts=[int(x) for x in parts]
            matrix.append(parts)
    return matrix
def matrix_sum():
    matrix=read_matrix()
    sumi=0
    for row in matrix:
        sumi+=sum(row)
    return sumi
def matrix_max():
    matrix=read_matrix()
    maxu=-1000
    for row in matrix:
        if maxu<max(row):
            maxu=max(row)
    return maxu
def row_sums():
    matrix=read_matrix()
    sums=[]
    for row in matrix:
        sums.append(sum(row))
    return sums