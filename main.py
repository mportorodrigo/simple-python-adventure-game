import time
import random


# Prints text, then wait for two seconds
def print_sleep(text):
    print(text)
    time.sleep(2)


def validate_option(options):
    # Prints all the option for the player to choose from
    i = 0
    while i < len(options):
        print(f"{i+1}. {options[i]}")
        i += 1

    # Validates and returns the player choice
    while True:
        selected_option = input("What would you like to do?\n")
        selected_option = int(selected_option)

        if selected_option > 0 and selected_option <= len(options):
            return selected_option
        else:
            print_sleep("That is not a valid option.")


# Describes the setting and start of the game
def intro(items, health, options, enemies_alive, scene_elements):
    print_sleep("You wake up, in a cell, hearing a moaning.")
    print_sleep("When you turn yourself around...")
    print_sleep("...you see behind your cell gate...")
    print_sleep("...a skeleton!")
    print_sleep("looking right at you.")
    print_sleep("It tries to open the gate, but it is locked.")
    print_sleep("It slowly walks away, as you get to your feet")
    middle_cell(items, health, options, enemies_alive, scene_elements)


# Elaborates the various scenes
def middle_cell(items, health, options, enemies_alive, scene_elements):
    print_sleep("You are in your cell")
    options.append("Open the gate.")
    # Verifies if the wall was already broken by the player
    if scene_elements[0] == False:
        options.append("Check the walls.")

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
            if scene_elements[0] == False:  # Verifies if the wall is broken
                print_sleep("The wall are old and some bricks seems loose.")
                print_sleep("As you force it, a portion of the wall crumbles.")
                print_sleep("The hole is enough for you to pass through.")
                options.append("Go through hole.")
                scene_elements[0] = True  # Updates the state of the wall
            else:
                print_sleep("The loose bricks fell.")
                print_sleep(
                    "The hole is big enough for a person to go through.")
        elif selected_option == 4:
            # TODO adjacent_cell(items, health, options, enemies_alive, scene_elements)
            break


# Starts and manages the game
def play_game():
    # Player statistics
    items = []
    health = 100

    # Game Logic
    options = ["Look around."]
    enemies_alive = [True, True, True, True]
    scene_elements = [False, False]  # Is the wall broken? the potion drunk?

    # Start the game
    intro(items, health, options, enemies_alive, scene_elements)


play_game()
