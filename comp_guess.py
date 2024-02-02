import random

print("Would you like to play?")
is_playing = input("Y/N: ").upper()

if is_playing == "Y":
    print("Awsome, choose a number for me to guess")
    top_of_range = input("Choose a number you cant go over: ")
    print(f"Ok, hold a number in your head between 1 and {top_of_range} and I'll start guessing")
    correct_num = False
    guess_count = 0
    min_of_range = 1

    ran_num = random.randint(min_of_range, int(top_of_range))
    print(ran_num) #TODO Take out

    while correct_num == False:
        guess_count +=1
        print(f"IS YOUR NUMBER {ran_num}?!?!?!?!")
        user_input = input("Y/N: ").upper()
        if user_input == "N":
            print(f"Was {ran_num} too High or Low?!?!")
            hL_input = input("H/L: ").upper()

            if hL_input == "H":
                top_of_range = ran_num
                ran_num = random.randint(min_of_range, int(top_of_range))
            elif hL_input == "L":
                min_of_range = ran_num
                ran_num = random.randint(min_of_range, int(top_of_range))
            else:
                print("Incorrect input, you broke me!!!")
                quit()
        else:
            correct_num = True
else:
    quit()