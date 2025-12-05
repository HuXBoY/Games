# FOR ALL THE DEPRECATED OR TEST/DEBUG CODE
# I SAVE THEM HERE TO NOT HAVE THEM COMMENTED IN MY MAIN CODE OR DELETE THEM
# SOME OF THEM MAY NOT EVEN MAKE SENSE BECAUSE OF DELETED FUCNTIONS OR THINGS JUST DIDNT GO AS PLANNED
# SO... DO NOT TRY TO RUN THIS FILE AS IT WILL JUST NOT WORK


# TEST | GETTING RANDOM CARDS
values = []
for suit in suits_cards.keys():
    for value in suits_cards[suit]:
        values.append(value)
removed_cards = []
while 1:
    clear_print(f.BLUE + "ALL CARDS ( WITHOUT SUIT ) -> " +
                f.WHITE + str(values))
    print(f.BLUE + "REMOVED CARDS -> " +
          f.WHITE + "\t" + str(len(removed_cards)))
    print(f.BLUE + "NUMBER OF VALUES -> " + f.WHITE + "\t" + str(len(values)))
    print("\n\n")
    if len(removed_cards) == len(values):
        input(
            f"{f.RED}no more Cards . . . press enter to go the main menu .{s.RESET_ALL}")
        break
    suit = random.choice(list(suits_cards.keys()))
    while len(suits_cards[suit]) < 1:
        suit = random.choice(list(suits_cards.keys()))
    rank = random.choice(suits_cards[suit])

    ####### DEBUG STUFF #######
    # print(f.BLUE + "Suit: " + suit + "\nType: " +
    #       str(type(suit)))
    # print(f.CYAN + "\nRank: " + str(rank) + "\nType: " +
    #       str(type(suits_cards[suit])))
    ###########################

    suits_cards[suit].remove(rank)
    removed_cards.append(str(rank)+" "+str(suit))
    print(f"{f.GREEN}\n{rank}\tof\t{suit}\t| {f.RED}REMOVED {len(removed_cards)}:\t{removed_cards}\n\n{f.YELLOW}Current Cards:\n\t {suits_cards}{s.RESET_ALL}")
    # suits_cards[suit].remove(rank)
    # show_current_cards()
    input()


# TRY | GET ROOM CARDS
def get_room_cards(amount):
    cards = []
    for i in range(amount):
        suit, rank = get_random_card()
        cards.append
    suits_cards[suit]
    return cards


# OLD | GET RANDOM CARDS ON THE ARRAY THING AT THE VERY BEGINNING OF PROJECT
def get_random_card():
    rand_suit_choice = random.choice(Suits)
    suit_symbol = rand_suit_choice[:2]
    suit_name = rand_suit_choice[2:]

    rank = random.choice(suits_cards[suit_name])
    return f"{rank} {suit_symbol}"
