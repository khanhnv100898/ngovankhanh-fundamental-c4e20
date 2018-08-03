teencode ={
    "hc" : "Học",
    "ng" : "Người",
    "pt" : "Phong trào",
    "eny" : "Em người yêu",
    "any": "Anh người yêu",
    "ns":"nói",
    "ngta":"Người ta",
    "lm": "Làm",
    "r":"Rồi",
    "stt":"Status"
}

loop = True
while loop:
    print("* "*20)
    for key in teencode.keys():
        print(key, end="\t")
    print()
    print("* "*20)

    code = input("Your code ?")
    if code in teencode:
        print("Translation: ", teencode[code])
    else:
        contribute = input("Not found, do you want to contribute this word ? (Y/N) ").upper()
        if contribute == "Y":
            trans = input("Translation: ")
            teencode[code]= trans
            print("Updated")
        else:
            loop = False

