from random import randint

mood = randint(0, 100)
if mood < 30 :
    print("I feeling sad")
elif mood < 60:
    print("I feeling OK")
else :
    print("I feeling Happy")