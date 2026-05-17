from hand import Hand
from participant import Participant
from deck import Deck


class Dealer(Participant):
    """
    Represents the dealer in the Blackjack game.

    The Dealer class inherits from Participant and follows
    the automatic dealer rules for Blackjack.
    """

    def __init__(self):
        """
        Initializes the dealer with the name 'dealer'
        and an empty Hand object.
        """
        hand = Hand()
        super().__init__("dealer", hand)

    def show_first_card(self):
        """
        Returns only the dealer's first visible card.

        This is used at the start of the game when
        one dealer card remains hidden.

        Returns:
            str: The dealer's first card.
        """
        parts = self.show_hand().split(",")
        return parts[0]

    def take_turn(self, deck: Deck):
        """
        Controls the dealer's turn.

        The dealer must continue drawing cards until
        the total value of the hand is at least 17.

        Args:
            deck (Deck): The deck used to draw cards.
        """
        while True:

            # Dealer stops drawing once total reaches 17 or more
            if self.get_total() >= 17:
                break

            else:
                # Deal one card from the deck
                card = deck.deal_card()

                # Add the dealt card to the dealer's hand
                self.take_card(card)

            # Display updated dealer information
            print(f"Dealer draws: {card}")
            print(f"Dealer total: {self.get_total()}")

        # Check if dealer busted
        if self.is_busted():
            print("Dealer busted!")
        else:
            print(f"Dealer stands with {self.get_total()}")
