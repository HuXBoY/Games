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


def draw_card(rank: int, suit: str):
    # print(f"{f.MAGENTA}DEBUG\t| rank: {rank}, suit: {suit}")
    suit_name = None
    if suit == "S" or suit == "s":
        suit = Spades
        suit_name = "Spades"
    elif suit == "C" or suit == "c":
        suit = Clubs
        suit_name = "Clubs"
    elif suit == "H" or suit == "h":
        suit = Hearts
        suit_name = "Hearts"
    elif suit == "D" or suit == "d":
        suit = Diamonds
        suit_name = "Diamonds"

    # print(f"{f.MAGENTA}DEBUG2\t| rank: {rank}, type: {type(rank)}; suit: {suit}, type: {type(suit)}")

    if rank in suit:
        suit.remove(rank)
        clear()
        show_current_cards()
        print(f"\n{f.GREEN}OK \t| Removed {rank} of {suit_name}{s.RESET_ALL}")
        # do = input("Enter to go back to main menu . . .")
    else:
        print(
            f"{f.RED}ERROR \t| Either that card does not exist or there's an Error!{s.RESET_ALL}")


def show_help():
    clear_print(f"{f.MAGENTA}Keep in mind you can always find online tutorials on how to play the game. Just search \"How to play Scoundrel Card Game\"{s.RESET_ALL}\n\n"
                f"{f.YELLOW} Scoundrel {s.RESET_ALL}\n"
                f"{f.WHITE}Imagine there's some helpful tutorial here\n\n\n")


while 1:
    clear_print(f"{f.GREEN}Choose One of the options: \n")
    print(f"{f.GREEN}1. {f.WHITE}Start the Dungeon\n"
          f"{f.GREEN}2. {f.WHITE}Remove cards\n"
          f"{f.GREEN}3. {f.WHITE}Show current cards\n"
          f"{f.GREEN}5. {f.WHITE}How to Play\n"
          f"{f.RED}X. {f.WHITE}Quit")

    op = input(f"\n{f.MAGENTA}--> {f.WHITE}").upper()

    if op == "1":
        clear_print(
            f"{f.RED}Starting the dungeon is not available yet . . .{s.RESET_ALL}")
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
