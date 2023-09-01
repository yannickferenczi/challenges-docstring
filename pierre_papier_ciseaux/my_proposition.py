import os, sys
from random import choice
from time import sleep

CHOICES_LIST = ["pierre", "papier", "ciseaux"]

PLAYER_POSSIBLE_COMBINATIONS = {
    ("pierre", "pierre"): (
        0, "Égalité ! Recommencez...", 0,
    ),
    ("pierre", "papier"): (
        0, "Vous avez perdu! Le papier enveloppe la pierre.", 1,
    ),
    ("pierre", "ciseaux"): (
        1, "Vous avez gagné! La pierre brise les ciseaux.", 0,
    ),
    ("papier", "pierre"): (
        1, "Vous avez gagné! Le papier enveloppe la pierre.", 0,
    ),
    ("papier", "papier"): (
        0, "Égalité ! Recommencez...", 0,
    ),
    ("papier", "ciseaux"): (
        0, "Vous avez perdu! Les ciseaux coupent le papier.", 1,
    ),
    ("ciseaux", "pierre"): (
        0, "Vous avez perdu! La pierre brise les ciseaux.", 1,
    ),
    ("ciseaux", "papier"): (
        1, "Vous avez gagné! Les ciseaux coupent le papier.", 0,
    ),
    ("ciseaux", "ciseaux"): (
        0, "Égalité ! Recommencez...", 0,
    ),
}

def typing_print(text):
    """Display the text with a typing effect."""
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.05)

def typing_input(text):
    """Display the text of an input with a typing effect."""
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.05)
    value = input()
    return value

def choice_is_valid(player_choice):
    """Return True is player_choice in CHOICES_LIST"""
    return player_choice in CHOICES_LIST

def computer_plays():
    """Defines the hand of the computer"""
    return choice(CHOICES_LIST)

def player_plays():
    """
    Ask the player to choose between rock, paper, and cisors.
    
    The function keeps asking the player until it gets a valid answer.
    """
    player_choice = typing_input("\nChoisi ton arme: " )
    if choice_is_valid(player_choice):
        return player_choice
    else:
        typing_print(
"""
Ton choix n'est pas valide! Merci de choisir parmi les
options suivantes (la casse est prise en compte):

pierre
papier
ciseaux

"""
        )
        return player_plays()


if __name__ == "__main__":
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    typing_print(
"""
Salut jeune aventurier, et bienvenue pour une partie de pierre,
papier ou ciseaux!

Pour jouer, c'est simple: tape ton choix en toutes lettres et tout
en minuscule. Les seules entrées acceptées sont 'pierre' 'papier'
ou 'ciseaux'.

"""
    )

    computer_points = 0
    player_points = 0

    while True:
        computer_move = computer_plays()
        player_move = player_plays()
        game = (player_move, computer_move)
        computer_points += PLAYER_POSSIBLE_COMBINATIONS[game][2]
        player_points += PLAYER_POSSIBLE_COMBINATIONS[game][0]
        typing_print("\n" + PLAYER_POSSIBLE_COMBINATIONS[game][1] + "\n")
        if PLAYER_POSSIBLE_COMBINATIONS[game][1] == "Égalité ! Recommencez...":
            continue
        else:
            typing_print(
f"""
\nTu as {player_points} point{'s' if player_points > 1 else ""}.
L'ordinateur a {computer_points} point{'s' if computer_points > 1 else ""}.\n
"""
            )
            while True:
                try_again = typing_input("\nNouvelle partie? (y/n) \n")
                if try_again == "y":
                    break
                elif try_again == "n":
                    sys.exit(0)
                else:
                    typing_print("\nTa décision n'est pas claire!\n")
