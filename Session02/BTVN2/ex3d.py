#i
for i in range(1,10):
    for j in range(1,10):
        a = (i+j) % 2
        if a == 0:
            print(1, end = "  ")
        else:
            print(0, end = "  ")
    print()

#ii
n = int(input("Nhap n ? "))
for i in range(1,n+1):
    for j in range(1,n+1):
        a = (i+j) % 2
        if a == 0:
            print(1, end = "  ")
        else:
            print(0, end = "  ")
    print()