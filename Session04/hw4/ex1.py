name = input("Your full name ? ")
# name = "NGo VaN    KhAnh"

name_lower = name.lower()
name_split = name_lower.split()

# print(name_split)
# print(name_lower)
# name_list = list(name_lower)
# print(*name_list)
name_update =[]
for i in name_split:
    # print(i)
    # print(name_list[i])
    name_update.append(i.title())
print("Updated: ",*name_update)

