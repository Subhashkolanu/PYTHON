import random
secret = random.randint(1,100)
for i in range(10):
    guess = int(input("Enter value : "))
    if guess == secret:
        print("Congrats!")
    elif guess>secret:
        print("Too much ahead")
    elif guess<secret:
        print("Too much away")
else:
    print("Better luck again!. it was ",secret)