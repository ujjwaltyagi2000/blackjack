import random
import art
import blackjack

print(art.logo)
#Dealer's card generated and one card printed
dealer_cards=blackjack.dealer_cards()
print("\nThe dealer's cards are: ")
print(art.cards[dealer_cards[0]])
dealer_score=blackjack.calculate_score(dealer_cards)

#Player's card generated and both cards printed
player_cards=blackjack.player_cards()
print("\nThe player's cards are: ")
print(art.cards[player_cards[0]])
print(art.cards[player_cards[1]])
player_score=blackjack.calculate_score(player_cards)


# game_over=False
repeat=True
dealer_bust=False
player_bust=False

print(f"\nYour current value is: {player_score}")

if player_score==21:
    print("It's a blackjack! ")
    dealer_score=blackjack.dealer_deal(dealer_cards)
    
    blackjack.who_won(dealer_score,player_score,dealer_bust,player_bust)

while repeat==True:

    player_choice=input("\nDo you want another card? Type 'hit' or 'stand': ").lower()

    if player_choice=='hit':
    
        player_new_card=blackjack.choose_card()
        player_cards.append(player_new_card)
        print(f"\nYour new card is: {art.cards[player_new_card]}")
        player_score+=blackjack.calculate_value(player_new_card)
        print(player_score)
        player_bust=blackjack.is_bust(player_score)
        if player_bust:
            print("It's a bust, You lost :(")
            repeat=False
        
        if player_score==21:
            print("It's a blackjack! ")
            dealer_score=blackjack.dealer_deal(dealer_cards)
            dealer_bust=blackjack.is_bust(dealer_score)
            blackjack.who_won(dealer_score,player_score,dealer_bust,player_bust)
           
            repeat=False

    elif player_choice=='stand':

        repeat=False
        dealer_score=blackjack.dealer_deal(dealer_cards)
        dealer_bust=blackjack.is_bust(dealer_score)
        blackjack.who_won(dealer_score,player_score,dealer_bust,player_bust)
        

