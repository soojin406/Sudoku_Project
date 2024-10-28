from print_board import print_board
from generate_sudoku import generate_sudoku
from solve_sudoku import solve_sudoku

def play_sudoku():
    board = generate_sudoku()
    while True:
        print_board(board)
        try:
            row = int(input("행(0-8): "))
            col = int(input("열(0-8): "))
            num = int(input("숫자(1-9): "))
            if row not in range(9) or col not in range(9) or num not in range(1, 10):
                print("잘못된 입력입니다. 다시 입력해 주세요.")
                continue
            if board[row][col] == 0:
                board[row][col] = num
                if solve_sudoku(board):
                    print("축하합니다! 스도쿠를 완료했습니다!")
                    break
            else:
                print("해당 위치에 이미 숫자가 있습니다.")
        except ValueError:
            print("잘못된 입력입니다. 다시 시도해 주세요.")
