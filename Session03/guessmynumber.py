from random import randint
rand_numb = randint(0,100)

print(rand_numb)

playing = True
count = 0

while playing  :
    guess = int(input("Doan so ? (1-100) "))

    if guess > rand_numb :
        print("A little too large")
    elif guess < rand_numb:
        print("Too small")
    else:
        print("Bingo")
        # playing = False
        break
    count += 1
    if count == 7:
        print("You lose")
        playing = False

    