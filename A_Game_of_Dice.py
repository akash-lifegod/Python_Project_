import random

print("Welcome to the Dice Game!")
print("------------------------")

while True:
    input("Press enter to roll the dice!")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("You rolled a", dice1, "and a", dice2)
    print("Your total is", total)
    if total == 7 or total == 11:
        print("Congratulations, you won!")
    elif total == 2 or total == 3 or total == 12:
        print("Sorry, you lost.")
    else:
        while True:
            input("Press enter to roll again!")
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            new_total = dice1 + dice2
            print("You rolled a", dice1, "and a", dice2)
            print("Your new total is", new_total)
            if new_total == 7:
                print("Sorry, you lost.")
                break
            elif new_total == total:
                print("Congratulations, you won!")
                break

    play_again = input("Would you like to play again? (y/n): ")
    if play_again.lower() == "n":
        break

print("Thanks for playing the Dice Game!")