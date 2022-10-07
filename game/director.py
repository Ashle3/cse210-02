import random


class Player:
    """A person who directs the game. 
    
    Attributes:
    is_playing (boolean): whether or not the game is being played."""

    def __init__(self):
        """Constructs a new player. """
        self.name = ""
        self.is_playing = True
        self.score_start = 300

    def changePlayerScore(self, outcome):
        if outcome:
            self.score_start += 100
        else:
            self.score_start -= 75

    def checkPlayerPoints(self):
        if self.score_start <= 0:
            self.is_playing = False
        else:
            return

class deck:

    def __init__(self):
        "construct a new deck of cards"
        self.cards = []
        for i in range(1,5):
            for j in range(1,14):
                self.cardSingle = card()
                self.cardSingle.number = j
                if i == 1:
                    self.cardSingle.suit = "hearts"
                elif i == 2:
                    self.cardSingle.suit = "diamonds"
                elif i == 3:
                    self.cardSingle.suit = "spades"
                elif i == 4:
                    self.cardSingle.suit = "clubs"
                self.cards.append(self.cardSingle)
        random.shuffle(self.cards)

    #recreate card pile(deck)
    def shuffleDeck(self):
        if len(self.cards)<12:
            print("Everyday I'm shuffling!")
            self.__init__()
            

    #gives us a card out of the deck
    def drawCard(self):
        drawn = self.cards[-1]
        self.cards = self.cards[:-1]
        return drawn

class card:
    def __init__(self):
        "construct a new deck of cards"
        self.number = 0
        self.suit = ""

    def cardCompareHigher(self, secondCard):
        if self.number < secondCard.number: return True
        elif self.number == secondCard.number:
            if secondCard.suit == "hearts":
                return True
            elif secondCard.suit == "diamonds" and self.suit != "hearts":
                return True
            elif secondCard.suit == "spades" and self.suit == "clubs":
                return True
            else: 
                return False

        else: return False

    def cardCompareLower(self, secondCard):
        if self.number > secondCard.number: return True
        elif self.number == secondCard.number:
            if secondCard.suit == "clubs":
                return True
            elif secondCard.suit == "spades" and self.suit != "clubs":
                return True
            elif secondCard.suit == "diamonds" and self.suit == "hearts":
                return True
            else: 
                return False

        else: return False


            
                

       

