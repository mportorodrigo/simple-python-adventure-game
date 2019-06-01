import time
import random


def print_sleep(text):
    """Print a message, then wait two seconds"""
    print(text)
    time.sleep(2)


def validate_option(options):
    """
    Print options and validate answer.

    Parameters:
        options (list): A list with avaiable options.

    Returns:
        selected_option (int): Number representing chosen option.
    """

    print_sleep("What would you like to do?")

    i = 0
    while i < len(options):
        print(f"{i+1}. {options[i]}")
        i += 1

    while True:
        selected_option = input(f"Type a number from 1 to {i}\n")

        try:
            selected_option = int(selected_option)

            if selected_option > 0 and selected_option <= len(options):
                return selected_option
            else:
                print_sleep("That is not a valid option.")
        except ValueError:
            print_sleep("That is not a number.")


def intro(items, health, enemies_alive, scene_elements):
    """
    Display introductory text for the game, takes on several parameters
    and pass them as parameters for other functions, updating the state
    and progress of the game.

    Parameters:
        items (list): Store player items.
        health (int): Store player health points.
        enemies_alive (list): Store the current state of enemies.
        scene_elements (list): Store interaction state of scene elements.
    """

    print_sleep("You wake up, in a cell, hearing a moaning.")
    print_sleep("When you turn yourself around...")
    print_sleep("...you see behind your cell gate...")
    print_sleep("...a skeleton!")
    print_sleep("looking right at you.")
    print_sleep("It tries to open the gate, but it is locked.")
    print_sleep("It slowly walks away, as you get to your feet.")
    player_cell(items, health, enemies_alive, scene_elements)


# The following function serve as scenes for the game

def player_cell(items, health, enemies_alive, scene_elements):
    """Describes the ocurrencies in the player cell scene."""

    print_sleep("You are in your cell.")
    options = ["Look around.", "Try to open the gate.", "Check the walls."]

    # If the player already broke the wall, let him through
    if scene_elements[0] is True:
        options.append("Go through hole.")

    while True:
        selected_option = validate_option(options)

        if selected_option == 1:
            print_sleep("You look around your cell.")
            print_sleep("The bars are rust, but still strong.")
            print_sleep("There are no windows.")
            print_sleep("The walls seem to be very old.")
        elif selected_option == 2:
            print_sleep("It is locked.")
        elif selected_option == 3:
            if scene_elements[0] is False:  # Verifies if the wall is broken
                print_sleep("The walls are old and some bricks seems loose.")
                print_sleep("As you force the loose bricks,")
                print_sleep("a portion of the wall crumbles.")
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
    """Describes the ocurrencies in the adjacent cell."""

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
            player_cell(items, health, enemies_alive, scene_elements)


def cell_block(items, health, enemies_alive, scene_elements):
    """Describes the ocurrencies in the player cell block."""

    print_sleep("You are now in the dungeon corridor.")
    options = ["Look around.", "Go to the Jailer Room."]

    while True:
        # If the skeleton has not yet been defeatd, the player can't proceed.
        if enemies_alive[0] is True:
            if "sword" not in items:
                print_sleep(
                    "The skeleton is at the other end of the corridor.")
                print_sleep("It has not yet noticed you.")
                print_sleep("You'd better find a weapon before fighting it.")
            else:
                print_sleep(
                    "The skeleton is at the other end of the corridor.")
                print_sleep("It has not yet noticed you.")
                print_sleep(
                    "Now that you have a sword, you might have a chance.")
                if "Fight skeleton." not in options:
                    options.append("Fight skeleton.")
        elif "Open the door." not in options:
            # Adds the option to continue after defeating the skeleton.
            options.append("Open the door.")
            options.append("Go through the right passage.")
            options.append("Go through the left passage.")

        selected_option = validate_option(options)

        if selected_option == 1:
            print_sleep("You can see that there are only two cells here.")
            print_sleep("Yours and the one you came out of.")
            print_sleep("The jailer room is at the end of this corridor.")
            print_sleep("There is a door that leads outside at the other end.")
            print_sleep(
                "And two passages, oposite to the other, beside that door.")
            if enemies_alive[0] is True:
                print_sleep("The skeleton is there.")
                print_sleep("You will have to defeat it.")
                print_sleep("Or you will not be able to go out.")
        elif selected_option == 2:
            jailer_room(items, health, enemies_alive, scene_elements)
        elif selected_option == 3:
            if enemies_alive[0] is True:
                # If the player defeats the skeleton, updates health
                health = combat(items, health, enemies_alive, scene_elements)
                # Updates the state of this skeleton
                options.remove("Fight skeleton.")
                enemies_alive[0] = False
            elif "key" in items:
                print_sleep("You unlock the door.")
                print_sleep("As you open it, you see a small village.")
                print_sleep("No villagers in sight.")
                print_sleep("Only dead bodies.")
                print_sleep("And many skeletons about.")
                print_sleep(
                    "Luckly, the prision is by the edge of the village.")
                print_sleep("So you manage to scape unoticed.")
                play_again()
            else:
                print_sleep("The door is locked.")
                print_sleep("You have to find the key.")
        elif selected_option == 4:
            guard_house(items, health, enemies_alive, scene_elements)
        elif selected_option == 5:
            kitchen(items, health, enemies_alive, scene_elements)


def jailer_room(items, health, enemies_alive, scene_elements):
    """Describes the ocurrencies in the player jailer room."""

    print_sleep("You are in the jailer room.")
    options = ["Look around.", "Go back."]

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
            print_sleep("The room is dark.")
            print_sleep("There is a table, a chair and some other furniture.")
            print_sleep("But there is nothing of use on them.")
            print_sleep("There are bars on the windows.")
        elif selected_option == 2:
            cell_block(items, health, enemies_alive, scene_elements)
        elif selected_option == 3:
            print_sleep("You take the sword.")
            print_sleep("Now you might have a chance to escape.")
            items.append("sword")
            options.remove("Take the sword.")


def guard_house(items, health, enemies_alive, scene_elements):
    """Describes the ocurrencies in the player guard house."""

    print_sleep("You are in the guard house.")
    options = ["Look around.", "Go back."]

    while True:
        selected_option = validate_option(options)

        if selected_option == 1:
            print_sleep("There are a couple of beds.")
            print_sleep("And nobody in sight.")
            print_sleep("The guards must have ran away.")
            if scene_elements[1] is False:  # If the potion was not yet drunk
                print_sleep("The only useful thing you find is a potion.")
                print_sleep("As you drink it, you fell better.")
                print_sleep("Back to full health.")
                scene_elements[1] = True
                health = 30
        elif selected_option == 2:
            cell_block(items, health, enemies_alive, scene_elements)


def kitchen(items, health, enemies_alive, scene_elements):
    """Describes the ocurrencies in the player kitchen."""

    print_sleep("You are in the kitchen.")
    options = ["Look around.", "Go back."]

    if enemies_alive[1] is True:
        print_sleep("As you enter, a skeleton attacks you.")
        print_sleep("You avoid its first attack.")
        print_sleep("But you can't escape. You have to face it.")
        health = combat(items, health, enemies_alive, scene_elements)
        enemies_alive[1] = False

    while True:
        selected_option = validate_option(options)

        if selected_option == 1:
            print_sleep("There are several cooking utensils.")
            print_sleep("Nothing particularly interesting.")
            if "key" not in items:
                print_sleep("As you look around, you find a key on the table.")
                print_sleep("It must open the front door!")
                items.append("key")
            else:
                print_sleep("There is nothing left to do here.")
        elif selected_option == 2:
            cell_block(items, health, enemies_alive, scene_elements)


# End of scene based functions

def combat(items, health, enemies_alive, scene_elements):
    """
    Simulates combat between the player and enemies by randomly
    choosing a number to subtract from their health points, updating
    the current state to the player through text messages.
    If the enemy is defeated, returns the player remaining health,
    otherwise, call play_again().

    Parameters:
        items (list): Store player items.
        health (int): Store player health points.
        enemies_alive (list): Store the current state of enemies.
        scene_elements (list): Store interaction state of scene elements.

    Returns:
        health (int): Returns the remaining health of the player.
    """

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
            print_sleep("Your vision darkens as your life escapes you.")
            print_sleep("You didn't manage to escape the dungen this time.")
            play_again()

        if enemy_health > 0:
            print_sleep("The skeleton attacks you.")
            damage_dealt = random.randint(1, 6)
            health -= damage_dealt
            print_sleep(f"It has caused {damage_dealt} points of damage.")
            print_sleep(f"You have {health} health points left.")
        else:
            print_sleep("You have defeated the skeleton.")
            return health


def play_again():
    """Ask the player if he wants to play again."""
    options = ["Yes", "No"]
    print_sleep("Would you like to play again?")

    selected_option = validate_option(options)

    while True:
        if selected_option == 1:
            play_game()
        elif selected_option == 2:
            print_sleep("Thank you for playing.")
            exit()


def play_game():
    """Starts and manages the game."""

    # Player statistics
    items = []
    health = 25

    # Game Logic
    enemies_alive = [True, True]  # Are the enemies alive?
    scene_elements = [False, False]  # Is the wall broken? the potion drunk?

    intro(items, health, enemies_alive, scene_elements)


# Start the game
if __name__ == "__main__":
    play_game()
