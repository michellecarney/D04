#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
import random


# Body

n = random.randrange(1,25)
guess = ''
guesscount = 0

while guesscount < 5:
    try:
        guess = int(input('Guess a number!: '))
        if guesscount < 5:
            if guess == n:
                print('WINNER')
                guesscount = guesscount + 1
                break
            elif guess < n:
                print('too low')
                guesscount = guesscount + 1
                continue
            elif guess > n:
                print('too high')
                guesscount = guesscount + 1
                continue
        else:
            print('the number was' + str(n))
    except:
        print('Please enter a number between 1 and 25')




################################################################################
def main():


    print("Hello World!") # Remove this and replace with your function calls
    

if __name__ == '__main__':
    main()