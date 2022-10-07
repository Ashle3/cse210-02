from game.director import Player, deck
import imp
def main():
    print("Hello! Welcome to Hi Lo!")
    print()
    print()

    #ask user for how many players 
    # for loop to get multiple players

    playersName = input("What is your name?: ")
    player1 = Player()
    player1.name = playersName
    cardDeck = deck()
    cardSelection = cardDeck.drawCard()

    while player1.is_playing == True: 
        print(f"The current card is {cardSelection.number} of {nextCard.suit}")

        #validate that input
        nextCard = cardDeck.drawCard()
        #print(f"The next card drawn is {nextCard}. ")
        validated = False
        while not validated:
            question = input("Do you think the next one is Higher or Lower? (h/l): ")
            if question == "h":
                validated = True
                result = cardSelection.cardCompareHigher(nextCard)
            elif question == "l":
                validated = True
                result = cardSelection.cardCompareLower(nextCard)
            else:
                print("Invalid Input. Try again. ")
        print(f"The next card drawn is {nextCard.number} of {nextCard.suit}. ")
        player1.changePlayerScore(result)
        player1.checkPlayerPoints()
        
        print(f"You currently have {player1.score_start} points. ")
        validatedKeepPlaying = False
        while not validatedKeepPlaying:
            answer = input("Do you want to keep playing? y/n: ")
            if answer == "n":
                validatedKeepPlaying = True
                player1.is_playing = False
            elif answer == "y":
                validatedKeepPlaying = True
            else:
                print("Invalid Answer")
        cardSelection = nextCard

    print("Thanks for playing the game!")





        

main()