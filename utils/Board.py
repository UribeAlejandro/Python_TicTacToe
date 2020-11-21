from sys import exit
from random import randint
from utils.Game import Game


class Board(Game):
    def __init__(self):
        pass

    def start(self) -> None:
        round_o = 0
        board_o = {
            0:
                {0: " ", 1: " ", 2: " "},
            1:
                {0: " ", 1: " ", 2: " "},
            2:
                {0: " ", 1: " ", 2: " "}
        }
        print("Instructions:")
        print("The positions in the board can be accessed by specifying the position as row,column.")
        print("You will be asked to enter a valid combination if you enter an invalid pair or an occupied position.")
        print("Row & Columns start at 0 and ends at 2.")
        print("If you want to finish the game type exit")
        # Prints empty board
        self.print_board(board_o)
        # Starts a game
        self.game_logic(board_o, round_o)

    def update_board(self, board_prev: dict, round_num: int, player: str, position: str) -> dict:
        """

        :param position:
        :param player: "X" or "O"
        :param round_num: 0 by default as the start of a new game.
        :param board_prev: Previous board, to be updated.
        :return: Board after update.
        """
        status, position_list = self.check_update(board_prev, position, round_num)

        if status:
            board_new = board_prev
            board_new[position_list[0]][position_list[1]] = player
            round_num += 1
            if player == "X":
                self.print_board(board_new)
                self.check_winner(board_new, player)
                self.game_logic(board_new, round_num)
            else:
                print("AI moves!")
                self.print_board(board_new)
                self.check_winner(board_new, player)
                self.game_logic(board_new, round_num)
        else:
            if player == "O":
                self.game_logic(board_prev, round_num)
            else:
                print("Invalid input")
                self.game_logic(board_prev, round_num)

        return board_new

    def check_update(self, board: dict, position: str, round_num: int):
        """

        :param round_num:
        :param board:
        :param position:
        :return:
        """
        position_list = self.clean_input(position=position)

        if len(position_list) == 2:
            row = position_list[0]
            pos = position_list[1]
            if board[row][pos] == " ":
                status = True
            else:
                status = False
        else:
            status = False

        return status, position_list

    def play_by_AI(self, board: dict, round_num: int) -> None:
        """

        :return:
        """

        row = randint(0, 2)
        pos = randint(0, 2)
        position = f"{row}{pos}"
        player = "O"

        board_new = self.update_board(board, round_num, player, position)

        self.game_logic(board_new, round_num)

    def check_winner(self, board: dict, player: str) -> None:
        points_d_l = 0
        points_d_r = 0
        for row in board.keys():
            points_h = 0
            points_v = 0
            for col in board[row].keys():
                # Check horizontal spaces
                if player in board[row][col]:
                    points_h += 1
                    if points_h == 3:
                        if player == "X":
                            print("You won!")
                            self.start()
                        else:
                            print("You lost!")
                            self.start()
                # Check vertical spaces
                if player in board[col][row]:
                    points_v += 1
                    if points_v == 3:
                        if player == "X":
                            print("You won!")
                            self.start()
                        else:
                            print("You lost!")
                            self.start()
                # Check diagonal (upper left to right bottom)
                if row == col:
                    if player in board[col][row]:
                        points_d_l += 1
                        if points_d_l == 3:
                            if player == "X":
                                print("You won!")
                                self.start()
                            else:
                                print("You lost!")
                                self.start()
                if 2-1-row == col:
                    if player in board[2-1-row][col]:
                        points_d_r += 1
                        if points_d_r == 3:
                            if player == "X":
                                print("You won!")
                                self.start()
                            else:
                                print("You lost!")
                                self.start()

    # Static Methods below
    @staticmethod
    def print_board(board_prev: dict) -> None:
        """
        Prints the board in console.
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

    @staticmethod
    def clean_input(position: str) -> list:
        """

        :param position:
        :return:
        """
        position = position.strip()
        position_list = []
        if position.lower() == "exit":
            exit("The player doesn't want to continue playing.")
        else:
            for number in position:
                if number in ["0", "1", "2"]:
                    position_list.append(int(number))

        return position_list
