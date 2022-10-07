# cse210-02
Through groupwork, we create a game called Hilo.

Group Members:
Ashlee Butterfield,
Brock Ford,
Zachary Lindstrom,
Sayri Quinchiguango de la Torre,
Spencer Cory Christensen

Hilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one. Points are won or lost based on whether or not the player guessed correctly.

The player starts the game with 300 points.
Individual cards are represented as a number from 1 to 13.
The current card is displayed.
The player guesses if the next one will be higher or lower.
The the next card is displayed.
The player earns 100 points if they guessed correctly.
The player loses 75 points if they guessed incorrectly.
If a player reaches 0 points the game is over.
If a player has more than 0 points they decide if they want to keep playing.
If a player decides not to play again the game is over.


The program must include a README file.
The program must include class and method comments.
The program must have at least two classes.
The program must remain true to game play described in the overview.

Enhanced input validation.
Enhanced game play and game over messages.
Enhanced game display, e.g. card suits
TODO:
Create a player class
    - player starts with 300 points
    - player name (string)
    - Continuing playing (bool)
Create a deck class
    - random card from ints 1-13 (4 sets of these)
    *- suits





player.score += 100 if correct
player.score -= 75 if inccorect

at end of each "turn" check_points to see if game is over
if they have more than 0, ask if they want to continue game. (while loop)




(Establish a new player with attributes (points)
Establish our deck of cards
print current card (random int from 1-13)
 ask for higher/lower input
 get next card value and print
 correct_guess indicates if it was right or wrong
 verify points
 play again? )




 IDEAS:
 could make a shuffle function to reset the cards class after x amount of draws.
 Add a second or thrid player to the game
 Validate input (easy)
 Give each player a name attribute
 
<<<<<<< HEAD
=======
>>>>>>> toDoList


TODO List (October):
    fix bugs as we run (possibly remove instead of pop)
    add multiple players
    fix drawing cards (find way to set next card as cardSelection after pass.) 
            - could take it out of the while loop and then just draw next card...
    validate user input
    ? put functions into classes istead of in main?
    Rename files and directories
    
>>>>>>> f088d3f92b90eb16fe908367f434e46fe85d03e4
