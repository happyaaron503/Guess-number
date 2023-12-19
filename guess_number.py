import random
r = random.randint(1, 10)
count = 0
while True:
    gus = int(input("Guess a number: "))
    count += 1
    if gus == r:
        print("Ur right!")
        print("猜了", count, "次")
        break
    else:
        print("Ur wrong! Keep guessing")
        print("猜了", count, "次")
        if r > gus:
            print("Too small")
        elif r < gus:
            print("Too big")