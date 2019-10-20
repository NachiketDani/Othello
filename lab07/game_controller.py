from pair_of_dice import PairofDice


class GameController:
    """
    Controls rolling, scoring and user interaction
    """
    def __init__(self):
        self.dice_pair = PairofDice()
        self.point = 0

    def start_play(self):
        print("Press enter to roll the dice:...")
        input()
        self.dice_pair.roll_dice()
        current_score = self.dice_pair.current_sum()
        self.outcome_roll1(current_score)

    def outcome_roll1(self, current_score):
        LOSE = [2, 3, 12]
        WIN = [7, 11]
        if current_score in LOSE:
            print("You rolled", current_score, ". You lose")
        elif current_score in WIN:
            print("You rolled", current_score, ". You win!")
        else:
            self.point = current_score
            print("Your point is", self.point, ".")
            self.continue_play()

    def continue_play(self):
        print("Press enter to roll the dice:...")
        input()
        self.dice_pair.roll_dice()
        current_score_contd = self.dice_pair.current_sum()
        if current_score_contd == 7:
            print("You rolled", current_score_contd, ". You lose")
        elif current_score_contd == self.point:
            print("You rolled", current_score_contd, ". You win!")
        else:
            print("You rolled", current_score_contd, ".")
            self.continue_play()
