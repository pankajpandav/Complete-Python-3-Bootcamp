import random

suits = ('Hearts','Spades','Clubs','Diamonds')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.deck.append(card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += "\n "+ card.__str__()
        return f"The Deck has: {deck_comp}"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        player_comp = ''
        for card in self.cards:
            player_comp += "\n "+ card.__str__()
        return f"The Player has: {player_comp}"

class Chips:

    def __init__(self):
        self.total = 100 #default value but it can be passed as well
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet():
    while True:
        try:
            bet = int(input("Please enter your bet: "))
        except TypeError:
            print("Sorry this is not a number! Please try again")
            continue
        except:
            print("An Error occured! Please try again")
            continue
        else:
            print("Thanks for the input.")
            break
        
