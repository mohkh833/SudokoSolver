import time
class SudokuSolver:
    def FindEmptyCells (self, board):
        for i in range(9):
            for j in range(9):
               if board[i][j] == -1 :
                return i,j
        return None, None

    def isValid (self, row, column, GussedNumber, board):
        for r in range(9):
            if board[r][column] == GussedNumber:
                return False

        for c in range(9):
            if board[row][c] == GussedNumber:
                return False

        row_Box = (row // 3) * 3
        column_Box = (column // 3) * 3

        for r in range(3):
            for c in range(3):
                if board[row_Box + r][column_Box + c] == GussedNumber:
                    return False

        return True


    def Solve (self,board):
        find = self.FindEmptyCells(board)
        row,col = find

        if row is None:
            return True

        for GussedNumber in range(1,10):
            if self.isValid(row, col, GussedNumber, board):
                board[row][col] = GussedNumber
                if self.Solve(board):
                    return True

        board[row][col] = -1

        return False




if __name__ == '__main__':
    start = time.time()
    obj = SudokuSolver()
    board = [
        [3, -1, -1, 9, -1, -1, -1, -1, -1],
        [-1, -1,7, -1, -1, -1, 2, 5, -1],
        [5, -1, -1, -1, -1, -1, -1, 1, -1],

        [-1, -1, -1, 1, -1, 2, -1, 7, 9],
        [-1, -1, -1, -1, -1, 8, 1, -1, -1],
        [-1, -1, -1, -1, -1, 4, -1, -1, -1],

        [-1, 7, -1, -1, -1, -1, -1, -1, -1],
        [-1, 2, -1, -1, 7, -1, -1, 4, 5],
        [-1, -1, 1, 3, -1, -1, -1, -1, 6]
    ]
    obj.Solve(board)

    print(board)
    end = time.time()
    print(f"Runtime of the program is {end - start}")