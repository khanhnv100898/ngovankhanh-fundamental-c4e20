items = ["T-Shirt","Sweater"]

select = True

while select:
    select = input("Welcome to your shop, what do you want (C,R,U,D) ?")
    if select == "r":
        print("Items : " )
        for index, item in enumerate(items):
            print(index + 1 , item, sep = ". ")
    elif select == "c":
        print("Items : " )
        for index, item in enumerate(items):
            print(index + 1 , item, sep = ". ")

        pos=(input("New item : "))
        items.append(pos)

        print("Items : ")
        for index, item in enumerate(items):
            print(index + 1 , item, sep = ". ")
    elif select == "u":
        for index , item in enumerate(items):
            print(index + 1, item ,sep = ". ")
            
        pos1 = int(input("Position you want to update ?"))
        while (pos1 - 1) < 0 or (pos1 ) > len(items):
            pos1 = int(input("Position you want to update ?"))

            for index , item in enumerate(items):
                print(index + 1, item ,sep = ". ")
        
        update_item = input("Your replacing item :")
        items[pos1 - 1 ] = update_item

        print("Items : ")
        for index, item in enumerate(items):
            print(index + 1 , item, sep = ". ")
    elif select == "d":
        for index, item in enumerate(items):
            print(index + 1, item , sep = ". ")

        pos2 = int(input("Position you want to delete ?"))
        while (pos2 - 1) < 0 or (pos2) > len(items):
            pos2 = int(input("Position you want to delete ?"))
            for index, item in enumerate(items):
                print(index + 1, item , sep = ". ")
        del items[pos2 - 1]

        print("Items : ")
        for index, item in enumerate(items):
            print(index + 1, item , sep = ". ")
        