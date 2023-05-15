import random

while True:
    guess = random.randint(1,5)
    player =input("guess a number: ")
    try:
        if guess != int(player):
            print(guess)
            continue
    except:
        print("wrong type")
        break
