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


def get_remaining_cards():
    values = []
    for suit in suits_cards.keys():
        for value in suits_cards[suit]:
            values.append(value)
    return len(values)


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


def get_random_card():
    suit = random.choice(list(suits_cards.keys()))
    while len(suits_cards[suit]) < 1:
        suit = random.choice(list(suits_cards.keys()))
    rank = random.choice(suits_cards[suit])
    return suit, rank


def remove_card(suit, rank):
    try:
        suits_cards[suit].remove(rank)
    except:
        print(f"{f.RED}ERROR\t| {rank} of {suit} couldn't be removed.{s.RESET_ALL}")


def start_dungeon():
    reset_deck()
    # DUNGEON
    room_number = 0
    room_cards = []
    # PLAYER
    health = 20

    def show_health():
        return f"{s.RESET_ALL}You have {f.GREEN if health >= 10 else f.RED}{health}{s.RESET_ALL} Health."
    equipped_weapon = 0
    last_card_hit_with_weapon = 15

    clear_print(
        f"{f.BLUE}Dungeon Started\t|{s.RESET_ALL} {show_health()}")
    while 1:
        if len(room_cards) < 2 and get_remaining_cards() > 2:
            room_number += 1
            while len(room_cards) < 4:
                suit, rank = get_random_card()
                remove_card(suit, rank)
                rank = rank_to_name(rank)
                room_cards.append(str(rank) + " of " + suit)
        # WIN CONDITION
        elif len(room_cards) < 2 and get_remaining_cards() <= 2:
            print(
                f"{f.GREEN}YOU CLEARED THE DUNGEON WITH {health} HEALTH REMAINING.\n|\tYou Win!\n{s.RESET_ALL}")
            break

        print(f"{f.MAGENTA}\nRoom #{room_number}: ")
        c = 1
        for card in room_cards:
            print(
                f"{f.WHITE if card.split()[-1][0].upper() in ["S", "C"] else f.RED}{c}->\t|\t{card}\t\t|\n{s.RESET_ALL}")
            c += 1
        c = 1
        card_to_play = input(f"Which card to play: ")
        try:
            card_to_play = int(card_to_play) - 1
            played_card = room_cards[card_to_play]
            room_cards.remove(played_card)
            played_card_rank = played_card.split()[0]
            # SET CORRECT RANK FOR DAMAGE FROM FACE CARD NAMES
            if played_card_rank == "Jack":
                played_card_rank = 11
            elif played_card_rank == "Queen":
                played_card_rank = 12
            elif played_card_rank == "King":
                played_card_rank = 13
            elif played_card_rank == "Ace":
                played_card_rank = 14
            else:
                played_card_rank = int(played_card_rank)
            played_card_suit = played_card.split()[-1][0].upper()
            print(f"You Played {played_card}\t**DEBUG\t|\tRank: {played_card_rank}, Type: {type(played_card_rank)}\t|\tSuit: {played_card_suit}, Type: {type(played_card_suit)}")

            if played_card_suit in ["C", "S"]:
                if played_card_rank < last_card_hit_with_weapon and equipped_weapon > 0:
                    health -= played_card_rank - equipped_weapon if played_card_rank - equipped_weapon > 0 else 0
                    print(
                        f"You have been hit for {played_card_rank} - {equipped_weapon} = {played_card_rank - equipped_weapon}. {show_health()}")
                    last_card_hit_with_weapon = played_card_rank
                else:
                    health -= played_card_rank
                    print(
                        f"You have been hit for {played_card_rank}. {show_health()}")
            elif played_card_suit == "D":
                print(f"Weapon set: {played_card}")
                equipped_weapon = int(played_card_rank)
                last_card_hit_with_weapon = 15
                print(f"DEBUG\t|\tEquipped weapon damage: {equipped_weapon}")
            else:
                health += int(played_card_rank)
                if health > 20:
                    health = 20
                print(
                    f"Healed for: {f.GREEN}{played_card_rank}{s.RESET_ALL}. {show_health()}")
        except:
            print(f"{f.RED}NOT A VALID INPUT{s.RESET_ALL}")

        if health < 1:
            print(f"{f.RED}YOU DIED.\n{s.RESET_ALL}")
            input()
            break


def show_help():
    clear_print(f"{f.MAGENTA}Keep in mind you can always find online tutorials on how to play the game. Just search \"How to play Scoundrel Card Game\"{s.RESET_ALL}\n\n"
                f"{f.YELLOW} Scoundrel {s.RESET_ALL}\n"
                f"{f.WHITE}Imagine there's some helpful tutorial here\n\n\n")


# MAIN LOOP
while 1:
    # AVAILABLE OPTIONS
    clear_print(
        f"{f.BLACK}{b.CYAN} Choose One of the options: \n{s.RESET_ALL}")
    print(f"{f.GREEN}1. {f.WHITE}Start the Dungeon\n"
          f"{f.GREEN}2. {f.WHITE}Remove cards\n"
          f"{f.GREEN}3. {f.WHITE}Show current cards\n"
          f"{f.GREEN}4. {f.WHITE}Reset Deck to default\n"
          f"{f.GREEN}5. {f.WHITE}How to Play\n"
          f"{f.RED}X. {f.WHITE}Quit")

    op = input(f"\n{f.MAGENTA}--> {f.WHITE}").upper()

    # OPTION CHOSEN
    if op == "1":
        start_dungeon()

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
        reset_deck()
        clear_print(
            f"{f.GREEN}OK\t| DECK RESET . . .{s.RESET_ALL}\n\nPress enter to go back to the main menu . . .")
        input()

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
