"""
Guess the Number
Concept : The computer randomly selects a number within a range, and the player has to guess it.
Key Elements :
Variables: Store the random number and the players guess.
Conditions: Check if the guess is too high, too low, or correct.
Loops: Allow multiple guesses until the correct number is found.
"""

# # for generating random number 
# import random

# number_guess = random.randint(1, 5)

# # print(number_guess)

# while True:
#     user_input = int(input("Enter the number (1 to 4)"))

#     if user_input < number_guess:
#         print("too low, guess again")
#     elif user_input > number_guess:
#         print("too high, guess again")
#     else:
#         print("Guessed right!")
#         break


# for generating random number 
import random

mychoice = ["rock", "paper", "scissor"]
number_guess = random.choice(mychoice)

print(number_guess)

# while True:
#     user_input = int(input("Enter the number (1 to 4)"))

#     if user_input < number_guess:
#         print("too low, guess again")
#     elif user_input > number_guess:
#         print("too high, guess again")
#     else:
#         print("Guessed right!")
#         break