from card import Card
import random


class Deck:
    """
    Represents a full deck of playing cards used in Blackjack.

    The Deck class is responsible for:
    - creating all 52 cards
    - shuffling the cards
    - dealing one card at a time
    """

    def __init__(self):
        """
        Initializes an empty list of cards.
        """
        self.cards = []

    def build_deck(self) -> None:
        """
        Creates a standard 52-card deck.

        Each suit receives:
        - numbered cards 2-10
        - face cards worth 10
        - Ace valued at 11
        """
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

        ranks = [
            ("2", 2), ("3", 3), ("4", 4), ("5", 5),
            ("6", 6), ("7", 7), ("8", 8), ("9", 9),
            ("10", 10), ("Jack", 10), ("Queen", 10),
            ("King", 10), ("Ace", 11)
        ]

        # Create one card for every suit/rank combination
        for suit in suits:
            for rank, value in ranks:
                self.cards.append(Card(suit, rank, value))

    def shuffle(self) -> None:
        """
        Randomly shuffles the deck of cards.
        """
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        """
        Removes and returns the top card from the deck.

        Returns:
            Card: The card dealt from the deck.
        """
        current_card = self.cards[len(self.cards) - 1]

        # Remove the dealt card from the deck
        self.cards.remove(current_card)

        return current_card

    def cards_remaining(self) -> int:
        """
        Returns the number of cards left in the deck.

        Returns:
            int: Remaining number of cards.
        """
        return len(self.cards)