from deck import Deck
from hand import Hand
from participant import Participant


class Player(Participant):
    """
    Represents the human player in the Blackjack game.

    The Player class inherits from Participant
    and allows the user to choose whether to
    hit or stand during their turn.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a Player object.

        Creates a new Hand object for the player
        and passes the information to the
        Participant parent class.

        Args:
            name (str): The player's name.
        """
        hand = Hand()
        super().__init__(name, hand)

    def take_turn(self, deck: Deck):
        """
        Controls the player's turn.

        The player repeatedly chooses whether
        to hit or stand.

        If the player chooses hit:
        - a card is dealt
        - the card is added to the player's hand
        - the updated total is displayed

        The turn ends if:
        - the player stands
        - the player busts

        Args:
            deck (Deck): The deck used to deal cards.
        """
        while True:

            # Ask the player whether they want another card
            choice = input("Would you like to hit or stand?")

            # Normalize the user's input
            choice = choice.lower().strip()

            # End the turn if the player stands
            if choice == "stand":
                print(f"{self.name} stands")
                break

            # Deal another card if the player hits
            elif choice == "hit":

                # Deal a card from the deck
                card = deck.deal_card()

                # Add the dealt card to the player's hand
                self.take_card(card)

                # Display the dealt card and updated total
                print(f"You drew: {card}")
                print(f"Your total is now {self.get_total()}")

                # Stop the turn if the player busts
                if self.is_busted():
                    break

            # Handle invalid user input
            else:
                print("Invalid choice, please try again")
