print("Guess your number game")
print("Now think of a number (0-100) ")
input()

print("""
All you have to do is to answer to my guess
'c' if my guess is 'C' orrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number
""")

low = 0
high = 100

loop = True

while loop:
    mid=(low + high )//2

    guess = input("Is {} your number : ".format(mid))
    if guess =="c":
        print("Correct")
        loop = False
    elif guess =="s":
        high = mid
    elif guess =="l":
        low = mid
