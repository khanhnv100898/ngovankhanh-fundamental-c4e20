from random import choice

words = ["champion","dungeon","vodka"]

word =choice(words)
chars = list(word)
update_chars =[]

loop = True

while loop:
    rand_char = choice(chars)
    update_chars.append(rand_char)
    chars.remove(rand_char)
    if len(chars) == 0:
        loop = False

print(update_chars)

ans = input("Your guess: ")
if ans == word:
    print("Huraa")
else:
    print(":(((")



