class Card:
    """ Гральна карта """

    RANKS = ["T", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "B", "Q", "k"]
    # ♣ ♦ ♥ ♠
    SUITS = [u'\u2660', u'\u2663', u'\u2665', u'\u2666']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep
    

class Hand:
    """ Рука: набір карт, який має гравець """

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep
    
    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """ Deck of playing cards """

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANLS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't give you more cards: ",
                          "the cards is over!")


card1 = Card(rank="T", suit=Card.SUITS[0])
print('Card one: ')
print(card1)

card2 = Card(rank="2", suit=Card.SUITS[0])
card3 = Card(rank="3", suit=Card.SUITS[0])
card4 = Card(rank="4", suit=Card.SUITS[0])
card5 = Card(rank="5", suit=Card.SUITS[0])
print('Another cards: ')
print(card2)
print(card3)
print(card4)
print(card5)

my_hand = Hand()
print('\nCards before taken: ')
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print('\nCards after taken: ')
print(my_hand)

your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("\nI give you my two first cards")
print("Now in your hands:")
print(your_hand)
print("In mine:")
print(my_hand)

my_hand.clear()
print("\nI dropped all my cards and now: ")
print(my_hand)

# main
deck1 = Deck()
print("Створено нову колоду.")
print("Ось ця колода:")
print(deck1)

deck1.populate()
print("\nУ колоді з'явилися карти.")
print("Ось як вона виглядає тепер:")
print(deck1)

deck1.shuffle()
print("\nDeck is shuffled.")
print("Deck now: ")

my_hand = Hand()
your_hand = Hand()