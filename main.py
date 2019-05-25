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
        print(f"{i+1}. {options[i]}")
        i += 1

    # Validate and returns the player choice
    while True:
        selected_option = input("What would you like to do?\n")
        selected_option = int(selected_option)

        if selected_option > 0 and selected_option <= len(options):
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
    middle_cell()


# Elaborates the various scenes
def middle_cell():
    print_sleep("You are in your cell")
    wall_broken = False
    options = ["Look around.", "Open the gate.", "Check the walls."]

    while True:
        selected_option = validate_option(options)

        if selected_option == 1:
            print_sleep("You look around your cell.")
            print_sleep("The bars are rust, but still strong.")
            print_sleep("There is no window.")
            print_sleep("The wall seems very old.")
        elif selected_option == 2:
            print_sleep("It is locked.")
        elif selected_option == 3:
            if wall_broken == False:
                print_sleep("The wall are old and some bricks seems loose.")
                print_sleep("As you force it, a portion of the wall crumbles.")
                print_sleep("The hole is enough for you to pass through.")
                options.append("Go through hole.")
                wall_broken = True
            else:
                print_sleep("The loose bricks fell.")
                print_sleep(
                    "The hole is big enough for a person to go through")
        elif selected_option == 4:
            # TODO adjacent_cell()
            break


def play_game():
    intro()


play_game()
