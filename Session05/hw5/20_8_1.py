import string

alphab = list(string.ascii_lowercase)
# print(alphab)

name  =list(input("Nhap chuoi ki tu ? ").lower() )


for i in alphab:
    count = 0
    for k in name:
        if i == k:
            count += 1
    if i not in name:
        continue
    print("{}     {}".format(i,count) )

