import random
c=random.randrange(1,101)
H=int(input("gesed the number"))
if c>H:
    print("the number was",c)
    print("your number is less")
elif c<H:
    print("the number was",c)
    print("your number is grater")
else:
    print("the number was",c)
    print("your number is equal")