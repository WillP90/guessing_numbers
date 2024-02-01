import random

print("Would you like to play?")
is_playing = input("Y/N: ").upper()

if is_playing == "Y":
    print("Awsome, choose a number for me to guess")
    top_of_range = input("Choose a number you cant go over: ")
    print(f"Ok, hold a number in your head between 1 and {top_of_range} and I'll start guessing")
    correct_num = False
    guess_count = 0

    ran_num = random.randint(1, int(top_of_range))
    print(ran_num)

else:
    quit()