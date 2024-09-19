def get_deck():
    colors = ["red", "green", "blue", "yellow"]     # list of colors in a deck
    deck = []

    # adding numbers (0-9) for each card color
    for color in colors:
        for number in range(10):
            deck.append([color, number])  # add a card of [color, value]
    
    # adding special cards (Skip, Reverse, Draw Two) for each color card
    for color in colors:
        deck.extend([[color, "skip"], [color, "reverse"], [color, "draw two"]])
    
    # addding wild and wild draw four cards
    deck.append(["wild", "wild"])
    deck.append(["wild", "draw four"])

    return deck


# call the get_deck() function to initalize the deck
uno_deck = get_deck() * 2       # doubling the deck size to make it 108 cards

for card in uno_deck:
    print(card)         # print each card in a deck
