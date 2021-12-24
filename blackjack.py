import art
import random

def choose_card():
 
 chosen_card=random.randint(0,12)
 return chosen_card

def calculate_value(chosen_card):

    if chosen_card==0:
        value=11

    elif chosen_card==1:
        value=2

    elif chosen_card==2:
        value=3

    elif chosen_card==3:
        value=4

    elif chosen_card==4:
        value=5

    elif chosen_card==5:
        value=6

    elif chosen_card==6:
        value=7

    elif chosen_card==7:
        value=8

    elif chosen_card==8:
        value=9

    elif chosen_card==9:
        value=10

    elif chosen_card==10:
        value=10

    elif chosen_card==11:
        value=10

    elif chosen_card==12:
        value=10

    return value

def dealer_cards():
   
    dealer_hand=[]
    dealer_hand.append(choose_card())
    dealer_hand.append(choose_card())
    # dealer_val=calculate_value(dealer_hand[0])+calculate_value(dealer_hand[1])
    # print(dealer_val)
    return dealer_hand

def player_cards():
    
    player_hand=[]
    # print("\nYour cards are: ")
    player_hand.append(choose_card())
    player_hand.append(choose_card())
    # print(art.cards[player_hand[0]],art.cards[player_hand[1]])
    # 
    # print(player_val)
    return player_hand

def calculate_score(cards):
    
    score=0
    for card in cards:
        score+=calculate_value(card)

    return score

def who_won(dealer_hand,player_hand,dealer_bust,player_bust):
    
    if dealer_hand==player_hand:
        print("\nIt's a draw!")

    elif dealer_bust==True:
        print("\nIt's a bust. You win! \nCONGRATULATIONS <3")

    elif player_bust==True:
        print("\nIt's a bust. You lost :(")
            
    elif dealer_hand<player_hand and player_bust==False:
        print("\nYou won! ")
            
    elif dealer_hand>player_hand and dealer_bust==False:
        print("\nYou lost :(")

def dealer_deal(cards):
    
    print("\n The dealer's cards are: ")
    for card in cards:
        print(art.cards[card])
    
    dealer_hand=calculate_score(cards)
    while dealer_hand<=16:
        dealer_new_card=choose_card()
        print(art.cards[dealer_new_card])
        dealer_hand+=calculate_value(dealer_new_card)
        print(f"\nDealer Current Value is: {dealer_hand}")
        
    return dealer_hand

def is_bust(score):
    bust=False
    if score>21:
        bust=True
    return bust