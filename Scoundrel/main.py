from colorama import Style as s
from colorama import Back as b
from colorama import Fore as f
import random
import os


def clear():
    os.system('cls')


def clear_print(text):
    clear()
    print(text)


Suits = ["♠ Spades", "♣ Clubs", "♥ Hearts", "♦ Diamonds"]
suits_cards = {
    "Spades": list(range(1, 15)),      # 1 to 14
    "Clubs": list(range(1, 15)),
    "Hearts": list(range(1, 11)),      # 1 to 10
    "Diamonds": list(range(1, 11)),
}


def reset_deck():
    global suits_cards
    suits_cards = {
        "Spades": list(range(1, 15)),
        "Clubs": list(range(1, 15)),
        "Hearts": list(range(1, 11)),
        "Diamonds": list(range(1, 11)),
    }


def get_suit_color(suit: str):
    if suit == "Spades" or suit == "Clubs":
        return "Black"
    else:
        return "Red"


def get_random_card():
    rand_suit_choice = random.choice(Suits)
    suit_symbol = rand_suit_choice[:2]
    suit_name = rand_suit_choice[2:]

    rank = random.choice(suits_cards[suit_name])
    return f"{rank} {suit_symbol}"


def rank_to_name(rank: int) -> str:
    names = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
    return names.get(rank, str(rank))


def show_current_cards():
    clear_print(f"{f.GREEN}-> Current Cards in the deck :\n")
    for suit_display in Suits:
        symbol = suit_display[:2]
        name = suit_display[2:]
        color = f.WHITE if get_suit_color(name) == "Black" else f.RED
        print(f"{color}    {suit_display}:")
        for rank in suits_cards[name]:
            card_name = rank_to_name(rank)
            print(f"        {card_name} {symbol}", end="")
        print(f"\n{s.RESET_ALL}")


def draw_card(rank: int, suit: str):
    suit_map = {
        "S": ("Spades", f.WHITE),
        "C": ("Clubs", f.WHITE),
        "H": ("Hearts", f.RED),
        "D": ("Diamonds", f.RED),
    }
    if suit.upper() not in suit_map:
        print(f"{f.RED}ERROR \t| Invalid suit!{s.RESET_ALL}")
        return

    suit_name, _ = suit_map[suit.upper()]
    if rank in suits_cards[suit_name]:
        suits_cards[suit_name].remove(rank)
        clear()
        show_current_cards()
        print(f"\n{f.GREEN}OK \t| Removed {rank} of {suit_name}{s.RESET_ALL}")
    else:
        print(f"{f.RED}ERROR \t| Card not in deck!{s.RESET_ALL}")


def show_help():
    clear_print(f"{f.MAGENTA}Keep in mind you can always find online tutorials on how to play the game. Just search \"How to play Scoundrel Card Game\"{s.RESET_ALL}\n\n"
                f"{f.YELLOW} Scoundrel {s.RESET_ALL}\n"
                f"{f.WHITE}Imagine there's some helpful tutorial here\n\n\n")


# MAIN LOOP
while 1:
    # AVAILABLE OPTIONS
    clear_print(f"{f.GREEN}Choose One of the options: \n")
    print(f"{f.GREEN}1. {f.WHITE}Start the Dungeon\n"
          f"{f.GREEN}2. {f.WHITE}Remove cards\n"
          f"{f.GREEN}3. {f.WHITE}Show current cards\n"
          f"{f.GREEN}5. {f.WHITE}How to Play\n"
          f"{f.RED}X. {f.WHITE}Quit")

    op = input(f"\n{f.MAGENTA}--> {f.WHITE}").upper()

    # OPTION CHOSEN
    if op == "1":
        clear_print(
            f"{f.GREEN}OK\t| Starting the dungeon . . .{s.RESET_ALL}")
        print(f"{f.MAGENTA} Room #1: ")

        # STAY IN THE DUNGEON
        input(f"{f.BLUE}Press Enter to go to the main menu . . .{s.RESET_ALL}")

    elif op == "2":
        while 1:
            show_current_cards()

            suit_to_remove = None
            rank_to_remove = None
            canceled = False
            print(
                f"{f.MAGENTA}ENTER X TO CANCEL\n{f.BLUE}Remove a card: Select card suit [S,C,H,D]:\t{s.RESET_ALL}", end="")
            while 1:
                suit_to_remove = input().upper()

                if suit_to_remove == "X":
                    canceled = True
                    break
                elif suit_to_remove not in ["S", "C", "H", "D"]:
                    print(
                        f"{f.RED}NOT A VALID SUIT \t| {f.BLUE}Select card suit [S,C,H,D]:\t{s.RESET_ALL}", end="")
                else:
                    break

            if not canceled:
                print(
                    f"{f.BLUE}Select card rank [1-14]:\t\t{s.RESET_ALL}", end="")
                while 1:
                    rank_to_remove = input().upper()
                    if rank_to_remove == "X":
                        canceled = True
                        break
                    try:
                        rank_to_remove = int(rank_to_remove)
                        if 1 <= rank_to_remove <= 14:
                            break
                        else:
                            print(
                                f"{f.RED}NOT IN RANGE: {f.BLUE}Select card rank [1-14]:\t{s.RESET_ALL}", end="")
                    except ValueError:
                        print(
                            f"{f.RED}NOT A NUMBER: {f.BLUE}Select card rank [1-14]:\t{s.RESET_ALL}", end="")

                if rank_to_remove != "X":
                    draw_card(rank_to_remove, suit_to_remove)
                    input(f"{f.BLUE}Press enter to continue . . .{s.RESET_ALL}")
                else:
                    canceled = True

            if canceled:
                break

    elif op == "3":
        show_current_cards()
        input(f"{f.BLUE}Press Enter to go to the main menu . . .{s.RESET_ALL}")

    elif op == "4":
        input(f"This option is clearly not in the list bro...\nPress Enter to try again, Also open your eyes!")

    elif op == "5":
        show_help()
        input(f"{f.BLUE}Press Enter to go to the main menu . . .{s.RESET_ALL}")

    elif op == "X":
        clear_print(f"{f.RED}- - - Quitted - - -{s.RESET_ALL}")
        break

    else:
        op2 = input(
            f"{f.RED}\n\tERROR\t| NOT A VALID OPTION. PRESS ENTER TO TRY AGAIN OR X TO QUIT: {s.RESET_ALL}").upper()
        if op2 == "X":
            clear_print(f"{f.RED}- - - Quitted - - -{s.RESET_ALL}")
            break
