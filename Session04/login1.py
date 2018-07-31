count = 0
loop = True
while loop:
    
    username = input("Username: ")
    if username == "c4e":
        password = input("Password: ")
        if password == "codethechange":
            print("Welcome: ",username)
            break
        else:
            print("Password is incorrect")
    else:
        print("User not found")
        
    count += 1
    if count == 3:
        print("You failed to log in 3 times, go away")
        loop = False
    
