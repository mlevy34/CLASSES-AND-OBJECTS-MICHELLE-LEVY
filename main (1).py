game.play()
from blackjackgame import BlackJackGame


"""
Main driver file for the Blackjack game.

This file:
- asks the user for their name
- creates a BlackjackGame object
- starts the game
"""

# Prompt the player to enter their name
name = input("Please enter your name:")

# Create a BlackjackGame object using the player's name
game = BlackJackGame(name)

# Start the Blackjack game
game.play()