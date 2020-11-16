class Game(object):
    def __init__(self, board_prev: dict, round_num: int, position: str = ""):
        self.position = position
        self.round_num = round_num
        self.board_prev = board_prev

    def game_logic(self, board_prev: dict, round_num: int):
        """
        Let the player play if it is their turn, otherwise the "AI" will play.
        :return:
        """
        if round_num < 10:
            if round_num % 2 == 0:
                player = "X"
                # TODO update parameters of method below
                self.update_board()
            else:
                player = "O"
                self.play_by_AI(board_prev, round_num, player)
        else:
            print("Game finished")
