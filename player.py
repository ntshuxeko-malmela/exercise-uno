from deck import colors
from uno_utils import BLUE, RESET

# show player cards
def player_cards(player, player_hand):
    print(f"\nPlayer {player + 1}'s Hand.")
    print("---------------------------------")
    for index, card in enumerate(player_hand, start=1):
        print(BLUE + f"{index}. {card}" + RESET)
    print("---------------------------------")

# check if a player can play and return True or False
def can_play(discard_card, player_hand):
    for card in player_hand:
        if "Wild" in card or discard_card[0] == card[0] or discard_card[1] == card[1]:
            return True
    return False
