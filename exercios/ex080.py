list = []
x = int(input("digite um valor: "))
list.append(x)
for c in range(0, 4):
    r = int(input("digite um valor: "))
    if r > x:
        list.append(r)
    else:
        list.insert(list.index(x)-1, r)
    x = r
print(list)