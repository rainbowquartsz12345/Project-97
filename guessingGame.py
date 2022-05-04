import random
number = random.randint(1, 9)
chanceCount = 0
while (chanceCount < 5):
    introString = int(input("Enter a number between 1 and 9: "))
    if (introString > number):
        print("Too BIG. Try again")
    elif (introString == number):
        print("correct! :)")
    else :
        print("too SMALL. Try again")
    chanceCount = chanceCount + 1
if (chanceCount > 5):
    print("You are out of chances")


