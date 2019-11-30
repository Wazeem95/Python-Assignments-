import random

random_number = random.randrange(1, 30)

flag = False

for i in range(1, 4):
    guess = int(input("Guess the number between 1 to 30 : "))
    if guess == random_number:
        flag = True
        break
    elif guess < random_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

if flag:
    print("Congratulation you Win!!")
else:
    print("You Loose")
    print("Correct Number is ", random_number)