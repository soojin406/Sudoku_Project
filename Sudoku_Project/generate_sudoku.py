import random

from solve_sudoku import solve_sudoku
from initialize_board import initialize_board

def generate_sudoku(empty_spaces=40):
    """빈 칸이 포함된 스도쿠 퍼즐을 생성합니다."""
    board = initialize_board()
    solve_sudoku(board)
    for _ in range(empty_spaces):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board
