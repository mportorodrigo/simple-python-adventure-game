import time
import random


# Prints text, then wait for two seconds
def print_sleep(text):
    print(text)
    time.sleep(2)


def validate_option(options):
    # Print all the option for the player to choose from
    i = 0
    while i < len(options):
        print(f"{i}. {options[i]}")
        i += 1

    # Verify and returns the player choice
    while True:
        selected_option = input("What would you like to do?\n")
        selected_option = int(selected_option)

        if selected_option > 0 and selected_option < len(options) + 1:
            return selected_option
        else:
            print_sleep("That is not a valid option.")


# Describes the setting and start of the game
def intro():
    print_sleep("You wake up, in a cell, hearing a moaning.")
    print_sleep("When you turn yourself around...")
    print_sleep("...you see behind your cell gate...")
    print_sleep("...a skeleton!")
    print_sleep("looking right at you.")
    print_sleep("It tries to open the gate, but it is locked.")
    print_sleep("It slowly walks away, as you get to your feet")


def play_game():
    intro()


play_game()
