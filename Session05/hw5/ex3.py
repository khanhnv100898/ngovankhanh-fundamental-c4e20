bacterias = int(input("How many B bacterias are there? "))
minutes = int(input("How much time in minutes will we wait?"))


# count = 0

if minutes % 2== 0:
    for i in range(2,minutes + 1):
        if i % 2 == 0:
           bacterias *= 2  
        else:
            continue
    print("After {} minutes, we would have {} bacterias".format(minutes,bacterias))
else:
    for i in range(2,minutes):
        if i % 2 == 0:
           bacterias *= 2  
        else:
            continue
    print("After {} minutes, we would have {} bacterias".format(minutes,bacterias))