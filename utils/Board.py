from random import randint
from string import punctuation

from utils.Game import Game


class Board(Game):
    def __init__(self, board_prev: dict, round_num: int):
        self.board_prev = board_prev or {
            0:
                {0: " ", 1: " ", 2: " "},
            1:
                {0: " ", 1: " ", 2: " "},
            2:
                {0: " ", 1: " ", 2: " "}
        }

    def print_board(self, board_prev: dict) -> None:
        """
        Prints the
        """
        board_chars = {
            0: "-",
            1: "+",
            2: "|"
        }
        for i in board_prev.keys():
            if i != 2:
                print(f"{board_prev[i][0]}{board_chars[2]}{board_prev[i][1]}{board_chars[2]}{board_prev[i][2]}")
                print(f"{board_chars[0]}{board_chars[1]}{board_chars[0]}{board_chars[1]}{board_chars[0]}")
            else:
                print(f"{board_prev[i][0]}{board_chars[2]}{board_prev[i][1]}{board_chars[2]}{board_prev[i][2]}")

    def update_board(self, board_prev: dict, round_num: int = 0, player: str = "X") -> None:
        """

        :param player:
        :param round_num:
        :param board_prev:
        :return:
        """
        board_new = board_prev
        position = input("Enter position (row,place):")
        position_list = self.clean_input(str(position))

        if self.check_update(board_prev, position_list, round_num):
            board_new[position_list[0]][position_list[1]] = player
            round_num += 1
            self.print_board(board_new)
            self.update_board(board_new, round_num)
        else:
            print("Invalid input")
            self.update_board(board_prev, round_num)

    def clean_input(self, position: str) -> list:
        """

        :param position:
        :return:
        """
        position = position.strip()
        for sign in list(punctuation):
            if sign in position:
                position = position.replace(sign, "")

        position_list = position.split()

        return position_list

    def check_update(self, board_prev: dict, position_list: list, round_num: int):
        """

        :param round_num:
        :param board_prev:
        :param position_list:
        :return:
        """
        if len(position_list) < 2 or len(position_list) > 2:
            self.update_board(board_prev, round_num)

        for position in position_list:
            if position not in ["0", "1", "2"]:
                self.update_board(board_prev, round_num)

        row = position_list[0]
        pos = position_list[1]

        if (board_prev[row][pos] == "X") or (board_prev[row][pos] == "O"):
            self.update_board(board_prev, round_num)

    def play_by_AI(self, board_new: dict, round_num: int, player: str):
        """

        :return:
        """
        row = randint(0, 2)
        pos = randint(0, 2)
        position = f"{row}{pos}"
        position_list = position.split()

        self.update_board()
