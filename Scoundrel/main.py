import os
from colorama import Fore as f
from colorama import Style as s


def clear():
    os.system('cls')


def clear_print(text):
    clear()
    print(text)


# CARDS
Suits = ["♠ Spades", "♣ Clubs", "♥ Hearts", "♦ Diamonds"]
Spades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
Clubs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
Hearts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Diamonds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_suit_color(suit: str):
    if suit == "Spades" or suit == "Clubs":
        return "Black"
    else:
        return "Red"


def show_current_cards():
    clear_print(f"{f.GREEN}-> Current Cards in the deck :\n")
    for suit in Suits:
        if get_suit_color(suit[2:]) == "Black":
            print(f"{f.WHITE}    {suit}:")
        else:
            print(f"{f.RED}    {suit}:")
        for card in eval(suit[1:]):
            if card > 10 or card == str:
                if card == 11:
                    card = "Jack"
                elif card == 12:
                    card = "Queen"
                elif card == 13:
                    card = "King"
                elif card == 14:
                    card = "Ace"
                else:
                    card = "Unknown"
            print(f"        {card} {suit[:1]}", end="")
        print(f"\n{s.RESET_ALL}")


def draw_card():
    pass


def show_help():
    clear_print(f"{f.MAGENTA}Keep in mind you can always find online tutorials on how to play the game.{s.RESET_ALL}\n\n"
                f"{f.YELLOW} Scoundrel {s.RESET_ALL}\n"
                f"{f.WHITE}Imagine there's some helpful tutorial here\n\n\n")


while 1:
    clear_print(f"{f.GREEN}Choose One of the options: \n")
    print(f"{f.GREEN}1. {f.WHITE}Start the Dungeon\n"
          f"{f.GREEN}2. {f.WHITE}Edit cards\n"
          f"{f.GREEN}3. {f.WHITE}Show current cards\n"
          f"{f.GREEN}5. {f.WHITE}How to Play")
    op = input(f"\n{f.MAGENTA}--> {f.WHITE}")
    if op == "1":
        clear_print(
            f"{f.RED}Starting the dungeon is not available yet . . .{s.RESET_ALL}")
        input(f"{f.BLUE}Press Enter to go to the main menu . . .{s.RESET_ALL}")
    elif op == "2":
        show_current_cards()
        input(f"{f.BLUE}Choose a card to remove - e.g. 2S ( 2 of Spades ), KH ( King of Hearts ):\t{s.RESET_ALL}")
    elif op == "3":
        show_current_cards()
        input(f"{f.BLUE}Press Enter to go to the main menu . . .{s.RESET_ALL}")
    elif op == "5":
        show_help()
        input(f"{f.BLUE}Press Enter to go to the main menu . . .{s.RESET_ALL}")
    else:
        print(f"{f.RED}\n\n\n- - - Not an operation | Aborting - - -{s.RESET_ALL}")
        break
