from abc import ABCMeta, abstractmethod


class Game(metaclass=ABCMeta):
    def __init__(self):
        pass

    def game_logic(self, board: dict, round_num: int):
        """
        Let the player play if it is their turn, otherwise the "AI" will play.
        :return:
        """
        if round_num < 9:
            if round_num % 2 == 0:
                player = "X"
                position = input("Your turn. Enter position (row,place):")
                self.update_board(board, round_num, player, position)
                round_num += 1
                self.game_logic(board=board, round_num=round_num)
            else:
                self.play_by_AI(board, round_num)
                round_num += 1
                self.game_logic(board=board, round_num=round_num)
        else:
            print("Game finished")
            print("Starting a new game")
            self.start()

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update_board(self, board_prev: dict, round_num: int, player: str, position: str):
        pass

    @abstractmethod
    def play_by_AI(self, board: dict, round_num: int):
        pass
