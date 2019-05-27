import time
import random


# Prints text, then wait for two seconds
def print_sleep(text):
    print(text)
    time.sleep(0)


def validate_option(options):
    print_sleep("Your options are:")
    # Prints all the option for the player to choose from
    i = 0
    while i < len(options):
        print(f"{i+1}. {options[i]}")
        i += 1
    time.sleep(0)

    # Validates and returns the player choice
    while True:
        selected_option = input("What would you like to do?\n")
        selected_option = int(selected_option)

        if selected_option > 0 and selected_option <= len(options):
            return selected_option
        else:
            print_sleep("That is not a valid option.")


# Describes the setting and start of the game
def intro(items, health, enemies_alive, scene_elements):
    print_sleep("You wake up, in a cell, hearing a moaning.")
    print_sleep("When you turn yourself around...")
    print_sleep("...you see behind your cell gate...")
    print_sleep("...a skeleton!")
    print_sleep("looking right at you.")
    print_sleep("It tries to open the gate, but it is locked.")
    print_sleep("It slowly walks away, as you get to your feet")
    middle_cell(items, health, enemies_alive, scene_elements)


# Elaborates the various scenes
def middle_cell(items, health, enemies_alive, scene_elements):
    print_sleep("You are in your cell")
    options = ["Look around.", "Try to open the gate.", "Check the walls."]

    # If the wall was already broken by the player, let the player go to the next room
    if scene_elements[0] == True:
        options.append("Go through hole.")

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
            adjacent_cell(items, health, enemies_alive, scene_elements)


def adjacent_cell(items, health, enemies_alive, scene_elements):
    print_sleep("You find yourself in the adjacent cell.")
    print_sleep("It looks much the same as your cell.")
    options = ["Open the gate.", "Go back to your cell."]

    while True:
        selected_option = validate_option(options)

        if selected_option == 1:
            print_sleep("This gate is unlocked.")
            print_sleep("You go out of the cell.")
            cell_block(items, health, enemies_alive, scene_elements)
        elif selected_option == 2:
            middle_cell(items, health, enemies_alive, scene_elements)


def cell_block(items, health, enemies_alive, scene_elements):
    print_sleep("You are now in the dungeon corridor.")
    options = ["Look around", "Go to the Jailer Room"]

    while True:
        # If the skeleton has not yet been defeatd, the player can't proceed.
        if enemies_alive[0] == True:
            if "sword" not in items:
                print_sleep(
                    "The skeleton is at the other end of the corridor.")
                print_sleep("It has not yet noticed you.")
                print_sleep("I'd better find a weapon before fighting it.")
            else:
                print_sleep(
                    "The skeleton is at the other end of the corridor.")
                print_sleep("It has not yet noticed you.")
                print_sleep(
                    "Now that you have a sword, you might have a chance.")
                options.append("Fight skeleton.")
        else:
            # Adds the option for the player to continue after defeating the skeleton.
            options.append("Opend the door.")
            options.append("Go through the right passage.")
            options.append("Go through the left passage.")

        selected_option = validate_option(options)

        if selected_option == 1:
            print_sleep("You can see that there are only two cells here.")
            print_sleep("Yours and the one you just came out of.")
            print_sleep("The jailer room is at the end of this corridor.")
            print_sleep("There is a door that leads outside at the other end.")
            print_sleep(
                "And two passages, oposite to the other, beside that door.")
            if enemies_alive[0] == True:
                print_sleep("The skeleton is there.")
                print_sleep("You will have to defeat it.")
                print_sleep("Or you will not be able to go out.")
        if selected_option == 2:
            jailer_room(items, health, enemies_alive, scene_elements)
        if selected_option == 3:
            if enemies_alive[0] == True:
                # If the player defeats the skeleton, updates health
                health = combat(items, health, enemies_alive, scene_elements)
                # Updates the state of this skeleton
                options.remove("Fight skeleton.")
                enemies_alive[0] = False
            else:
                # TODO outside()
                break


def jailer_room(items, health, enemies_alive, scene_elements):
    print_sleep("You are in the jailer room.")
    options = ["Look around.", "Go back"]

    if "sword" not in items:
        print_sleep("His corpse lies on the floor.")
        print_sleep("A sword lay by his side.")
        print_sleep("It is bloody and a little rusty, but it will have to do.")
        options.append("Take the sword.")
    else:
        print_sleep("There is nothing left to do here.")

    while True:
        selected_option = validate_option(options)

        if selected_option == 1:
            print_sleep("The room is dark")
            print_sleep("There is a table, a chair and some other furniture.")
            print_sleep("But there is nothing of use on them.")
            print_sleep("There are bars on the windows.")
        if selected_option == 2:
            cell_block(items, health, enemies_alive, scene_elements)
        if selected_option == 3:
            items.append("sword")
            options.remove("Take the sword.")


# Manages the combat
def combat(items, health, enemies_alive, scene_elements):
    enemy_health = 15
    damage_dealt = 0

    while True:
        if health > 0:
            print_sleep("You attack the skeleton.")
            damage_dealt = random.randint(1, 6)
            enemy_health -= damage_dealt
            print_sleep(f"You have caused {damage_dealt} points of damage.")
            print_sleep(f"It has {enemy_health} health points left.")
        else:
            print_sleep("The skeleton killed you.")
            return

        if enemy_health > 0:
            print_sleep("The skeleton attacks you.")
            damage_dealt = random.randint(1, 6)
            health -= damage_dealt
            print_sleep(f"It has caused {damage_dealt} points of damage.")
            print_sleep(f"You have {health} health points left.")
        else:
            print_sleep("You have defeated the skeleton.")
            return health


# Starts and manages the game
def play_game():
    # Player statistics
    items = []
    health = 100

    # Game Logic
    enemies_alive = [True, True, True, True]  # Are the enemies alive?
    scene_elements = [False, False]  # Is the wall broken? the potion drunk?

    # Start the game
    intro(items, health, enemies_alive, scene_elements)


play_game()
