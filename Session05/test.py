# quy =["Quy", 20, "Vinh Phuc",2, 3,["Anime","ping pong"]]

#dictionary
#CRUD
#key : value

person={
    "Name" : "Quy",
    "Age" : 20,
    "University" : "HUST",
    "Ex": 2,
    "Favs":["Anime","Ping Pong"]
}
person["Gender"]="Male"

# print(person)

# key = "Ex"
# print(person[key])

# if key in person:
#     print(person[key])
# else:
#     print("Not found")


#read:
# for key in person.keys():
#     print(key, end="\t")

# for key, value in person.items():
#     print(key,value)

# for value in person.values():
#     print(value)

#update
person["Ex"] = 20
# print(person)

#delete
del person["Age"]
# print(person)