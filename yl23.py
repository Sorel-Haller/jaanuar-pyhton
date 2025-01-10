import random

# Define card values
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

# Create a deck of cards
def create_deck():
    deck = []
    for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
        for rank in card_values:
            deck.append(f"{rank} of {suit}")
    random.shuffle(deck)
    return deck

# Deal a card
def deal_card(deck):
    return deck.pop()

# Calculate hand value
def calculate_hand_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        rank = card.split(' ')[0]  # Get the rank of the card
        value += card_values[rank]
        if rank == 'A':
            ace_count += 1
    # Adjust for Aces if value is over 21
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value

# Display hand
def display_hand(name, hand):
    print(f"{name}'s hand: {', '.join(hand)} (value: {calculate_hand_value(hand)})")

# Main game logic
def play_blackjack():
    print("Welcome to Blackjack!")

    # Create a deck and deal initial cards
    deck = create_deck()
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Player's turn
    while True:
        display_hand("Player", player_hand)
        player_value = calculate_hand_value(player_hand)

        if player_value > 21:
            print("Player busts! Dealer wins!")
            return
        elif player_value == 21:
            print("Player has Blackjack!")
            break

        action = input("Do you want to [H]it or [S]tand? ").lower()
        if action == 'h':
            player_hand.append(deal_card(deck))
        elif action == 's':
            break

    # Dealer's turn
    while True:
        display_hand("Dealer", dealer_hand)
        dealer_value = calculate_hand_value(dealer_hand)

        if dealer_value > 21:
            print("Dealer busts! Player wins!")
            return
        elif dealer_value >= 17:
            break
        else:
            dealer_hand.append(deal_card(deck))

    # Final comparison
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value > dealer_value:
        print("Player wins!")
    elif dealer_value > player_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == '__main__':
    play_blackjack()