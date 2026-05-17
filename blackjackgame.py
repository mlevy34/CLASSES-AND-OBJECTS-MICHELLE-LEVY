from dealer import Dealer
from deck import Deck
from player import Player


class BlackJackGame:
    def __init__(self, player_name : str):
        self.player_name = player_name
        self.deck = Deck()
        self.player = Player(player_name)
        self.dealer = Dealer()


    def initial_deal(self)->None:
        for i in range(2):
            self.player.take_card(self.deck.deal_card())
            self.dealer.take_card(self.deck.deal_card())

    def show_game_state(self) -> None:

        print(f"Dealer shows: {self.dealer.show_first_card()}")
        print("Dealer has: [Hidden Card]")

        print()

        print(f"{self.player.name}'s hand: {self.player.show_hand()}")
        print(f"{self.player.name}'s total: {self.player.get_total()}")

    def determine_winner(self) -> str:

        player_total = self.player.get_total()
        dealer_total = self.dealer.get_total()

        if self.player.is_busted():
            return "Dealer wins! Player busted."

        elif self.dealer.is_busted():
            return "Player wins! Dealer busted."

        elif player_total > dealer_total:
            return "Player wins!"

        elif dealer_total > player_total:
            return "Dealer wins!"

        else:
            return "It's a tie!"

    def play(self) -> None:

        print("Welcome to Blackjack!")
        print()
        print("Building Deck...")
        self.deck.build_deck()

        print()

        print("Shuffling...")
        self.deck.shuffle()

        print()

        print("Dealing cards...")
        self.initial_deal()

        print()

        print("CURRENT GAME STATE:")
        self.show_game_state()

        print()
        print("PLAYER TURN:")
        print()

        self.player.take_turn(self.deck)

        if not self.player.is_busted():

            print()
            print("DEALER TURN")
            print()

            self.dealer.take_turn(self.deck)


        print("FINAL HANDS")


        print(f"Dealer hand: {self.dealer.show_hand()}")
        print(f"Dealer total: {self.dealer.get_total()}")

        print()

        print(f"{self.player.name}'s hand: {self.player.show_hand()}")
        print(f"{self.player.name}'s total: {self.player.get_total()}")

        print()
        print(self.determine_winner())
