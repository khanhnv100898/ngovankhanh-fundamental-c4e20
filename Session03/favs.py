favs = ["death note","netflix","teaching"]
print("Hi there ....")
print(*favs, sep=",")

new_fav = input("Nhap them ")

favs.append(new_fav)
print(*favs, sep=",")
