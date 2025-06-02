Write a Python program to simulate a card game using object-oriented principles. The program should
include a Card class to represent individual playing cards, a Deck class to represent a deck of cards,
and a Player class to represent players receiving cards. Implement a shuffle method in the Deck class
to shuffle the cards and a deal method to distribute cards to players. Display each player’s hand after
dealing.

Ans:
    import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_players, cards_each):
        return [[self.cards.pop() for _ in range(cards_each)] for _ in range(num_players)]

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def show_hand(self):
        return ', '.join(str(card) for card in self.hand)

deck = Deck()
deck.shuffle()

players = [Player("Alice"), Player("Bob")]
hands = deck.deal(2, 5)

for i, player in enumerate(players):
    player.receive_cards(hands[i])
    print(f"{player.name}'s hand: {player.show_hand()}")
