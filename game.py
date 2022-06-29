class Board:
    board = [["e", "e", "e", "e", "e", "e", "e"], ["e", "e", "e", "e", "e", "e", "e"], ["e", "e", "e", "e", "e", "e", "e"], ["e", "e", "e", "e", "e", "e", "e"], ["e", "e", "e", "e", "e", "e", "e"], ["e", "e", "e", "e", "e", "e", "e"]]
    def __init__(self):
        pass
    def print_board(self):
        for i in reversed(range(0, 6)):
            for j in range(0, 7):
                print(self.board[i][j], end=" ")
            print()
    def play(self, player, column):
        if column > 6 or column < 0:
            return False
        for i in range(0, 6):
            if self.board[i][column] == "e":
                self.board[i][column] = player.get_symbol()
                return True
        return False
    def check_for_winner(self):
        end = False
        winner = None
        for i in range(0, 6):
            for j in range(0, 7):
                if self.board[i][j] != "e":
                    try:
                        if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3]:
                            end = True
                        if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == self.board[i + 3][j]:
                            end = True
                        if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3]:
                            end = True
                        if self.board[i][j] == self.board[i - 1][j + 1] == self.board[i - 2][j + 2] == self.board[i - 3][j + 3]:
                            end = True
                    except IndexError:
                        pass
                    if end:
                        winner = next(player.name for player in [player1, player2] if player.symbol == self.board[i][j])
        return end, winner
class Player:
    def __init__(self, symbol):
        self.symbol = symbol
    def get_symbol(self):
        return self.symbol
class Tile:
    pass

board = Board()
player1 = Player("x")
player2 = Player("o")

print("Welcome to the game!")
print("Player 1, please enter your name:")
player1.name = input()
print("Player 2, please enter your name:")
player2.name = input()

player1turn = True
while True:
    if player1turn == True:
        print(player1.name + ", please enter your column:")
        column = int(input())-1
        if board.play(player1, column):
            board.print_board()
            player1turn = False
        else:
            print("Invalid column")
    else:
        print(player2.name + ", please enter your column:")
        column = int(input())-1
        if board.play(player2, column):
            board.print_board()
            player1turn = True
        else:
            print("Invalid column")
    end, winner = board.check_for_winner()
    if end:
        print("The winner is " + winner)
        break
