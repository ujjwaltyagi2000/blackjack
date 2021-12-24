import random
import art
import blackjack

dealer_hand,dealer_card1,dealer_card2=blackjack.dealer_cards()
# print(dealer_hand,dealer_card1,dealer_card2)
player_hand=blackjack.player_cards()

game_over=False

while game_over!=True:

    print(f"\nYour current value is: {player_hand}")
    
    if player_hand==21:
        print("It's a blackjack! ")
        blackjack.dealer_deal(dealer_hand,dealer_card1,dealer_card2)
        
        blackjack.who_won(dealer_hand,player_hand)
        game_over=True
        
            
    repeat=True

    while repeat==True:

        player_choice=input("\nDo you want another card? Type 'hit' or 'stand': ").lower()

        if player_choice=='hit':
        
            player_new_card=blackjack.choose_card()
            print(f"\nYour new card is: {art.cards[player_new_card]}")
            player_hand+=blackjack.calculate_value(player_new_card)
            print(player_hand)


        elif player_choice=='stand':

            repeat=False
            dealer_hand=blackjack.dealer_deal(dealer_hand,dealer_card1,dealer_card2)
            print(dealer_hand)
            blackjack.who_won(dealer_hand,player_hand)
            game_over=True

