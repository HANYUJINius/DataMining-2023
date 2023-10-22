#3번
def sasp(n):
    s = ("안녕" *(n//2 + 1))[:n]
    return s

print(sasp(4))
print(sasp(5))
