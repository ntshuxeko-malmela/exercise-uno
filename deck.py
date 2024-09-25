import random

# set colors
colors = ["Red", "Green", "Blue", "Yellow"]

def get_deck():
    deck = []
    for color in colors:
        for number in range(10):
            deck.append([color, number]) # add a colored number card
            if number != 0:
                deck.append([color, number]) # add another one to double the cards
    
    # add special cards
    for color in colors:
        deck.extend([[color, "Skip"], [color, "Reverse"], [color, "Draw Two"]] * 2)
    
    # add Wild cards
    for _ in range(4):
        deck.append(["Wild", "Wild"])
        deck.append(["Wild", "Draw Four"])

    return deck

# shauffle the deck
def shuffle_deck(deck):
    for card_position in range(len(deck)):
        random_position = random.randint(0, len(deck) - 1)
        deck[card_position], deck[random_position] = deck[random_position], deck[card_position]
    
    return deck

# draw cards for a specified number e.g. 7 cards
def draw_cards(deck, number_of_cards):
    return [deck.pop(0) for _ in range(number_of_cards)]
