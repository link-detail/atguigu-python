list1 = [('name', 'rose'), ('age', 12), ('height', 180)]

for e in list1:
    e = tuple(e)
    for i in range(len(e)):
        print(e[i], end= "")
        print(" ", end= " ")
    print()

