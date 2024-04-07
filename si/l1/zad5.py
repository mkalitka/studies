import random

_TRIES = 1000

class Board():
    def __init__(self, size, rows, cols):
        self.size = size

        self.rows = rows
        self.cols = cols

        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def reset_board(self):
        for x in range(self.size):
            height = self.cols[x]
            for y in range(height):
                self.board[x][y] = 1
            for y in range(height, self.size):
                self.board[x][y] = 0

    def sum_row(self, y):
        sum = 0
        for x in range(self.size):
            sum += self.board[x][y]
        return sum

    def wspolczynnik_zlo(self):
        sum = 0
        for y in range(self.size):
            sum += abs(self.rows[y] - self.sum_row(y))
        return sum

    def flip(self):
        col = random.randint(0, self.size - 1)

        start_to_zlo = {}

        for start in range(self.size - self.cols[col] + 1):
            for y in range(self.size):
                self.board[col][y] = 0

            for y in range(start, start + self.cols[col]):
                self.board[col][y] = 1

            start_to_zlo[start] = self.wspolczynnik_zlo()

        best_start = min(start_to_zlo, key=start_to_zlo.get)
        for y in range(self.size):
            self.board[col][y] = 0

        for y in range(best_start, best_start + self.cols[col]):
            self.board[col][y] = 1

    def __str__(self):
        ret = ""
        for y in range(self.size):
            for x in range(self.size):
                ret += str(self.board[x][y])
            ret += "\n"
        ret = ret.replace("0", ".")
        ret = ret.replace("1", "#")
        return ret
    
    def is_solved(self):
        return self.wspolczynnik_zlo() == 0

    def solve(self):
        for _ in range(_TRIES):
            self.reset_board()
            for _ in range(_TRIES):
                self.flip()
                if self.is_solved():
                    return True


def main():
    with open("zad5_input.txt") as f:
        size, *rest = f.read().splitlines()
        size = int(size.split()[0])
        rows = [int(x) for x in rest[:size]]
        cols = [int(x) for x in rest[size:]]
        board = Board(size, rows, cols)
        board.solve()
        with open("zad5_output.txt", "w") as out:
            out.write(str(board))

if __name__ == "__main__":
    main()
