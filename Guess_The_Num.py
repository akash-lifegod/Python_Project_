import random
a=random.randrange(1,10)
while a:
    b=int(input("Guess The Number..."))
    if a==b:
        print("Hurray!!! You Won :)")
        break
    else:
        print("Wrong Guess :(")
        print("Try Again...!")
