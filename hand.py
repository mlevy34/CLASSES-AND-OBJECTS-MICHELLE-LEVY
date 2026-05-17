from card import Card


class Hand:
    """
    Represents the collection of cards held by a participant.

    The Hand class is responsible for:
    - storing cards
    - adding new cards
    - calculating Blackjack totals
    - handling Ace value adjustments
    """

    def __init__(self):
        """
        Initializes an empty hand of cards.
        """
        self.cards = []

    def add_card(self, card) -> None:
        """
        Adds a card to the hand.

        Args:
            card (Card): The card being added to the hand.
        """
        self.cards.append(card)

    def get_total(self) -> int:
        """
        Calculates the total Blackjack value of the hand.

        Ace cards are initially counted as 11.
        If the total exceeds 21, Ace values are adjusted
        from 11 to 1 as needed to prevent busting.

        Returns:
            int: The total value of the hand.
        """
        total = 0
        aces = 0

        # Add the value of each card
        for card in self.cards:
            total += card.value

            # Count how many aces are in the hand
            if card.rank == "Ace":
                aces += 1

        # Adjust Ace values if total exceeds 21
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total

    def show_hand(self) -> str:
        """
        Creates a readable string representation
        of all cards in the hand.

        Returns:
            str: A comma-separated list of cards.
        """
        lst = []

        # Convert each card into a string
        for card in self.cards:
            lst.append(str(card))

        return ",".join(lst)

    def __str__(self):
        """
        Returns the string representation of the hand.

        Returns:
            str: The formatted hand display.
        """
        return self.show_hand()

