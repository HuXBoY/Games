from time import sleep
import random
import os

class Text:
    Reset = "\033[0m"

    class Fore:
        Reset = "\033[38m"
        Black = "\033[30m"
        Red = "\033[31m"
        Green = "\033[32m"
        Yellow = "\033[33m"
        Blue = "\033[34m"
        Magenta = "\033[35m"
        Cyan = "\033[36m"
        White = "\033[37m"
        #
        Bright_Black = "\033[90m"
        Bright_Red = "\033[91m"
        Bright_Green = "\033[92m"
        Bright_Yellow = "\033[93m"
        Bright_Blue = "\033[94m"
        Bright_Magenta = "\033[95m"
        Bright_Cyan = "\033[96m"
        Bright_White = "\033[97m"

    class Back:
        Reset = "\033[48m"
        Black = "\033[40m"
        Red = "\033[41m"
        Green = "\033[42m"
        Yellow = "\033[43m"
        Blue = "\033[44m"
        Magenta = "\033[45m"
        Cyan = "\033[46m"
        White = "\033[47m"
        #
        Bright_Black = "\033[100m"
        Bright_Red = "\033[101m"
        Bright_Green = "\033[102m"
        Bright_Yellow = "\033[103m"
        Bright_Blue = "\033[104m"
        Bright_Magenta = "\033[105m"
        Bright_Cyan = "\033[106m"
        Bright_White = "\033[107m"

    def Fore_VGA(color: int) -> str:
        return f"\033[38;5;{color}m"

    def Back_VGA(color: int) -> str:
        return f"\033[48;5;{color}m"

    class VGA:
        # Extended useful colors (grayscale and common hues)
        Orange = 208
        Pink = 218
        Lime = 118
        Teal = 37
        Coral = 204
        Gold = 220
        Salmon = 210
        Indigo = 54
        Gray1 = 232  # Darkest gray
        Gray2 = 235
        Gray3 = 239
        Gray4 = 243
        Gray5 = 247
        Gray6 = 250
        Gray7 = 254  # Lightest gray

    class Effect:
        Bold = "\033[1m"
        Dim = "\033[2m"
        Underline = "\033[4m"
        Blink = "\033[5m"
        Reverse = "\033[7m"
        Hide = "\033[8m"
        OFF = "\033[21m\033[22m\033[24m\033[25m\033[27m\033[28m"

# SYS/TERMINAL VARS
terminal_size = os.get_terminal_size()
terminal_columns = terminal_size.columns
terminal_lines = terminal_size.lines
h_center = terminal_lines // 2
w_center = terminal_columns // 2
def refresh_terminal():
    global terminal_size, terminal_columns, terminal_lines, h_center, w_center
    terminal_size = os.get_terminal_size()
    terminal_columns = terminal_size.columns
    terminal_lines = terminal_size.lines
    h_center = terminal_lines // 2
    w_center = terminal_columns // 2
time_to_start = 1


def clear():
    os.system('cls')


def clear_print(text):
    clear()
    print(text)


Suits = ["♠ Spades", "♣ Clubs", "♥ Hearts", "♦ Diamonds"]
suits_cards = {
    "Spades": list(range(1, 15)),
    "Clubs": list(range(1, 15)),
    "Hearts": list(range(1, 11)),
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
    clear_print(f"{Text.Fore.Green}-> Current Cards in the deck :\n")
    for suit_display in Suits:
        symbol = suit_display[:2]
        name = suit_display[2:]
        color = Text.Fore.White if get_suit_color(name) == "Black" else Text.Fore.Red
        print(f"{color}    {suit_display}:")
        for rank in suits_cards[name]:
            card_name = rank_to_name(rank)
            print(f"        {card_name} {symbol}", end="")
        print(f"\n{Text.Reset}")


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
        print(f"{Text.Fore.Red}ERROR\t| {rank} of {suit} couldn't be removed.{Text.Reset}")


def start_dungeon():
    refresh_terminal()
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
        return f"{Text.Reset}You have {Text.Fore.Green if health >= 10 else Text.Fore.Red}{health}{Text.Reset} Health."

    def show_stats():
        texts = [f"Health: {Text.Fore.Green}{health} {"▰" * health}{Text.Fore.White}{"▱" * (20 - health)} 20",
                 f"Equipped weapon: {equipped_weapon}",
                 f"Last hit with weapon: {None if last_card_hit_with_weapon == 15 else last_card_hit_with_weapon} {Text.Reset}",
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
                f"\033[{line};{terminal_columns}H{"\b" * len(list(text))}{text}")
            line += 1
        side_bar_width = 20
        cards_help_section_height = 7
        for lines in range(terminal_lines - 1):
            if lines + 1 == cards_help_section_height:
                print(f"\033[{lines+1};{terminal_columns - side_bar_width}H┣")
            else:
                print(f"\033[{lines+1};{terminal_columns - side_bar_width}H┃")
        for columns in range(side_bar_width):
            print(f"\033[{cards_help_section_height};{terminal_columns - side_bar_width + (columns + 1)}H━")

        remaining_cards = len(suits_cards["Spades"]) + len(suits_cards["Clubs"]) + len(suits_cards["Diamonds"]) + len(suits_cards["Hearts"])
        remaining_cards_text = f"Remaining cards: {remaining_cards}"
        print(f"\033[1;{terminal_columns - ( side_bar_width + 1 )}H\033[{len(list(remaining_cards_text))}D{remaining_cards_text}")

        section_start_line = 10
        line = section_start_line
        section_height = terminal_lines - ( section_start_line + 1 )
        if len(cards_played) > 0:
            if len(cards_played) < section_height:
                cards_played.reverse()
                for card in cards_played:
                    print(f"\033[{line};{terminal_columns}H\033[{side_bar_width}D\033[{(side_bar_width - len(list(card.strip())))}C{card.strip()}")
                    line += 1
                cards_played.reverse()
            else:
                cards_played.reverse()
                for i in range(section_height - 1):
                    print(f"\033[{line};{terminal_columns}H\033[{side_bar_width}D\033[{(side_bar_width - len(list(cards_played[i].strip())))}C{cards_played[i].strip()}")
                    line += 1
                print(f"\033[{line};{terminal_columns}H\033[{side_bar_width}D\033[{(side_bar_width - len(list(cards_played[i].strip())))}C . . .")
                cards_played.reverse()

    while 1:
        refresh_terminal()
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
            win_texts = [f"YOU CLEARED THE DUNGEON WITH {Text.Fore.Green}{health}{Text.Reset} HEALTH REMAINING.",
                         "You win !"]
            clear_print(f"\033[{h_center};{w_center}H{"\b" * ( len(list(win_texts[0])) // 2 - 5)}{win_texts[0]}")
            print(f"\033[{h_center + 1};{w_center}H{"\b" * ( len(list(win_texts[1])) // 2)}{win_texts[1]}")
            break

        if new_room:
            clear_print(f"{Text.Fore.Magenta}{"\n" * 5}Room #{room_number}: ")
            new_room = False
        else:
            print(f"{Text.Fore.Magenta}{"\n" * 5}Room #{room_number}: ")
        c = 1
        for card in room_cards:
            print(
                f"{Text.Fore.White if card.split()[-1][0].upper() in ["S", "C"] else Text.Fore.Red}{c}->\t|\t{card}\t\t|\n{Text.Reset}")
            c += 1
        c = 1
        show_stats()
        show_help()
        card_to_play = input(
            f"\033[{terminal_lines};1HWhich card to play: ")
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
                    f"Healed for: {Text.Fore.Green}{played_card_rank}{Text.Reset}. {show_health()}")
        except:
            print(f"{Text.Fore.White + Text.Back.Red}NOT A VALID INPUT{Text.Reset}")

        if health < 1:
            print(f"{Text.Fore.Red}YOU DIED.\n{Text.Reset}")
            input()
            break


def show_help():
    clear()
    print(f"{Text.Fore.Cyan}{Text.Effect.Bold}{'=' * 60}{Text.Reset}")
    print(f"{Text.Fore.Magenta}{Text.Effect.Bold}                  SCOUNDREL - COMPUTER EDITION                  {Text.Reset}")
    print(f"{Text.Fore.Cyan}{Text.Effect.Bold}{'=' * 60}{Text.Reset}")
    print(f"{Text.Fore.Yellow}A solo roguelike card game by Zach Gage & Kurt Bieg{Text.Reset}")
    print(f"{Text.Fore.Yellow}    Python terminal version - Built by Hu-Bo-    {Text.Reset}")
    print()

    input(f"{Text.Fore.Blue}Press Enter for Setup & Deck...{Text.Reset}")

    clear_print(f"{Text.Fore.Green}{Text.Effect.Bold}🎮 SETUP & DECK{Text.Reset}")
    print(f"{Text.Fore.White}The game automatically shuffles a custom deck:{Text.Reset}")
    print()
    print(f"{Text.Fore.Red}{Text.Effect.Bold}♠ Spades & ♣ Clubs (Monsters):{Text.Reset} {Text.Fore.White}1-10, Jack(11), Queen(12), King(13), Ace(14) — {Text.Fore.Red}14 each (28 total){Text.Reset}")
    print(f"{Text.Fore.Yellow}{Text.Effect.Bold}♦ Diamonds (Weapons):{Text.Reset} {Text.Fore.White}1-10 — {Text.Fore.Yellow}10 total{Text.Reset}")
    print(f"{Text.Fore.Green}{Text.Effect.Bold}♥ Hearts (Potions):{Text.Reset} {Text.Fore.White}1-10 — {Text.Fore.Green}10 total{Text.Reset}")
    print()
    print(f"{Text.Fore.Cyan}Starting Health: {Text.Fore.Green}20{Text.Reset} (capped at 20){Text.Fore.Cyan}{Text.Reset}")
    print(f"{Text.Fore.Cyan}Deck total: 48 cards (digital shuffle){Text.Reset}")
    print()

    input(f"{Text.Fore.Blue}Press Enter for Card Types & Effects...{Text.Reset}")

    clear_print(f"{Text.Fore.Green}{Text.Effect.Bold}⚔️  CARD TYPES & EFFECTS{Text.Reset}")
    print(f"{Text.Fore.Red}{Text.Effect.Bold}{'=' * 20} MONSTERS ♠♣ {'=' * 20}{Text.Reset}{Text.Reset}")
    print(f"{Text.Fore.Red}Deal damage = rank value (e.g. 10=10, Jack=11, Ace=14){Text.Reset}")
    print()
    print(f"{Text.Fore.Yellow}{Text.Effect.Bold}{'=' * 18} WEAPONS ♦ {'=' * 18}{Text.Reset}{Text.Reset}")
    print(f"{Text.Fore.Yellow}Equip automatically — replaces old weapon & resets 'monster limit'{Text.Reset}")
    print(f"{Text.Fore.Yellow}Reduces damage from future monsters{Text.Reset}")
    print()
    print(f"{Text.Fore.Green}{Text.Effect.Bold}{'=' * 17} POTIONS ♥ {'=' * 17}{Text.Reset}{Text.Reset}")
    print(f"{Text.Fore.Green}Heal = rank value (stacks all in room!){Text.Reset}")
    print(f"{Text.Fore.Green}Note: Unlike physical rules, {Text.Effect.Bold}ALL potions heal{Text.Reset} — no limit per turn.{Text.Reset}")
    print()

    input(f"{Text.Fore.Blue}Press Enter for Gameplay...{Text.Reset}")

    clear_print(f"{Text.Fore.Green}{Text.Effect.Bold}🕹️  GAMEPLAY{Text.Reset}")
    print(f"{Text.Fore.White}1. Rooms auto-generate: {Text.Effect.Bold}4 cards shown, numbered 1-4{Text.Reset}")
    print(f"{Text.Fore.White}2. Enter number to {Text.Effect.Bold}PLAY (resolve) that card{Text.Reset}{Text.Fore.White}.{Text.Reset}")
    print(f"{Text.Fore.White}3. Room shrinks. When there is only 1 card in the room: {Text.Effect.Bold}adds new cards to fill 4{Text.Reset}")
    print(f"{Text.Fore.White}4. {Text.Effect.Bold}Order matters!{Text.Reset} Play weapons/potions first? Save weak monsters for weapon?{Text.Reset}")
    print()
    print(f"{Text.Fore.Magenta}{Text.Effect.Bold}No 'avoid' rooms in this version — pure dungeon crawl!{Text.Reset}")
    print()

    input(f"{Text.Fore.Blue}Press Enter for Monster Fighting...{Text.Reset}")

    clear_print(f"{Text.Fore.Red}{Text.Effect.Bold}👹 MONSTER FIGHTING DETAILS{Text.Reset}")
    print(f"{Text.Fore.White}When playing ♠/♣:{Text.Reset}")
    print()
    print(f"{Text.Fore.Cyan}• {Text.Effect.Bold}No weapon or monster rank highter than last monster defeated with weapon?{Text.Reset} {Text.Fore.Red}Full damage!{Text.Reset}")
    print(
        f"{Text.Fore.Cyan}• {Text.Effect.Bold}Weapon equipped AND rank lower than last defeated monster?{Text.Reset} Damage = {Text.Fore.Red}[monster rank] - [weapon] -> if <0 it will {Text.Effect.Bold}NOT{Text.Reset} Heal you. it just won't do damage{Text.Reset}")
    print(f"{Text.Fore.Cyan}  → Updates 'last defeated' to this monster's rank{Text.Reset}")
    print()
    print(f"{Text.Fore.Yellow}New weapon always resets 'last defeated' to high (15){Text.Reset}")
    print()
    print(f"{Text.Fore.Red}{Text.Effect.Bold}EXAMPLE:{Text.Reset}")
    print(f"{Text.Fore.White}Equip 5♦ → Can fight any monster first time.{Text.Reset}")
    print(f"{Text.Fore.Red}Play 3♠: 3 < 15 → dmg = max(0,3-5)=0, last=3{Text.Reset}")
    print(f"{Text.Fore.Red}Play Jack♠ (11): 11 ≮ 3 → full 11 dmg{Text.Reset}")
    print(f"{Text.Fore.Red}Play 2♠: 2 < 3 → dmg = max(0, 2-5) = 0, last=2{Text.Reset}")
    print()
    print(f"{Text.Fore.Yellow}Note: Strict {Text.Effect.Bold}'<'{Text.Reset} — can't repeat exact rank!{Text.Reset}")

    input(f"{Text.Fore.Blue}Press Enter for Win/Lose...{Text.Reset}")

    clear_print(f"{Text.Fore.Green}{Text.Effect.Bold}🏆 WIN & LOSE{Text.Reset}")
    print(f"{Text.Fore.Green}{Text.Effect.Bold}WIN:{Text.Reset} Clear deck (≤2 cards left) with room <2 → {Text.Fore.Green}'Cleared with X health!'{Text.Reset}")
    print()
    print(f"{Text.Fore.Red}{Text.Effect.Bold}LOSE:{Text.Reset} Health <1 → {Text.Fore.Red}'YOU DIED'{Text.Reset}")
    print()
    print(f"{Text.Fore.Cyan}Score = remaining health (no negative/monster sum in this version){Text.Reset}")
    print()
    print(f"{Text.Fore.Yellow}{Text.Effect.Bold}TIPS:{Text.Reset}")
    print(f"{Text.Fore.White}• Use {Text.Effect.Bold}option 2/3/4{Text.Reset} to edit deck & practice!{Text.Reset}")
    print(f"{Text.Fore.White}• {Text.Effect.Bold}DEBUG{Text.Reset} info shown during play (rank/suit types){Text.Reset}")
    print(f"{Text.Fore.White}• Search '{Text.Effect.Bold}How to play Scoundrel Card Game{Text.Reset}' for original physical rules!{Text.Reset}")
    print()

    input(f"{Text.Fore.Blue}Press Enter to return...{Text.Reset}")


# MAIN MENU
while 1:
    # REMINDER
    clear_print(
        f"\033[{h_center};{w_center}H{"\b" * (len(list(" Please go Fullscreen "))//2)}{Text.Back.Yellow}{Text.Fore.Black} Please go Fullscreen {Text.Reset}")
    print(f"\033[{h_center+1};{w_center}H{"\b" * (len(list(f" Starting in {time_to_start} Seconds! "))//2)}{Text.Back.Magenta} Starting in \033[s{time_to_start} Seconds! {Text.Reset}")
    while time_to_start > -1:
        h_center = terminal_lines // 2
        w_center = terminal_columns // 2
        sleep(1)
        print(f"\033[u{time_to_start}")
        time_to_start -= 1
    print(Text.Reset)
    # AVAILABLE OPTIONS
    clear_print(
        f"{Text.Fore.Black}{Text.Back.Cyan} Choose One of the options: \n{Text.Reset}")
    print(f"{Text.Fore.Green}1. {Text.Fore.White}Start the Dungeon\n"
          f"{Text.Fore.Green}2. {Text.Fore.White}Remove cards\n"
          f"{Text.Fore.Green}3. {Text.Fore.White}Show current cards\n"
          f"{Text.Fore.Green}4. {Text.Fore.White}Reset Deck to default\n"
          f"{Text.Fore.Green}5. {Text.Fore.White}How to Play\n"
          f"{Text.Fore.Red}X. {Text.Fore.White}Quit")

    op = input(f"\n{Text.Fore.Magenta}--> {Text.Fore.White}").upper()

    # OPTION CHOSEN
    if op == "1":
        start_dungeon()

        # STAY IN THE DUNGEON
        input(f"\033[{terminal_lines};{terminal_columns // 2 - len(list(" Press Enter to go to the main menu . . . ")) // 2}H{Text.Back.Blue}{Text.Fore.White} Press Enter to go to the main menu . . . {Text.Reset}")

    elif op == "2":
        while 1:
            show_current_cards()

            suit_to_remove = None
            rank_to_remove = None
            canceled = False
            print(
                f"{Text.Fore.Magenta}ENTER X TO CANCEL\n{Text.Fore.Blue}Remove a card: Select card suit [S,C,H,D]:\t{Text.Reset}", end="")
            while 1:
                suit_to_remove = input().upper()

                if suit_to_remove == "X":
                    canceled = True
                    break
                elif suit_to_remove not in ["S", "C", "H", "D"]:
                    print(
                        f"{Text.Fore.Red}NOT A VALID SUIT \t| {Text.Fore.Blue}Select card suit [S,C,H,D]:\t{Text.Reset}", end="")
                else:
                    break

            if not canceled:
                print(
                    f"{Text.Fore.Blue}Select card rank [1-14]:\t\t{Text.Reset}", end="")
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
                                f"{Text.Fore.Red}NOT IN RANGE: {Text.Fore.Blue}Select card rank [1-14]:\t{Text.Reset}", end="")
                    except ValueError:
                        print(
                            f"{Text.Fore.Red}NOT A NUMBER: {Text.Fore.Blue}Select card rank [1-14]:\t{Text.Reset}", end="")

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
                        f"{Text.Effect.Bold + Text.Fore.Yellow}The card [{rank_to_remove} of {suit_to_remove}] Removed . . .{Text.Reset}")
                    input(f"{Text.Fore.Blue}Press enter to continue . . .{Text.Reset}")
                else:
                    canceled = True

            if canceled:
                break

    elif op == "3":
        show_current_cards()
        input(f"{Text.Fore.Blue}Press Enter to go to the main menu . . .{Text.Reset}")

    elif op == "4":
        reset_deck()
        clear_print(
            f"{Text.Fore.Green}OK\t| DECK RESET . . .{Text.Reset}\n\nPress enter to go back to the main menu . . .")
        input()

    elif op == "5":
        show_help()

    elif op == "X":
        clear_print(f"{Text.Fore.Red}- - - Quitted - - -{Text.Reset}")
        break

    else:
        op2 = input(
            f"{Text.Fore.Red}\n\tERROR\t| NOT A VALID OPTION. PRESS ENTER TO TRY AGAIN OR X TO QUIT: {Text.Reset}").upper()
        if op2 == "X":
            clear_print(f"{Text.Fore.Red}- - - Quitted - - -{Text.Reset}")
            break
