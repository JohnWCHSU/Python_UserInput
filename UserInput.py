# Pythone v3.6

import sys

if len(sys.argv) == 2:
    # python UserInput.py $user_name
    print("Hi!!" + sys.argv[1] + "!")
else:
    # python UserInput.py
    # > what's your name? $user_name
    name = input("what's your name?")
    print("Hi!!" + name + "!")