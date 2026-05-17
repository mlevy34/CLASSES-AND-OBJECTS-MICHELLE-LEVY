from deck import Deck
from hand import Hand
from card import Card


class Participant:
    """
    Represents a general participant in the Blackjack game.

    This class serves as the parent class for both
    the Player and Dealer classes.

    A Participant:
    - has a name
    - has a Hand object
    - can take cards
    - can display cards
    - can calculate hand totals
    - can determine if they busted
    """

    def __init__(self, name: str, hand: Hand):
        """
        Initializes a Participant object.

        Args:
            name (str): The participant's name.
            hand (Hand): The participant's hand of cards.
        """
        self.name = name
        self.hand = hand

    def take_card(self, card: Card):
        """
        Adds a card to the participant's hand.

        Args:
            card (Card): The card being added.
        """
        self.hand.add_card(card)

    def show_hand(self) -> str:
        """
        Returns a readable string representation
        of the participant's hand.

        Returns:
            str: The formatted hand.
        """
        return self.hand.__str__()

    def get_total(self) -> int:
        """
        Returns the total Blackjack value
        of the participant's hand.

        Returns:
            int: The hand total.
        """
        return self.hand.get_total()

    def is_busted(self) -> bool:
        """
        Determines whether the participant's
        hand total exceeds 21.

        Returns:
            bool: True if busted, otherwise False.
        """
        if self.hand.get_total() > 21:
            return True
        else:
            return False

    def take_turn(self, deck: Deck) -> None:
        """
        Deals one card from the deck and adds it
        to the participant's hand.

        Args:
            deck (Deck): The deck used to deal cards.
        """
        card = deck.deal_card()
        self.take_card(card)

