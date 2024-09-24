import random

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'  # Reset color to default

colors = ["Red", "Green", "Blue", "Yellow"]     # list of colors in a deck

def get_deck():
    deck = []

    # adding numbers (0-9) for each card color
    for color in colors:
        for number in range(10):
            deck.append([color, number])  # add a card of [color, value]
            if number != 0:
                deck.append([color, number])  # add a card of [color, value]
    
    # adding special cards (Skip, Reverse, Draw Two) for each color card
    for color in colors:
        deck.extend([[color, "Skip"], [color, "Reverse"], [color, "Draw Two"]] * 2)
    
    # addding wild and wild draw four cards
    for number in range(4):
        deck.append(["Wild", "Wild"])
        deck.append(["Wild", "Draw Four"])

    return deck

# function to shuffle the cards in the deck
def shuffle_deck(deck):
    for card_position in range(len(deck)):
        random_position = random.randint(0, 107)    # generate a random number
        deck[card_position], deck[random_position] = deck[random_position], deck[card_position] #swap positions
    
    return deck

# function to draw cards from the deck
def draw_cards(number_of_cards):
    cards_drawn = []
    for number in range(number_of_cards):
        cards_drawn.append(uno_deck.pop(0))
    
    return cards_drawn

# function to show the player's cards
def player_cards(player, player_hand):
    print(f"Player {player + 1}'s Hand.")
    print("---------------------------------")
    
    index = 1
    for card in player_hand:
        print(BLUE + f"{index}. {card}" + RESET)
        index += 1
    print("---------------------------------")
 
 # function to check if a player can play
'''
    Revisit the while logic
'''
def can_play(discard_card, player_hand):
    for card in player_hand:
        if "Wild" in card: 
            return True
        elif discard_card[0] == card[0] or discard_card[1] == card[1]:
            return True
    
    return False   
 
 # function to check if a player can play

# calling the functions
uno_deck = get_deck()      # generate the deck

discard_pile = []

#print("NORMAL DECK")
#print(BLUE + f"{uno_deck}" + RESET)         # print each card in a deck

uno_deck = shuffle_deck(uno_deck)      # shuffle the cards in the deck

#print("\nSHUFFLED DECK")    
#print(GREEN + f"{uno_deck}" + RESET)          # print each card in a deck
    
players = []
number_of_players = int(input("Enter number of players (2-10): "))

while number_of_players < 2 or number_of_players > 10:
    number_of_players = int(input("Invalid: Please enter number of players (2-10): "))

for number in range(number_of_players):
    players.append(draw_cards(5))   

player_turn = 0
play_direction = 1
discard_pile.append(uno_deck.pop(0))
is_playing = True

while is_playing:
    
    player_cards(player_turn, players[player_turn])
    print(f"Discard Pile top card: {discard_pile[-1]}")
    
    if can_play(discard_pile[-1], players[player_turn]):
        option = int(input("Which card to you want to play?: "))        
        while not can_play(discard_pile[-1], [players[player_turn][option - 1]]):
            option = int(input("Invalid card! Which card to you want to play?: "))
            
        discard_pile.append(players[player_turn].pop(option - 1))
        
         # check for special cards
        current_card_value = discard_pile[-1][1]
        current_card_color = discard_pile[-1][0]
        
        if current_card_color == "Wild" and (current_card_value == "Wild" or current_card_value == "Draw Four"):
            for index in range(len(colors)):
                print(f"{index + 1}. {colors[index]}")
            new_card_color = int(input("Which color would you like to choose?: "))
            while new_card_color < 0 or new_card_color > 4:
                new_card_color = int(input("Invalid card! Which color would you like to choose?: "))
            
            discard_pile[-1][0] = colors[new_card_color - 1] # Change ["Wild", "Wild"] card to ["Any_Color", "Wild"]
        
        # check for special cards
        if current_card_value == "Reverse":
            play_direction = play_direction * -1
        elif current_card_value == "Skip":
            player_turn += play_direction
            if player_turn >= number_of_players:
                player_turn = 0
            elif player_turn < 0:
                player_turn = number_of_players - 1
        elif current_card_value == "Draw Two":
            player_draw = player_turn + play_direction
            if player_draw >= number_of_players:
                player_draw = 0
            elif player_draw < 0:
                player_draw = number_of_players - 1
            players[player_draw].extend(draw_cards(2))
        elif current_card_value == "Draw Four":
            player_draw = player_turn + play_direction
            if player_draw >= number_of_players:
                player_draw = 0
            elif player_draw < 0:
                player_draw = number_of_players - 1
            players[player_draw].extend(draw_cards(4))
        
        print("")
    else:
        print("You cannot play any card. You need to draw a card.")
        players[player_turn].extend(draw_cards(1))
    
    # check for a winner
    if len(players[player_turn]) == 0:
        print(GREEN + f"UNO! Player {player_turn + 1} is a WINNER!" + RESET)
        print(RED + f"Game Over!" + RESET)
        break
    
    # change player turn
    player_turn += play_direction
    if player_turn >= number_of_players:
        player_turn = 0
    elif player_turn < 0:
        player_turn = number_of_players - 1
    
    print("")    
    #print(players[player_turn])
    
