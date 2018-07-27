#list / array
#creat
menu = ["Cơm","Cá","Thịt bò","Rau","Pizza"]
#length
# menu.append("Ghẹ")

# for i in range(len(menu)):
    # print(menu[i])

# for index  , item in enumerate(menu):
#     print("{}. {} ".format(index + 1,item))

# for item in menu:
#     print(item)


#update
print(*menu)
menu[4] = "Bun"
print(*menu, sep=",")

