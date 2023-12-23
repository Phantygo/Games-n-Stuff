import random
import sys

playing = True
# Suit, Rank, and Values

values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 1}
ranks = ("Two", "Three", "Four", "Five", "Six","Seven","Eight","Nine", "Ten", "Jack", "Queen", "King", "Ace")
suits = ("Hearts", "Diamonds", "Spades", "Clubs")

class Card():

    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        self.values = values[rank]
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck():

    def __init__(self):
        
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit,rank)
                self.all_cards.append(new_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self, player_cards, dealer_cards, player_hand, dealer_hand):

        for num in range(2):
            #Pop card off deck, add to list, add card value, adjust for ace
            player_moved_card = self.all_cards.pop(0)
            player_cards.append(player_moved_card)
            player_hand.value += values[player_moved_card.rank]
            player_hand.ace_adjust()

            moved_card = self.all_cards.pop(0)
            dealer_cards.append(moved_card)
            dealer_hand.value+= values[moved_card.rank] 
            dealer_hand.ace_adjust()

    def __str__(self):
        
        pass

class Hand:

    def __init__(self,deck_instance,cards):
        self.cards = cards
        self.value = 0
        self.aces = 0
        self.deck_instance = deck_instance
    
    def add_card(self):
        
        card = self.deck_instance.all_cards.pop(0)
        self.cards.append(card)
        self.value += values[card.rank]    
    
    def ace_adjust(self):
        
        for i in self.cards:
            if i.rank == "Ace":
                self.aces += 1
            # Make ace = 11
            if  self.aces == 1 and self.value <= 10:
                self.value += 10 
            # Ace = 1 when value exceeds 21
            if self.aces > 0 and self.value > 21:
                self.value -= 10
    
    def __str__(self) -> str:
        pass

class Player:

    def __init__(self, name):
        self.balance = 100
        self.bet_amount = 0
        self.name = name

    def double_down(self):
    
        double_down = ' '
        while double_down != "Yes" and double_down != "No":
            double_down = input("Double Down? ")
        
            if double_down == "Yes":
                self.bet_amount+=self.bet_amount
                break
            
            elif double_down =="No":
                break

            else:
                print("Invalid Input. Choose Yes or No")
            
    def place_bet(self):

        while True:
            try:
                #Ask for Bet
                self.bet_amount = int(input(f"{self.name}, place bet amount: "))  

                #Check for Over-Betting   
                while self.bet_amount > self.balance:
                    print("Insufficient Funds")
                    self.bet_amount = int(input(f"{self.name}, place bet amount: "))   
                    
            except ValueError:
                print("Please input a number")
        
            else:
                self.balance -= self.bet_amount
                print(f"Bet: {self.bet_amount} \nBalance: {self.balance}")
                break
    
    def win_bet(self):

        self.balance += self.bet_amount*2
        print(f"New Balance: {self.balance}")
        pass

    def lose_bet(self):

        print(f"New Balance: {self.balance}")
        pass

#Functions

def hit(deck_instance,dealer_hand, player_hand):
    global playing

    hit = ' '
    while hit != "Yes" and hit != "No":
        hit = input("Hit?").capitalize()

        if hit == "Yes":
            
            player_hand.add_card()
         
            player_hand.ace_adjust()
            if player_hand.value >= 21:
                
                show_all(dealer_hand,player_hand)
                
                break
            show_hidden(dealer_hand,player_hand)

        elif hit == "No":
            while dealer_hand.value <= 16:
                dealer_hand.add_card()
                dealer_hand.ace_adjust()
            playing = False
            show_all(dealer_hand,player_hand)
            break
        
        else:
            print("Invalid Input. Choose Yes or No.")

def hit_or_stand(deck_instance,player_hand, dealer_hand):
    global playing

    while playing and player_hand.value < 21:
        hit(deck_instance,dealer_hand, player_hand)
    

def show_hidden(dealer_hand, player_hand):

    #Iterate through hand list to print cards individually
    dealer_cards_info = ", ".join(str(dealer_hand.cards[i]) for i in range(len(dealer_hand.cards) -1 ))
    player_cards_info = ", ".join(str(player_hand.cards[i]) for i in range(len(player_hand.cards)))
    print(f"\nDealer's Cards: {dealer_cards_info}, Hidden Card \nYour Cards: {player_cards_info}. Value: {player_hand.value}")

def show_all(dealer_hand, player_hand):

    player_cards_info = ", ".join(str(player_hand.cards[i]) for i in range(len(player_hand.cards)))
    dealer_cards_info = ", ".join(str(dealer_hand.cards[i]) for i in range(len(dealer_hand.cards)))
    print(f"\nDealer's Cards: {dealer_cards_info}, Value: {dealer_hand.value} \nYour Cards: {player_cards_info}, Value: {player_hand.value}")


print("Welcome to BlackJack. You begin with $100. ")
account = Player("New Player")

def play_game():
    global playing
    while account.balance > 0:

        # Start with empty hands
        player_cards = []
        dealer_cards = []

        # Create Deck and Deal Cards
        playing = True
        new_deck = Deck()
        dealer_hand = Hand(new_deck, dealer_cards)
        player_hand = Hand(new_deck, player_cards)
        new_deck.shuffle()
        new_deck.deal(player_cards, dealer_cards, player_hand, dealer_hand)
        dealer_hand.ace_adjust()
        player_hand.ace_adjust()
        show_hidden(dealer_hand, player_hand)

        account.place_bet()
        hit_or_stand(new_deck, player_hand, dealer_hand)

        if player_hand.value > dealer_hand.value and player_hand.value <= 21:
            account.win_bet()
            print("You Win")
            break
        if dealer_hand.value > 21:
            account.win_bet()
            print("Dealer Busted, You win.")
            break
        if dealer_hand.value > player_hand.value and dealer_hand.value <= 21:
            account.lose_bet()
            print("Dealer Won")
            break
        if player_hand.value > 21:
            print("Bust")
            account.lose_bet()
            break
        elif player_hand.value == dealer_hand.value:
            print("Tie. No winner")
            break
    
    if account.balance > 0:

        play_again = input("Play Again? (yes/no) ").lower()

        if play_again == "yes":
            play_game()

        if play_again == "no":
            print("Thank you for playing")

    else:
        print("you broke")

# Start the game
play_game()










