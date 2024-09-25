import random
from deck import get_deck, shuffle_deck, draw_cards
from player import player_cards, can_play
from uno_utils import MAGENTA, CYAN, GREEN, RED, RESET, colors
from computer import computer_play, choose_color  # Importing computer logic

def main():
    uno_deck = get_deck()
    uno_deck = shuffle_deck(uno_deck) # get a shuffled deck

    discard_pile = []
    players = []
    is_computer_player = []

    print(MAGENTA + f"-------- WELCOME TO THE UNO GAME --------\n" + RESET)
    number_of_players = int(input(GREEN + f"Enter number of players (2-10): " + RESET))

    while number_of_players < 2 or number_of_players > 10:
        number_of_players = int(input(RED + f"Invalid: Please enter number of players (2-10): " + RESET))

    # Ask if each player is a human or a computer
    for player in range(number_of_players):
        if input(f"Is player {player + 1} a computer (yes/no)?: ").lower() == "yes":
            is_computer_player.append(True)
        else:
            is_computer_player.append(False)

        players.append(draw_cards(uno_deck, 7))

    discard_pile.append(uno_deck.pop(0))  # Start the discard pile
    player_turn = 0
    play_direction = 1
    is_playing = True

    while is_playing:
        print(MAGENTA + f"\nDiscard Pile top card: {discard_pile[-1]}" + RESET)

        # If current player is a computer
        if is_computer_player[player_turn]:
            computer_hand = players[player_turn]
            computer_card = computer_play(discard_pile, computer_hand, player_turn + 1)

            if computer_card:
                discard_pile.append(computer_card)
            else:
                computer_hand.extend(draw_cards(uno_deck, 1))
        else:
            # Human player's turn
            player_cards(player_turn, players[player_turn])

            if can_play(discard_pile[-1], players[player_turn]):
                option = int(input("Which card do you want to play?: "))   
                while option < 1 or option > len(players[player_turn]):
                    option = int(input(RED + f"Invalid card! Which card do you want to play?: " + RESET))

                while not can_play(discard_pile[-1], [players[player_turn][option - 1]]):
                    option = int(input(RED + f"Invalid card! Which card do you want to play?: " + RESET))

                discard_pile.append(players[player_turn].pop(option - 1))
            else:
                print(RED + f"You cannot play any card. You need to draw a card." + RESET)
                players[player_turn].extend(draw_cards(uno_deck, 1))

        # Check if the player has won
        if len(players[player_turn]) == 0:
            if is_computer_player[player_turn]:
                print(GREEN + f"\nUNO! Computer {player_turn + 1} is the WINNER!" + RESET)
            else:
                print(GREEN + f"\nUNO! Player {player_turn + 1} is the WINNER!" + RESET)
            print(RED + f"Game Over!" + RESET)
            break

        # check for special cards played (Skip, Reverse, Draw Two, etc.)
        if len(discard_pile) > 0:
            current_card_value = discard_pile[-1][1]
            current_card_color = discard_pile[-1][0]

            # choosing the color after playing Wild or Draw Four card
            if current_card_color == "Wild" and (current_card_value == "Wild" or current_card_value == "Draw Four"):
                if is_computer_player[player_turn]:
                    new_color = choose_color()  # Computer chooses a color
                else:
                    for index, color in enumerate(colors):
                        print(f"{index + 1}. {color}")
                    new_color = int(input("Which color would you like to choose?: "))
                    while new_color < 1 or new_color > 4:
                        new_color = int(input(RED + f"Invalid selection! Please choose a color (1-4): " + RESET))

                    new_color = colors[new_color - 1]  # Convert selection to the color name

                discard_pile[-1][0] = new_color  # Apply the chosen color to the discard pile
                print(f"Discard Pile top card: {discard_pile[-1]}")


            # get special cards (Reverse, Skip, Draw Two, Draw Four)
            current_card_value = discard_pile[-1][1]
            current_card_color = discard_pile[-1][0]

            if current_card_value == "Reverse":
                play_direction *= -1

            elif current_card_value == "Skip":
                # Skip the next player
                player_turn = (player_turn + play_direction) % number_of_players

            elif current_card_value == "Draw Two":
                # Move to the next player and make them draw 2 cards
                player_turn = (player_turn + play_direction) % number_of_players
                players[player_turn].extend(draw_cards(uno_deck, 2))

            elif current_card_value == "Draw Four":
                # Move to the next player and make them draw 4 cards
                player_turn = (player_turn + play_direction) % number_of_players
                players[player_turn].extend(draw_cards(uno_deck, 4))


        # Change player turn
        player_turn += play_direction
        if player_turn >= number_of_players:
            player_turn = 0
        elif player_turn < 0:
            player_turn = number_of_players - 1

if __name__ == "__main__":
    main()
