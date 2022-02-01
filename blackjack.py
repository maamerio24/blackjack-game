import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        one_card = self.deck.pop()
        return one_card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total = 0
        self.busted = False
        self.play = None

    def score(self):
        self.total = 0 
        for card in self.hand:
            if card.rank == 'Ace' and self.hand.count('Ace') < 1:
                self.total += 11
            elif card.rank == 'Ace' and self.total > 10:
                self.total += 1
            else:
                self.total += int(card.value)
        return self.total
    
    def make_move(self, player, decision):
        if decision == 'hit':
            Deck.deal(player)
            player.play = 'Hit'
        elif decision == 'stay':
            player.play = 'Stay'
    
    def show_cards(self):
        if self.name == 'Dealer':
            print('\n', f"{self.name}'s hand:")
            print("? of ?,")
            for card in self.hand[1:]:
                print(card)
            self.score()
        else:
            print('\n', f"{self.name}'s hand after dealing cards:")
            for card in self.hand:
                print(card)

            print('\n')
            print('\n', f"{self.name}'s total = {self.calc_score()}", '\n')
        






class Dealer(Player):
    pass


class Human(Player):
    pass


class Game:
    def __init__(self):
        playing = True
    


def main():
    pass


# main()

