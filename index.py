import random
import art
import blackjack

dealer_hand=blackjack.dealer_cards()
player_hand=blackjack.player_cards()

print(f"\nYour current value is: {player_hand}")
player_choice=input("\nDo you want another card? Type 'hit' or 'stand': ").lower()

if player_choice=='hit':
    new_card=blackjack.choose_card()
    print(f"\nYour new card is: {art.cards[new_card]}")
    player_hand+=blackjack.calculate_value(new_card)
    print(player_hand)


