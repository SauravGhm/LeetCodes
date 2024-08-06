def solve_n_queens(n):
    def is_save(board, row, col):
        #Check this row on the left side
        for i in range(col):
            

