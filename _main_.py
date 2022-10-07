from game.objects import Player, Deck
def main():
    print("Hello! Welcome to Hi Lo!")
    print()
    print()
    playersName = input("What is your name?: ")
    player1 = Player()
    player1.name = playersName
<<<<<<< HEAD
    cardDeck = Deck()
    
    currCard = cardDeck.drawCard()
    while player1.is_playing == True: 
        print(f"{player1.name}'s current card is the {currCard.number} of {currCard.suit}")
        nextCard = cardDeck.drawCard()
        validated = False
        while(not validated):
            question = input("Do you think the next one is Higher or Lower? (h/l): ") 
            if question == "h":
                validated = True
                result = currCard.cardCompareHigher(nextCard)
            elif question == "l":
                validated = True
                result = currCard.cardCompareLower(nextCard)
            elif question == "quit":
                validated = True
            else:
                print("If you meant to exit program, please enter \"quit\", otherwise try again... ")
        if question == "quit":
            player1.is_playing = False
            break
        print(f"The next card is the {nextCard.number} of {nextCard.suit}...")
        player1.changePlayerScore(result)
        player1.checkPlayerPoints()
        cardDeck.checkForShuffle()
        currCard = nextCard
        print()
        keepPlaying = input("Would you like to keep playing? (type \"quit\" to quit): ")
        if keepPlaying == "quit":
            player1.is_playing = False
=======
    cardDeck = deck()
    cardSelection = cardDeck.drawCard()

    while player1.is_playing == True: 
        print(f"The current card is {cardSelection.number} of {nextCard.suit}")

        #validate that input
        nextCard = cardDeck.drawCard()
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
>>>>>>> main

    print("Thanks for playing the game!")
    print(f"{player1.name}, you ended the game with {player1.score} points.")


<<<<<<< HEAD
=======



        
>>>>>>> main

main()