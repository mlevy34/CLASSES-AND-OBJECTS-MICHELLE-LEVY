class Card:
    """
    Represents a single playing card used in Blackjack.

    Attributes:
        suit (str): The suit of the card (Hearts, Diamonds, Clubs, Spades).
        rank (str): The rank of the card (Ace, 2-10, Jack, Queen, King).
        value (int): The Blackjack value of the card.
    """

    def __init__(self, suit: str, rank: str, value: int) -> None:
        """
        Initializes a Card object.

        Args:
            suit (str): The card's suit.
            rank (str): The card's rank.
            value (int): The Blackjack value assigned to the card.
        """
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self) -> str:
        """
        Returns a readable string representation of the card.

        Returns:
            str: The card formatted as 'Rank of Suit'.
        """
        return f"{self.rank} of {self.suit}"