username = input("Usernam: ")

if username != "c4e":
    print ("You're not a superuser")
else:
    password = input("Password: ")
    if password != "codethechange":
        print("Incorrect password")
    else:
        print("Welcome")

