# Number Guessing Game
# importing the Random Module
import random
# Asking to start the GAME LOOP
print("Would you like to play the Number Guess Game?")
is_playing = input("Y/N: ").upper()

# Checking to see if the game loop was initiated
if is_playing == "Y":
    # Asking the user for the game range
    user_random_limit = input("Pick a number I can't go past: ")
    # Setting a random number to a variable using the users game perameters
    ran_num = random.randint(1, int(user_random_limit))

    # loop to check for guesses
    correct_num = False
    guess_num = 0
    while correct_num == False:
        user_guess = input("Try to guess my number, 1 through " + user_random_limit + ": ")
        guess_num += 1

        # Comparison loop to check if the answer was correct
        if int(user_guess) > ran_num:
            print(f"Your guess of {int(user_guess)} was to high")
        elif int(user_guess) < ran_num:
            print(f"Your guess of {int(user_guess)} was to low")
        else:
            print("You got it correct!!!")
            correct_num = True
    print(f"It took you {guess_num} tries...")
else:
    quit()