import random
import numpy as np
import turtle
import time
import tkinter as tk

class GamePlayer:
    def __init__(self):
        self.board = gameBoard()
        self.board.startGame()

    def move(self, direction):
        if direction == "w":
            self.board.moveUp()
        elif direction == "s":
            self.board.moveDown()
        elif direction == "a":
            self.board.moveLeft()
        elif direction == "d":
            self.board.moveRight()
        else:
            print("Invalid move. Use w, s, a, or d.")
        return self.board.board

    def is_game_over(self):
        return not self.board.checkIfMovePossible()

    def get_board(self):
        return self.board.board

    def get_total_score(self):
        return np.sum(self.board.board)

def slide(arr):
    result = np.zeros_like(arr)
    j = 0

    for x in range(4):
        if arr[x] != 0:
            result[j] = arr[x]
            j += 1

    return result

def merge(arr):
    for x in range(3):
        if arr[x] != 0 and arr[x] == arr[x+1]:
            arr[x] *= 2
            arr[x+1] = 0

    return arr
    return arr


class gameBoard():
    def __init__(self):
        self.board = np.zeros((4,4))

    def draw_grid(self):
        return

    def addNew(self):
        empty_cells = [(row, col) for row in range(4) for col in range(4) if self.board[row][col] == 0]

        # Choose a random empty cellda
        try:
            row, col = random.choice(empty_cells)
        except:
            return

        # Randomly assign a value of 2 or 4
        self.board[row][col] = 4 if random.randint(1, 5) == 1 else 2

    def startGame(self):
        self.addNew()
        self.addNew()
    
    def checkIfMoved(self, prevBoard):
        return not np.array_equal(self.board, prevBoard)

    def checkIfFull(self):
        return np.all(self.board)

    def checkIfMoveUpPossible(self):
        original_board = self.board.copy()
        for x in range(4):
            self.board[:, x] = slide(self.board[:, x])
            self.board[:, x] = merge(self.board[:, x])
            self.board[:, x] = slide(self.board[:, x])
        if not np.array_equal(self.board, original_board):
            self.board = original_board  # Restore the original board state
            return True
        self.board = original_board  # Restore the original board state
        return False

    def checkIfMoveDownPossible(self):
        original_board = self.board.copy()
        for x in range(4):
            self.board[:,x] = np.flip(slide(np.flip(self.board[:,x])))
            self.board[:,x] = np.flip(merge(np.flip(self.board[:,x])))
            self.board[:,x] = np.flip(slide(np.flip(self.board[:,x])))
        if not np.array_equal(self.board, original_board):
            self.board = original_board  # Restore the original board state
            return True
        self.board = original_board  # Restore the original board state
        return False

    def checkIfMoveLeftPossible(self):
        original_board = self.board.copy()
        for x in range(4):
            self.board[x, :] = slide(self.board[x, :])
            self.board[x, :] = merge(self.board[x, :])
            self.board[x, :] = slide(self.board[x, :])
        if not np.array_equal(self.board, original_board):
            self.board = original_board  # Restore the original board state
            return True
        self.board = original_board  # Restore the original board state
        return False

    def checkIfMoveRightPossible(self):
        original_board = self.board.copy()
        for x in range(4):
            self.board[x, :] = np.flip(slide(np.flip(self.board[x, :])))
            self.board[x, :] = np.flip(merge(np.flip(self.board[x, :])))
            self.board[x, :] = np.flip(slide(np.flip(self.board[x, :])))
        if not np.array_equal(self.board, original_board):
            self.board = original_board  # Restore the original board state
            return True
        self.board = original_board  # Restore the original board state
        return False

    def checkIfMovePossible(self):
        if(self.checkIfMoveUpPossible() or
            self.checkIfMoveDownPossible() or
            self.checkIfMoveLeftPossible() or
            self.checkIfMoveRightPossible()):
            return True
        print(f"Total score: {np.sum(self.board)}")
        return False
    
    
    def moveDown(self):
        if(self.checkIfFull()):
            self.checkIfMovePossible()

        if(not self.checkIfMoveDownPossible()):
            #print("cant move down but other direction possible")
            return False

        prevBoard = np.copy(self.board)
        for x in range(4):
            self.board[:,x] = np.flip(slide(np.flip(self.board[:,x])))
            self.board[:,x] = np.flip(merge(np.flip(self.board[:,x])))
            self.board[:,x] = np.flip(slide(np.flip(self.board[:,x])))
        if(self.checkIfMoved(prevBoard)):
            self.addNew()
        return True

    def moveUp(self):
        if(self.checkIfFull()):
            self.checkIfMovePossible()
                    
        if(not self.checkIfMoveUpPossible()):
            #print("cant move up but other direction possible")
            return False

        prevBoard = np.copy(self.board)
        for x in range(4):
            self.board[:,x] = slide(self.board[:,x])
            self.board[:,x] = merge(self.board[:,x])
            self.board[:,x] = slide(self.board[:,x])
        if(self.checkIfMoved(prevBoard)):
            self.addNew()
        return True

    def moveRight(self):
        if(self.checkIfFull()):
            self.checkIfMovePossible()

        if(not self.checkIfMoveRightPossible()):
            #print("cant move right but other direction possible")
            return False

        prevBoard = np.copy(self.board)
        for x in range(4):
            self.board[x, :] = np.flip(slide(np.flip(self.board[x, :])))
            self.board[x, :] = np.flip(merge(np.flip(self.board[x, :])))
            self.board[x, :] = np.flip(slide(np.flip(self.board[x, :])))
        if(self.checkIfMoved(prevBoard)):
            self.addNew()
        return True

    def  moveLeft(self):
        if(self.checkIfFull()):
            self.checkIfMovePossible()
                    
        if(not self.checkIfMoveLeftPossible()):
            #print("cant move left but other direction possible")
            return False

        prevBoard = np.copy(self.board)
        for x in range(4):
            self.board[x, :] = slide(self.board[x, :])
            self.board[x, :] = merge(self.board[x, :])
            self.board[x, :] = slide(self.board[x, :])
        if(self.checkIfMoved(prevBoard)):
            self.addNew()
        return True
