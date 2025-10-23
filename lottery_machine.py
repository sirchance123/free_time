import random
import sys
import time

accept = input("Do you want to play the lottery? Answer Yes or No : ").strip()
accept_real = accept.capitalize()
print(accept_real)

if accept_real != "Yes":
    print("You're a bum")
    sys.exit(0)

mode = input("Do you want...Easy...Normal...or Hard mode? : ").strip()
mode_real = mode.capitalize()
print(mode_real)

if mode_real == "Easy":
    print("You will now roll a number between 1 and 10. If you get a seven, you survive another round")
    number = random.randint(1, 10)
    print("Rolling...")
    time.sleep(2)
    if number == 7:
        print("You rolled a 7. You live...for now.")
    else:
        print("You rolled a", number, ". You DIE.")
elif mode_real == "Normal":
    print("You will now roll a number between 1 and 100. If you get a 77, you survive another round")
    number2 = random.randint(1, 100)
    print("Rolling...")
    time.sleep(2)
    if number2 == 77:
        print("You rolled a 77. You got lucky...unfortunately.")
    else:
        print("You rolled a", number2, ". You DIE x10!")
elif mode_real == "Hard":
    print("Hard mode: roll between 1 and 1000. If you get 777, you survive.")
    number3 = random.randint(1, 1000)
    print("Rolling...")
    time.sleep(2)
    if number3 == 777:
        print("You rolled a 777. Miraculous survival.")
    else:
        print("You rolled a", number3, ". You DIE horribly.")
else:
    print("Invalid mode. Exiting.")

