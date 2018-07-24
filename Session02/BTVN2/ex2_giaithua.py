n = int(input(" Nhap n ? "))

total = 1

for i in range(n):
    total *= (i+1)

print("Giai thua cua:",n, "=" , total )