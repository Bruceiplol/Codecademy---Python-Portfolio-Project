import random


#Design Cards
#suits = ["Spades", "Hearts","Clubs", "Diamonds"]]
suits = ["\u2664", "\u2661","\u2667", "\u2662"]
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9","10", "J", "Q", "K"] 
card_values = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,"10":10, "J":10, "Q":10, "K":10, "0":10}

#Design Deck
deck=[]
for suit in suits:
    for card in cards:
        deck.append(suit + card)
random.shuffle(deck)

#deck reset function
def reset_deck():
    global deck
    deck=[]
    for suit in suits:
        for card in cards:
            deck.append(suit + card)
    random.shuffle(deck)

#Design Player
class Player:
    def __init__(self, name, age, bank):
        self.name = name
        self.age = age
        self.bank = bank
        self.bet_amount = 0
        self.hand = []
        self.score = 0
        self.has_ace = False
        self.has_split_ace = False
        self.split_hand = []
        self.split_value = 0
        self.is_surrender = False
        self.double_amount = 0
        self.first_ace = False
        self.split_first_ace = False
        self.is_split = False
    
    def reset(self):
        self.hand = []
        self.score = 0
        self.has_ace = False
        self.has_split_ace = False
        self.split_hand = []
        self.split_score = 0
        self.is_surrender = False
        self.double_amount = 0
        self.first_ace = False
        self.split_first_ace = False
        self.is_split = False
    
    def show_hand_1(self):
        print(f"{self.name}'s Hand:")
        print(self.hand)
        self.score = card_values[self.hand[0][-1]] + card_values[self.hand[1][-1]]
        print (f"{self.name}'s score: {self.score}")
    
    
    def show_hand_2(self):
        print(f"{self.name}'s Hand:")
        print(self.hand)
        print(f"{self.name} score:", self.score)
        
    
    def hit(self, card):
        self.hand.append(card)
        print("...\n(You have drawn a card)")
        self.score += card_values[card[-1]]
        if card[-1] == 'A' and card_values[card[-1]]==11:
            self.has_ace = True
        while self.score > 21 and self.has_ace:
            self.score -= 10
            self.has_ace = False
    
    def split_hit(self, card):
        self.split_hand.append(card)
        print("...\n(You have drawn a card for split hand)")
        self.split_score += card_values[card[-1]]
        if card[-1] == 'A' and card_values[card[-1]]==11:
            self.has_split_ace = True
        while self.split_score > 21 and self.has_split_ace:
            self.split_score -= 10
            self.has_split_ace = False
    
    
    def stand(self):
        pass

    def double(self):
        if len(self.hand) == 2:
            self.double_amount = self.bet_amount
            self.bank -= self.double_amount
            print(f"(Pocket -${self.double_amount})")
            self.hit(deck.pop())
            self.show_hand_2()
            self.stand()
        else:
            print(f'You can only double at the first round!')
    
    def split_double(self):
        if len(self.split_hand) == 2:
            self.double_amount = self.bet_amount
            self.bank -= self.double_amount
            print(f"(Pocket -${self.double_amount})")
            self.split_hit(deck.pop())
            self.show_split_hand_2()
            self.stand()
    
    def split(self):
        if len(self.hand) == 2 and card_values[self.hand[0][-1]] == card_values[self.hand[1][-1]]:
            self.is_split = True
            self.split_hand = [self.hand.pop()]
            self.split_bet = self. bet_amount
            self.bank -= self.split_bet
            print(f'(Pocket -${self.split_bet})')
            self.split_hit(deck.pop())
            self.score -= card_values[self.hand[0][-1]]
        else:
            print(f'You are not able to split the card!')

    def show_split_hand_1(self):
        if self.split_hand:
            print(f"{self.name}'s Split Hand:")
            print(self.split_hand)
            self.split_score += card_values[self.split_hand[0][-1]]
            print (f"{self.name}'s split score: {self.split_score}")

    def show_split_hand_2(self):
        print(f"{self.name}'s Split Hand:")
        print(self.split_hand)
        print(f"{self.name} split score:", self.split_score)
        

    def surrender(self):
        self.is_surrender = True
        print (f'You surrender. Dealer win!')
        print(f'${round(self.bet_amount*0.5)} is returned to you~')
        self.bank += round(self.bet_amount*0.5)
        print(f'(Your pocket remains: {self.bank})')
        

#Design Dealer
class Dealer:
    def __init__(self):
        self.hand = []
        self.score = 0
        self.has_ace = False
        self.first_ace = False
    
    def reset(self):
        self.hand = []
        self.score = 0
        self.has_ace = False
        self.first_ace = False

    def show_hand_1(self):
        print("...\n...\nDealer's Hand:")
        print(f'({self.hand[0]}, ?)')
        self.score = card_values[self.hand[0][-1]] + card_values[self.hand[1][-1]]
        print("Dealer score:", card_values[self.hand[0][-1]])

    def show_hand_2(self):
        print("...\n...\nDealer's Hand:")
        print(self.hand)
        print("Dealer's score:", self.score)
        
    def hit(self, card):
        self.hand.append(card)
        print("...\n(Dealer is hitting a card)")
        self.score += card_values[card[-1]]
        if card[-1] == 'A' and card_values[card[-1]] ==11:
            self.has_ace = True
        while self.score > 21 and self.has_ace:
            self.score -= 10
            self.has_ace = False




name = input("Enter your name: ")
age = input("Enter your age: ")
bank = int(input("Enter your starting amount: "))

# Create the player and dealer objects
player = Player(name, age, bank)
dealer = Dealer()

def play():    
    # Clear hands and reshuffle the deck
    player.reset()
    dealer.reset()
    reset_deck()
    
    print("...\n...\n...\n(You have find a table)")
    while True:
        try:
            player.bet_amount = int(input('Please enter your betting amount (minimum $1): $'))
            if player.bet_amount > player.bank:
                print('Your betting amount exceeds your pocket. Please enter the amount again.')
                continue
            elif player.bet_amount == 0:
                print(f"You cannot bet with nothing!")
                continue
            else:
                player.bank -= player.bet_amount
                print(f'(Pocket -${player.bet_amount})')
                print(f'(Pocket remaining: ${player.bank})')
                break
        except:
            print('Invalid input. Please enter a valid integer.')
            continue

    print(f"...\n...\n...\n(Shuffling cards)\n(Drawing cards)")
    for gamestart in range(2):
            player.hand.append(deck.pop())
            dealer.hand.append(deck.pop())
    dealer.show_hand_1()
    print("")
    player.show_hand_1()
    for pc in player.hand:
        if pc[-1] == "A":
            player.first_ace = True
    for dc in dealer.hand:
        if dc[-1] == "A":
            dealer.first_ace = True
    
    # Check for player blackjack
    while player.score == 21:
        ans = input(f'BlackJack! You win!\n(Pocket +${player.bet_amount*2+round(player.bet_amount*0.5)})\nYour pocket remains: ${player.bank}\nDo you wanna play again? Y/N\n')
        if ans == "Y" or ans =="y":
            play()   
        elif ans == "N" or ans =="n":
            print ("Thanks for playing. Have a nice day!")
            exit()
        else:
            print ("Please only answer with Y / N")
            continue
    
    #If dealer's hand has an ace and ask for insurance
    while dealer.hand[0][-1] =="A":
        ans = input("Do you want to take a insurance? Y/N\n")
        if ans.lower() in ["yes", "y"]:
            insurance = round(player.bet_amount *0.5)
            player.bank -= insurance
            print(f'(Pocket -${insurance})')
            if card_values[dealer.hand[0][-1]] + card_values[dealer.hand[1][-1]] == 21:
                dealer.show_hand_2
                print ("Bingo! Dealer's score is 21.")
                player.bank += insurance*3
                print(f"Pocket +${insurance*3} ")
                print(f'Your pocket remains: ${player.bank}')
                while True:
                    ans1 = input('Do you wanna play again? Y/N\n')
                    if ans1.lower() in ["yes", "y"]:
                        play()   
                    elif ans1.lower() in ["no", "n"]:
                        print ("Thanks for playing. Have a nice day!")
                        exit()
                    else:
                        print ("Please only answer with Y/N")
            else:
                print("Dealer's score is not 21. Game continue.")
                break
        elif ans.lower() in ["no", "n"]:
            break
        else:
            print ("Please only answer with Y/N")

    
    
    # Check for dealer blackjack
    while dealer.score == 21:
        dealer.show_hand_2()
        ans = input(f'Dealer got BlackJack! You lost!\nYour pocket remains: ${player.bank}\nDo you wanna play again? Y/N\n')
        if ans == "Y" or ans =="y":
            play()   
        elif ans == "N" or ans =="n":
            print ("Thanks for playing. Have a nice day!")
            exit()
        else:
            print ("Please only answer with Y/N")

    # Player turn
    while player.score <21 :
        if len(player.hand) == 2:
            if card_values[player.hand[0][-1]] == card_values[player.hand[1][-1]] and player.is_split is False:
                ans = input(f"\nDo you wanna ...\n(1) Hit (2) Stand? (3) Double (4) Split (5) Surrender\nPlease enter a number: ")
            else:
                ans = input(f"\nDo you wanna ...\n(1) Hit (2) Stand? (3) Double           (5) Surrender\nPlease enter a number: ")
        else:   
            ans = input("\nDo you wanna ...\n(1) Hit (2) Stand?\nPlease enter a number: ")
        
        if ans == "1":
            player.hit(deck.pop())
            for c in player.hand[:2]:
                if c[-1] =="A" and player.score >21 and player.first_ace:
                    player.score -= 10
                    player.first_ace = False
            player.show_hand_2()
            
        elif ans == "2":
            player.stand()
            break
        elif ans == "3":
            player.double()
            for c in player.hand[:2]:
                if c[-1] =="A" and player.score >21 and player.first_ace:
                    player.score -= 10
                    player.first_ace = False
            break
        elif ans == "4":
            for pc in player.split_hand:
                if pc[-1] == "A":
                    player.split_first_ace = True
            player.split()
            player.show_split_hand_1()
            while len(player.hand) == 1 and player.split_score <21:
                ans = input("\nOn your split hand, do you wanna...\n(1) Hit (2) Stand? (3) Double \nPlease enter a number: ")
                if ans == '1':
                    player.split_hit(deck.pop())
                    for c in player.hand[:2]:
                        if c[-1] =="A" and player.score >21 and player.first_ace:
                            player.score -= 10
                            player.first_ace = False
                    player.show_split_hand_2()
                    if player.split_score > 21:
                        print("You are busted! You lose your split bet.")
                        print (f'...\n(Back to your main hand)\n')
                        player.hit(deck.pop())
                        player.show_hand_2()
                        break
                elif ans == '2':
                    print (f'...\n(Back to your main hand)\n')
                    player.hit(deck.pop())
                    player.show_hand_2()
                    break
                elif ans == '3':
                    player.split_double()
                    for c in player.split_hand[:2]:
                        if c[-1] =="A" and player.split_score >21 and player.split_first_ace:
                            player.split_score -= 10
                            player.split_first_ace = False
                    if player.split_score > 21:
                        print("You are busted! You lose your split bet.")
                        player.hit(deck.pop())
                        player.show_hand_2()
                        break
                    else:
                        print (f'...\n(Back to your main hand)\n')
                        player.hit(deck.pop())
                        player.show_hand_2()
                        break

                else:
                    print("Invalid action. Try again.")
        elif ans == "5":
            player.surrender()
            break
        else:
            print("Invalid action. Try again.")
        
    if player.score > 21:
                print("You are busted!")

    if player.is_surrender:
        while True:
            ans = input('Do you wanna play again? Y/N \n')    
            if ans == "Y" or ans == "y":
                play()
            elif ans == "N" or ans == "n":
                print("Thanks for playing. Have a nice day!")
                exit()
            else:
                print("Please only answer with Y/N")


    # Dealer turn
    dealer.show_hand_2()
    while dealer.score <17:
        dealer.hit(deck.pop())
        for c in dealer.hand[:2]:
            if c[-1] =="A" and dealer.score >21 and dealer.first_ace:
                dealer.score -= 10
                dealer.first_ace = False
        dealer.show_hand_2()

    #Check Split hand:
    if len(player.split_hand) > 0:
        print(f'\nChecking for {player.name} split hand result:')
        if player.split_score > 21:
            if dealer.score >21:
                print("Both your split hand and dealer busted!")
            else:
                print("Dealer wins over your split hand!")
        else:
            if dealer.score > 21:
                print("Dealer is busted! Your split hand win!")
                print(f'(Pocket +${(player.bet_amount+player.double_amount)*2})')
                player.bank += (player.bet_amount+player.double_amount)*2
                print(f'(Your pocket remains: ${player.bank})')
            elif dealer.score == 21 and player.split_score !=21:
                print("Dealer wins over your split hand!")
                print(f'(Your pocket remains: ${player.bank})')
            elif dealer.score > player.split_score:
                print("Dealer wins over your split hand!")
                print(f'(Your pocket remains: ${player.bank})')
            elif dealer.score < player.split_score:
                print("You win for your split hand!")
                print(f'(Pocket +${(player.bet_amount+player.double_amount)*2})')
                player.bank += (player.bet_amount+player.double_amount)*2
                print(f'(Your pocket remains: ${player.bank})')
            elif dealer.score == player.split_score:
                print("It's a tie for your split hand!")
                player.bank += (player.bet_amount+player.double_amount)
                print(f'${(player.bet_amount+player.double_amount)} is returned to you~')
                print(f'(Your pocket remains: ${player.bank})')

    # Determine the winner(s)
    print(f"\nChecking for {player.name}'s main hand result:")
    if player.score>21:
        if dealer.score >21:
            print("Both busted!")
            print(f"(Your pocket remains: ${player.bank})")
        else: 
            print("Dealer wins!")
            print(f'(Your pocket remains: ${player.bank})')
    else:
        if dealer.score > 21:
            print("Dealer is busted! You win!")
            print(f'(Pocket +${(player.bet_amount+player.double_amount)*2})')
            player.bank += (player.bet_amount+player.double_amount)*2
            print(f'(Your pocket remains: ${player.bank})')
        elif dealer.score == 21 and player.score !=21:
            print("Dealer wins!")
            print(f'(Your pocket remains: ${player.bank})')
        elif dealer.score > player.score:
            print("Dealer wins!")
            print(f'(Your pocket remains: ${player.bank})')
        elif dealer.score < player.score:
            print("You win!")
            print(f'(Pocket +${(player.bet_amount+player.double_amount)*2})')
            player.bank += (player.bet_amount+player.double_amount)*2
            print(f'(Your pocket remains: ${player.bank})')
        elif dealer.score == player.score:
            print("It's a tie!")
            player.bank += (player.bet_amount+player.double_amount)
            print(f'${(player.bet_amount+player.double_amount)} is returned to you~')
            print(f'(Your pocket remains: ${player.bank})')
    
    while True:
        if player.bank <=0:
            print("Sorry you lost all the money. GAME OVER!")
            exit()
        else:
            ans = input('Do you wanna play again? Y/N \n')    
            if ans == "Y" or ans == "y":
                play()
            elif ans == "N" or ans == "n":
                print("Thanks for playing. Have a nice day!")
                exit()
            else:
                print("Please only answer with Y/N")
play()
