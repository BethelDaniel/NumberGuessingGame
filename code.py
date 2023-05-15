import random

while True:
    guess = random.randint(1,5)
    player = input("guess a number: ")
    if TypeError or ValueError:
        print("please try again")
        break
    if guess != int(player):
        print(guess)
        continue
    else:
        break
