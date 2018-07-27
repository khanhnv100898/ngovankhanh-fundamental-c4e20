favs=["death note","netflix","teaching"]
print("Hi there, here you favorite things so far : ")

# for index  , fav in enumerate(menu):
#     print("{}. {} ".format(index + 1,fav))

print("* " *20)
for index  , fav  in enumerate(favs):
    print(index +1 , fav,sep = ". ")
print("* " *20)

pos = int(input("Position you want to update ? "))
update_fav = input("Your replacing fav : ")
favs[pos - 1] = update_fav

print("* " *20)
for index  , fav in enumerate(favs):
    print("{}. {} ".format(index + 1,fav))
print("* " *20)







