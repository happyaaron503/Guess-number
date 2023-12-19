import random
r = random.randint(1, 10)
while True:
    gus = int(input("Guess a number: "))
    if gus == r:
        print("Ur right!")
        break
    else:
        print("Ur wrong! Keep guessing")