# Day 24 - MindTact: Tic Tac Toe AI
# A console-based Tic Tac Toe game featuring an unbeatable AI using the Minimax algorithm.

import math
import os
import time

# --------------------------------------------------
# Board Handling
# --------------------------------------------------
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("MINDTACT – TIC TAC TOE AI\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == " "]


def check_winner(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None


def is_full(board):
    return " " not in board


# --------------------------------------------------
# AI Logic (Minimax Algorithm)
# --------------------------------------------------
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = "O"
            score = minimax(board, depth + 1, False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = "X"
            score = minimax(board, depth + 1, True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score


def ai_move(board):
    best_score = -math.inf
    best_move = None
    for move in available_moves(board):
        board[move] = "O"
        score = minimax(board, 0, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = "O"


# --------------------------------------------------
# Game Loop
# --------------------------------------------------
def main():
    board = [" "] * 9
    print_board(board)
    print("You are X. The AI is O.\n")

    while True:
        # Player move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move not in range(9) or board[move] != " ":
                print("Invalid move. Try again.")
                time.sleep(1)
                continue
        except ValueError:
            print("Please enter a number between 1 and 9.")
            time.sleep(1)
            continue

        board[move] = "X"
        print_board(board)

        if check_winner(board) == "X":
            print("You win! (But only because the AI let you start...)")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is thinking...")
        time.sleep(0.7)
        ai_move(board)
        print_board(board)

        if check_winner(board) == "O":
            print("AI wins! Better luck next time.")
            break
        elif is_full(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()
