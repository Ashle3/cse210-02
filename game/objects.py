import random
class Player:
    """A person who plays the game. 
    
    Attributes:
    name = name of person 
    is_playing = if they are still in the game
    score = their current score"""

    def __init__(self):
        """Constructs a new player. """
        self.name = ""
        self.is_playing = True
        self.score = 300

    def changePlayerScore(self, outcome):
        if outcome:
            self.score += 100
            print(f"That was correct {self.name}! Your current score is {self.score}")
        else:
            self.score -= 75
            print(f"Ooohh sorry that was wrong {self.name}. Your current score is {self.score}")

    def checkPlayerPoints(self):
        if self.score <= 0:
            self.is_playing = False
        else:
            return


class Deck:

    def __init__(self):
        """The deck of cards in the game
        attributes:
        checkForShuffle = see if cards are less than 12, then shuffle cards
        drawCard = take card off top of pile

        """
        self.cards = []
        for i in range(1,5):
            for j in range(1,14):
                self.singleCard = Card()
                self.singleCard.number = j
                if i == 1:
                    self.singleCard.suit = "Hearts"
                elif i == 2:
                    self.singleCard.suit = "Diamonds"
                elif i == 3:
                    self.singleCard.suit = "Spades"
                elif i == 4:
                    self.singleCard.suit = "Clubs"    
                self.cards.append(self.singleCard)
        random.shuffle(self.cards)

    #recreate card pile(deck)
    def checkForShuffle(self):
        if len(self.cards) < 12:
            self.__init__()                                         

    #gives us new card from deck
    def drawCard(self):
        drawn = self.cards[-1]
        self.cards = self.cards[:-1]
        return drawn

class Card:
    """ A single card in the deck
    attributes: 
    cardCompareHigher = see if next card is higher
    cardCompareLower = see if next card is lower
    Hierarchy = Hearts -> Diamonds -> Spades -> Clubs (best -> worst)
    """
    def __init__(self):
        self.number = 0
        self.suit = ""

    def cardCompareHigher(self, nextCard):
        if self.number < nextCard.number:
            return True
        elif self.number == nextCard.number:
            if nextCard.suit == "Hearts":
                return True
            elif nextCard.suit == "Diamonds" and self.suit != "Hearts":
                return True
            elif nextCard.suit == "Spades" and self.suit == "Clubes":
                return True
            else: 
                return False
        else:
            return False

        
    def cardCompareLower(self, nextCard):
        if self.number > nextCard.number:
            return True
        elif self.number == nextCard.number:
            if nextCard.suit == "Clubs":
                return True
            elif nextCard.suit == "Spade" and self.suit != "Club":
                return True
            elif nextCard.suit == "Diamond" and self.suit == "Heart":
                return True
            else: 
                return False
        else:
            return False
        
            
                

