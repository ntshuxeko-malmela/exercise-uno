import random
from player import can_play
from uno_utils import CYAN, RESET, colors

#   Check if a computer can play. Returns the card played or None if the computer had to draw.
def computer_play(discard_pile, computer_hand, player_number):
    print(CYAN + f"\nComputer {player_number}'s Turn..." + RESET)
    
    for index, card in enumerate(computer_hand):
        if can_play(discard_pile[-1], [card]):
            print(f"Computer {player_number} plays: {card}")
            return computer_hand.pop(index)
    
    print(f"Computer {player_number} cannot play, drawing a card...")
    return None

#   choose a random color for Wild or Draw Four cards.
def choose_color():
    new_color = random.choice(colors)
    print(f"Computer chooses color: {new_color}")
    return new_color
