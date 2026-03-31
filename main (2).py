import random


class Player:
    """
    Represents the player in the Codebreaker game.

    Tracks all guesses made and the number of attempts used.
    """

    def __init__(self) -> None:
        """
        Initializes a Player object with empty guess history
        and zero attempts used.
        """
        self.guesses = []
        self.attempts_used = 0

    def make_guess(self)-> str:
        """
        Prompts the player to enter a valid 4-digit guess.

        Returns:
            str: A valid 4-digit numeric guess.
        """
        while True:
            guess = str(input("Enter a 4 digit code:"))
            if guess.isdigit() and len(guess) == 4:
                self.attempts_used += 1
                return guess
            else:
                print("Invalid code, please reenter")
                continue

    def store_guess(self, guess : str)->None:
        """
        Stores a guess in the player's guess history.

        Args:
            guess (str): The player's guess.
        """
        self.guesses.append(guess)

    def get_attempts_used(self)->int:
        """
        Returns the number of attempts used by the player.

        Returns:
            int: Number of attempts used.
        """
        return self.attempts_used


class Code:
    """
    Represents the secret code used in the game.
    """

    def __init__(self)->None:
        """
        Initializes the Code object with an empty value.
        """
        self.value = ""

    def generate_code(self)->None:
        """
        Generates a random 4-digit secret code (digits 0–9).
        """
        code = ""
        for i in range(4):
            digit = random.randint(0, 9)
            code += str(digit)
        self.value = code

    def get_code(self)->str:
        """
        Returns the generated secret code.

        Returns:
            str: The secret code.
        """
        return self.value


class Evaluator:
    """
    Responsible for comparing the player's guess with the secret code.
    """

    def count_exact(self, code : str, guess : str)->int:
        """
        Counts digits that are correct in both value and position.

        Args:
            code (str): The secret code.
            guess (str): The player's guess.

        Returns:
            int: Number of exact matches.
        """
        count = 0
        for i in range(len(code)):
            if code[i] == guess[i]:
                count += 1
        return count

    def count_partial(self, code : str, guess : str)->int:
        """
        Counts digits that are correct but in the wrong position.

        Args:
            code (str): The secret code.
            guess (str): The player's guess.

        Returns:
            int: Number of partial matches.
        """
        count = 0
        secrets = list(code)
        guesses = list(guess)

        if len(guesses) == 0:
            return 0
        else:
            for i in range(len(guesses)):
                if guesses[i] == secrets[i]:
                    guesses[i] = None
                    secrets[i] = None

            for i in range(len(guess)):
                if guesses[i] is not None:
                    if guesses[i] in secrets:
                        count += 1
                        secrets[secrets.index(guesses[i])] = None

            return count


class Game:
    """
    Controls the overall flow of the Codebreaker game.
    """

    def __init__(self, code_obj : object, evaluator_obj : object, player_obj : object, max_attempts : int)->None:
        """
        Initializes the Game object.

        Args:
            code_obj (Code): Code generator object.
            evaluator_obj (Evaluator): Evaluator object.
            player_obj (Player): Player object.
            max_attempts (int): Maximum allowed attempts.
        """
        self.code = code_obj
        self.evaluator = evaluator_obj
        self.player = player_obj
        self.max_attempts = max_attempts

        self.code.generate_code()
        self.secret_code = self.code.get_code()

    def play(self)->None:
        """
        Runs the main game loop until win or loss condition is met.
        """
        while True:
            guess2 = self.player.make_guess()
            self.max_attempts -= 1
            self.player.store_guess(guess2)

            e, p = self.process_turn(guess2)

            if self.check_win(e):
                print("You won!")
                break
            else:
                if self.check_loss():
                    print(f"You lost!, correct code: {self.show_user_code()}")
                    break
                else:
                    continue

    def process_turn(self, guess1 : str)->tuple:
        """
        Processes a single guess and prints feedback.

        Args:
            guess1 (str): Player's guess.

        Returns:
            tuple: (exact matches, partial matches)
        """
        exact = self.evaluator.count_exact(self.secret_code, guess1)
        partial = self.evaluator.count_partial(self.secret_code, guess1)

        print(f"Exact: {exact}, Partial: {partial}")
        return exact, partial

    def check_win(self, exact_matches : int)->bool:
        """
        Checks if the player has won.

        Args:
            exact_matches (int): Number of exact matches.

        Returns:
            bool: True if player wins, otherwise False.
        """
        if exact_matches == 4:
            return True
        else:
            return False

    def check_loss(self)->bool:
        """
        Checks if the player has lost.

        Returns:
            bool: True if attempts are exhausted.
        """
        if self.max_attempts <= 0:
            return True
        else:
            return False

    def show_user_code(self)->str:
        """
        Returns the secret code.

        Returns:
            str: The secret code.
        """
        return self.secret_code


# -----------------------------
# Game execution
# -----------------------------

player = Player()
code = Code()
evaluator = Evaluator()
game = Game(code, evaluator, player, 10)

game.play()













