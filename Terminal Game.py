import random

#Betting chips

class Cards:
    def __init__(self, suits, card_symbols, card_values):
        self.suits = suits
        self.card_symbols = card_symbols
        self.card_values = card_values
    
    def __repr__(self):
        return f"{self.suits}{self.card_symbols}"

suits = ["Spades", "Hearts","Clubs", "Diamonds"]
suits_symbols = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
card_symbols = ["A", "2", "3", "4", "5", "6", "7", "8", "9","10", "J", "Q", "K"] 
card_values = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,"10":10, "J":10, "Q":10, "K":10}


deck = []
for suit in suits:
    for card in card_symbols:
        deck.append(Cards(suits_symbols[suit], card, card_values[card]))
random.shuffle(deck)

def reset_deck():
    global deck
    deck =[]
    if len(deck) <52:
        for suit in suits:
            for card in card_symbols:
                deck.append(Cards(suits_symbols[suit], card, card_values[card]))
        random.shuffle(deck)
        return deck

#print(deck)

class Player:
    def __init__(self, name, age, bank):
        self.name = name
        self.age = age
        self.bank = bank
        self.hand = []
        self.score = 0

    def hit(self, card):
        self.hand.append(card)
        print("...\nYou have drawn a card")
        if card.card_symbols == "A":
            print("It's an ACE!")
            while True:
                value = int(input(f"Choose value for the Ace (1 or 11): "))
                if value == 1 or value == 11:
                    break
                else:
                    print("Invalid value, please choose 1 or 11 only")
        else:
            value = card_values[card.card_symbols]
        self.score += value
        return value

    #def double_down():
    #def split():
    #def surrender():

class Dealer():
    def __init__(self):
        self.hand = []
        self.score = 0

    def hit(self, card):
        self.hand.append(card)
        print("...\nDealer is hitting the card...\n")
        if card.card_symbols == "A":
            print("It's an ACE!")
            while True:
                value = int(input(f"Choose value for the Ace (1 or 11): "))
                if value == 1 or value == 11:
                    break
                else:
                    print("Invalid value, please choose 1 or 11 only")
        else:
            value = card_values[card.card_symbols]
        self.score += value
        return value



#In-game settings
print("Welcome to BlakJack Casino ~!")
player_name = input("Please enter your name: ")
player_age = input("Please enter your age: ")
player_bank = input("Please enter your starting amount: $")
player = Player(player_name, player_age, player_bank)
dealer = Dealer()

player_score = player.score
dealer_score = dealer.score
player_hand = player.hand
dealer_hand = dealer.hand

#Rules:
while True:
    # reset game variables
    player_score = 0
    dealer_score = 0
    player.hand.clear()
    dealer.hand.clear()
    in_game_deck = reset_deck()

    # deal initial hands
    print(f"...\n...\n...\nThe table is drawing cards:\n")
    for gamestart in range(2):
        player_hand.append(in_game_deck.pop())
        dealer_hand.append(in_game_deck.pop())

    # print initial hands and scores
    print("Player's Hand:")
    print(player_hand)
    for card in player_hand:
        player_score += card_values[card.card_symbols]
    print("Your score: ", player_score)

    print("\nDealer's Hand:")
    print(f'({dealer_hand[0]}, ?)')
    for card in dealer_hand:
        dealer_score += card_values[card.card_symbols]
    print("Dealer score:", card_values[dealer_hand[0].card_symbols])
    print("")

    # player's turn
    while player_score < 21:
        ans = input("Do you wanna Hit or Stand?\n")
        if ans in ["Hit", "hit", "H", "h"]:
            hit = player.hit(in_game_deck.pop())
            player_score += hit
            print("Your hand:")
            print(player_hand)
            print(player_score)
        elif ans in ["Stand", "stand", "S", "s"]:
            break

    # check for player win/loss/bust
    if player_score == 21:
        ans = input('You have won! Do you wanna play again? Y/N \n')
        if ans == "Y" or ans =="y":
            continue   
        elif ans == "N" or ans =="n":
            print ("Thanks for playing, have a nice day!")
            break
        else:
            print ("Please only answer with Y / N")
    elif player_score >21:
        ans = input('You were busted! Do you wanna play again? Y/N \n')
        if ans == "Y" or ans =="y":
            continue
        elif ans == "N" or ans =="n":
            print ("Thanks for playinng, have a nice day!")
            break
        else:
            print ("Please only answer with Y / N")
    else:
        # dealer's turn
        print("\nDealer's Hand:")
        print(dealer_hand)
        print(dealer_score)

        while dealer_score < 17:
            dealer_hit = dealer.hit(in_game_deck.pop())
            dealer_score += dealer_hit
            print("Dealer's Hand:")
            print(dealer_hand)
            print("Dealer Score: ", dealer_score)

        # check for dealer win/loss/bust
        if dealer_score > 21:
            print("Dealer is busted! You win!")
        elif dealer_score == 21 or dealer_score > player_score:
            print("Dealer wins!")
        elif dealer_score < player_score:
            print("You win!")
        else:
            print("It's a tie!")

        ans = input('Do you wanna play again? Y/N \n')
        if ans == "Y" or ans == "y":
            continue
        elif ans == "N" or ans == "n":
            print ("Thanks for playing, have a nice day!")
            break
        else:
            print ("Please only answer with Y / N")

    