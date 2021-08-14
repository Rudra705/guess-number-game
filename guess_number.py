print("Welcome to the number guessing game")
print("Guess a number (between 1 and 9)")
import time
num = 6
chances = 5
while chances > 0:
    a = int(input("Enter your guess:- "))
    if not chances > 1:
        print("YOU LOSE !!! The number is " + str(num))
        time.sleep(2)
    if a == num:
        print("Congratulation YOU WON !!!")
        chances = chances - chances
        time.sleep(2)
    elif a > num:
        print("Your guess was too high: Guess a number lesser than " + str(a))
        chances = chances - 1
    elif a < num :
        print("Your guess was too low: Guess a number higher than " + str(a))
        chances = chances - 1