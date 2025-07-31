import random

x=random.randint(1,101)

y=int(input("guess a number between 1 and 100:"))

while y!=x:
    if int(y)>int(x):
        print("too high")
        y=int(input("try again:"))
    elif int(y)<int(x):
        print("too low")
        y=int(input("try again:"))
else:
    print("you won!")