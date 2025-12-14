from colorama import Style as s
from colorama import Back as b
from colorama import Fore as f
from time import sleep
import random
import os

# SYS/TERMINAL VARS
h_center = os.get_terminal_size().lines // 2
w_center = os.get_terminal_size().columns // 2
time_to_start = 1


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


def get_random_card():
    suit = random.choice(list(suits_cards.keys()))
    while len(suits_cards[suit]) < 1:
        suit = random.choice(list(suits_cards.keys()))
    rank = random.choice(suits_cards[suit])
    return suit, rank


def remove_card(suit, rank):
    if suit == "S":
        suit = "Spades"
    elif suit == "C":
        suit = "Clubs"
    elif suit == "H":
        suit = "Hearts"
    elif suit == "D":
        suit = "Diamonds"
    try:
        suits_cards[suit].remove(rank)
    except:
        print(f"{f.RED}ERROR\t| {rank} of {suit} couldn't be removed.{s.RESET_ALL}")


def start_dungeon():
    # DUNGEON
    room_number = 0
    room_cards = []
    # PLAYER
    health = 20
    equipped_weapon = 0
    last_card_hit_with_weapon = 15
    last_card_played = None
    # MANAGER
    new_room = False
    cards_played = []
    

    def show_health():
        return f"{s.RESET_ALL}You have {f.GREEN if health >= 10 else f.RED}{health}{s.RESET_ALL} Health."

    def show_stats():
        texts = [f"Health: {f.GREEN}{health} {"▰" * health}{f.WHITE}{"▱" * (20 - health)} 20",
                 f"Equipped weapon: {equipped_weapon}",
                 f"Last hit with weapon: {None if last_card_hit_with_weapon == 15 else last_card_hit_with_weapon} {s.RESET_ALL}",
                 f"Last card played: {last_card_played}"]
        line = 1
        for text in texts:
            print(f"\033[{line};1H{text}\n")
            line += 1
        

    def show_help():
        texts = ["Name  ->  Rank",
                 "Jack  ->   11 ",
                 "Queen ->   12 ",
                 "King  ->   13 ",
                 "Ace   ->   14 "]
        line = 1
        for text in texts:
            print(
                f"\033[{line};{os.get_terminal_size().columns}H{"\b" * len(list(text))}{text}")
            line += 1
        side_bar_width = 20
        cards_help_section_height = 7
        for lines in range(os.get_terminal_size().lines - 1):
            if lines + 1 == cards_help_section_height:
                print(f"\033[{lines+1};{os.get_terminal_size().columns - side_bar_width}H┣")
            else:
                print(f"\033[{lines+1};{os.get_terminal_size().columns - side_bar_width}H┃")
        for columns in range(side_bar_width):
            print(f"\033[{cards_help_section_height};{os.get_terminal_size().columns - side_bar_width + (columns + 1)}H━")

        remaining_cards = len(suits_cards["Spades"]) + len(suits_cards["Clubs"]) + len(suits_cards["Diamonds"]) + len(suits_cards["Hearts"])
        remaining_cards_text = f"Remaining cards: {remaining_cards}"
        print(f"\033[1;{os.get_terminal_size().columns - ( side_bar_width + 1 )}H\033[{len(list(remaining_cards_text))}D{remaining_cards_text}")

        section_start_line = 10
        line = section_start_line
        section_height = os.get_terminal_size().lines - ( section_start_line + 1 )
        if len(cards_played) > 0:
            if len(cards_played) < section_height:
                cards_played.reverse()
                for card in cards_played:
                    print(f"\033[{line};{os.get_terminal_size().columns}H\033[{side_bar_width}D\033[{(side_bar_width - len(list(card.strip())))}C{card.strip()}")
                    line += 1
                cards_played.reverse()
            else:
                cards_played.reverse()
                for i in range(section_height - 1):
                    print(f"\033[{line};{os.get_terminal_size().columns}H\033[{side_bar_width}D\033[{(side_bar_width - len(list(cards_played[i].strip())))}C{cards_played[i].strip()}")
                    line += 1
                print(f"\033[{line};{os.get_terminal_size().columns}H\033[{side_bar_width}D\033[{(side_bar_width - len(list(cards_played[i].strip())))}C . . .")
                cards_played.reverse()

    while 1:
        clear()
        if len(room_cards) < 2 and get_remaining_cards() > 2:
            room_number += 1
            if room_number > 1:
                new_room = True
            while len(room_cards) < 4:
                suit, rank = get_random_card()
                remove_card(suit, rank)
                rank = rank_to_name(rank)
                room_cards.append(str(rank) + " of " + suit)
        # WIN CONDITION
        elif len(room_cards) < 2 and get_remaining_cards() <= 2:
            win_texts = [f"YOU CLEARED THE DUNGEON WITH {f.GREEN}{health}{s.RESET_ALL} HEALTH REMAINING.",
                         "You win !"]
            clear_print(f"\033[{h_center};{w_center}H{"\b" * ( len(list(win_texts[0])) // 2 - 5)}{win_texts[0]}")
            print(f"\033[{h_center + 1};{w_center}H{"\b" * ( len(list(win_texts[1])) // 2)}{win_texts[1]}")
            break

        if new_room:
            clear_print(f"{f.MAGENTA}{"\n" * 5}Room #{room_number}: ")
            new_room = False
        else:
            print(f"{f.MAGENTA}{"\n" * 5}Room #{room_number}: ")
        c = 1
        for card in room_cards:
            print(
                f"{f.WHITE if card.split()[-1][0].upper() in ["S", "C"] else f.RED}{c}->\t|\t{card}\t\t|\n{s.RESET_ALL}")
            c += 1
        c = 1
        show_stats()
        show_help()
        card_to_play = input(
            f"\033[{os.get_terminal_size().lines};1HWhich card to play: ")
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
            if last_card_played != None:
                cards_played.append(last_card_played)
            last_card_played = played_card
            print(f"You Played {played_card}")

            if played_card_suit in ["C", "S"]:
                if played_card_rank < last_card_hit_with_weapon and equipped_weapon > 0:
                    health -= played_card_rank - \
                        equipped_weapon if played_card_rank - equipped_weapon > 0 else 0

                    print(
                        f"You have been hit for {played_card_rank} - {equipped_weapon} = {played_card_rank - equipped_weapon}. {show_health()}")
                    last_card_hit_with_weapon = played_card_rank
                else:
                    health -= played_card_rank
                    health = max(0, health)
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
            print(f"{f.WHITE + b.RED}NOT A VALID INPUT{s.RESET_ALL}")

        if health < 1:
            print(f"{f.RED}YOU DIED.\n{s.RESET_ALL}")
            input()
            break


def show_help():
    clear()
    print(f"{f.CYAN}{s.BRIGHT}{'=' * 60}{s.RESET_ALL}")
    print(f"{f.MAGENTA}{s.BRIGHT}                  SCOUNDREL - COMPUTER EDITION                  {s.RESET_ALL}")
    print(f"{f.CYAN}{s.BRIGHT}{'=' * 60}{s.RESET_ALL}")
    print(f"{f.YELLOW}A solo roguelike card game by Zach Gage & Kurt Bieg{s.RESET_ALL}")
    print(f"{f.YELLOW}    Python terminal version - Built by Hu-Bo-    {s.RESET_ALL}")
    print()

    input(f"{f.BLUE}Press Enter for Setup & Deck...{s.RESET_ALL}")

    clear_print(f"{f.GREEN}{s.BRIGHT}🎮 SETUP & DECK{s.RESET_ALL}")
    print(f"{f.WHITE}The game automatically shuffles a custom deck:{s.RESET_ALL}")
    print()
    print(f"{f.RED}{s.BRIGHT}♠ Spades & ♣ Clubs (Monsters):{s.RESET_ALL} {f.WHITE}1-10, Jack(11), Queen(12), King(13), Ace(14) — {f.RED}14 each (28 total){s.RESET_ALL}")
    print(f"{f.YELLOW}{s.BRIGHT}♦ Diamonds (Weapons):{s.RESET_ALL} {f.WHITE}1-10 — {f.YELLOW}10 total{s.RESET_ALL}")
    print(f"{f.GREEN}{s.BRIGHT}♥ Hearts (Potions):{s.RESET_ALL} {f.WHITE}1-10 — {f.GREEN}10 total{s.RESET_ALL}")
    print()
    print(f"{f.CYAN}Starting Health: {f.GREEN}20{s.RESET_ALL} (capped at 20){f.CYAN}{s.RESET_ALL}")
    print(f"{f.CYAN}Deck total: 48 cards (digital shuffle){s.RESET_ALL}")
    print()

    input(f"{f.BLUE}Press Enter for Card Types & Effects...{s.RESET_ALL}")

    clear_print(f"{f.GREEN}{s.BRIGHT}⚔️  CARD TYPES & EFFECTS{s.RESET_ALL}")
    print(f"{f.RED}{s.BRIGHT}{'=' * 20} MONSTERS ♠♣ {'=' * 20}{s.RESET_ALL}{s.RESET_ALL}")
    print(f"{f.RED}Deal damage = rank value (e.g. 10=10, Jack=11, Ace=14){s.RESET_ALL}")
    print()
    print(f"{f.YELLOW}{s.BRIGHT}{'=' * 18} WEAPONS ♦ {'=' * 18}{s.RESET_ALL}{s.RESET_ALL}")
    print(f"{f.YELLOW}Equip automatically — replaces old weapon & resets 'monster limit'{s.RESET_ALL}")
    print(f"{f.YELLOW}Reduces damage from future monsters{s.RESET_ALL}")
    print()
    print(f"{f.GREEN}{s.BRIGHT}{'=' * 17} POTIONS ♥ {'=' * 17}{s.RESET_ALL}{s.RESET_ALL}")
    print(f"{f.GREEN}Heal = rank value (stacks all in room!){s.RESET_ALL}")
    print(f"{f.GREEN}Note: Unlike physical rules, {s.BRIGHT}ALL potions heal{s.RESET_ALL} — no limit per turn.{s.RESET_ALL}")
    print()

    input(f"{f.BLUE}Press Enter for Gameplay...{s.RESET_ALL}")

    clear_print(f"{f.GREEN}{s.BRIGHT}🕹️  GAMEPLAY{s.RESET_ALL}")
    print(f"{f.WHITE}1. Rooms auto-generate: {s.BRIGHT}4 cards shown, numbered 1-4{s.RESET_ALL}")
    print(f"{f.WHITE}2. Enter number to {s.BRIGHT}PLAY (resolve) that card{s.RESET_ALL}{f.WHITE}.{s.RESET_ALL}")
    print(f"{f.WHITE}3. Room shrinks. When there is only 1 card in the room: {s.BRIGHT}adds new cards to fill 4{s.RESET_ALL}")
    print(f"{f.WHITE}4. {s.BRIGHT}Order matters!{s.RESET_ALL} Play weapons/potions first? Save weak monsters for weapon?{s.RESET_ALL}")
    print()
    print(f"{f.MAGENTA}{s.BRIGHT}No 'avoid' rooms in this version — pure dungeon crawl!{s.RESET_ALL}")
    print()

    input(f"{f.BLUE}Press Enter for Monster Fighting...{s.RESET_ALL}")

    clear_print(f"{f.RED}{s.BRIGHT}👹 MONSTER FIGHTING DETAILS{s.RESET_ALL}")
    print(f"{f.WHITE}When playing ♠/♣:{s.RESET_ALL}")
    print()
    print(f"{f.CYAN}• {s.BRIGHT}No weapon or monster rank highter than last monster defeated with weapon?{s.RESET_ALL} {f.RED}Full damage!{s.RESET_ALL}")
    print(
        f"{f.CYAN}• {s.BRIGHT}Weapon equipped AND rank lower than last defeated monster?{s.RESET_ALL} Damage = {f.RED}[monster rank] - [weapon] -> if <0 it will {s.BRIGHT}NOT{s.RESET_ALL} Heal you. it just won't do damage{s.RESET_ALL}")
    print(f"{f.CYAN}  → Updates 'last defeated' to this monster's rank{s.RESET_ALL}")
    print()
    print(f"{f.YELLOW}New weapon always resets 'last defeated' to high (15){s.RESET_ALL}")
    print()
    print(f"{f.RED}{s.BRIGHT}EXAMPLE:{s.RESET_ALL}")
    print(f"{f.WHITE}Equip 5♦ → Can fight any monster first time.{s.RESET_ALL}")
    print(f"{f.RED}Play 3♠: 3 < 15 → dmg = max(0,3-5)=0, last=3{s.RESET_ALL}")
    print(f"{f.RED}Play Jack♠ (11): 11 ≮ 3 → full 11 dmg{s.RESET_ALL}")
    print(f"{f.RED}Play 2♠: 2 < 3 → dmg = max(0, 2-5) = 0, last=2{s.RESET_ALL}")
    print()
    print(f"{f.YELLOW}Note: Strict {s.BRIGHT}'<'{s.RESET_ALL} — can't repeat exact rank!{s.RESET_ALL}")

    input(f"{f.BLUE}Press Enter for Win/Lose...{s.RESET_ALL}")

    clear_print(f"{f.GREEN}{s.BRIGHT}🏆 WIN & LOSE{s.RESET_ALL}")
    print(f"{f.GREEN}{s.BRIGHT}WIN:{s.RESET_ALL} Clear deck (≤2 cards left) with room <2 → {f.GREEN}'Cleared with X health!'{s.RESET_ALL}")
    print()
    print(f"{f.RED}{s.BRIGHT}LOSE:{s.RESET_ALL} Health <1 → {f.RED}'YOU DIED'{s.RESET_ALL}")
    print()
    print(f"{f.CYAN}Score = remaining health (no negative/monster sum in this version){s.RESET_ALL}")
    print()
    print(f"{f.YELLOW}{s.BRIGHT}TIPS:{s.RESET_ALL}")
    print(f"{f.WHITE}• Use {s.BRIGHT}option 2/3/4{s.RESET_ALL} to edit deck & practice!{s.RESET_ALL}")
    print(f"{f.WHITE}• {s.BRIGHT}DEBUG{s.RESET_ALL} info shown during play (rank/suit types){s.RESET_ALL}")
    print(f"{f.WHITE}• Search '{s.BRIGHT}How to play Scoundrel Card Game{s.RESET_ALL}' for original physical rules!{s.RESET_ALL}")
    print()

    input(f"{f.BLUE}Press Enter to return...{s.RESET_ALL}")


# MAIN LOOP
while 1:
    # REMINDER
    clear_print(
        f"\033[{h_center};{w_center}H{"\b" * (len(list(" Please go Fullscreen "))//2)}{b.YELLOW}{f.BLACK} Please go Fullscreen {s.RESET_ALL}")
    print(f"\033[{h_center+1};{w_center}H{"\b" * (len(list(f" Starting in {time_to_start} Seconds! "))//2)}{b.MAGENTA} Starting in \033[s{time_to_start} Seconds! {s.RESET_ALL}")
    while time_to_start > -1:
        h_center = os.get_terminal_size().lines // 2
        w_center = os.get_terminal_size().columns // 2
        sleep(1)
        print(f"\033[u{time_to_start}")
        time_to_start -= 1
    print(s.RESET_ALL)
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
        input(f"\033[{os.get_terminal_size().lines};{os.get_terminal_size().columns // 2 - len(list(" Press Enter to go to the main menu . . . ")) // 2}H{b.BLUE}{f.WHITE} Press Enter to go to the main menu . . . {s.RESET_ALL}")

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
                    remove_card(suit_to_remove, rank_to_remove)
                    if suit_to_remove == "S":
                        suit_to_remove = "Spades"
                    elif suit_to_remove == "C":
                        suit_to_remove = "Clubs"
                    elif suit_to_remove == "H":
                        suit_to_remove = "Hearts"
                    elif suit_to_remove == "D":
                        suit_to_remove = "Diamonds"
                    print(
                        f"{s.BRIGHT + f.YELLOW}The card [{rank_to_remove} of {suit_to_remove}] Removed . . .{s.RESET_ALL}")
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

    elif op == "X":
        clear_print(f"{f.RED}- - - Quitted - - -{s.RESET_ALL}")
        break

    else:
        op2 = input(
            f"{f.RED}\n\tERROR\t| NOT A VALID OPTION. PRESS ENTER TO TRY AGAIN OR X TO QUIT: {s.RESET_ALL}").upper()
        if op2 == "X":
            clear_print(f"{f.RED}- - - Quitted - - -{s.RESET_ALL}")
            break
