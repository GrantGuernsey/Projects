import random
import numpy as np
import turtle
import time
import tkinter as tk

def visualize_game(verbose = 1):
    def up(event):
        nonlocal board
        board.moveUp()
        draw_board()

    def down(event):
        nonlocal board
        board.moveDown()
        draw_board()

    def left(event):
        nonlocal board
        board.moveLeft()
        draw_board()

    def right(event):
        nonlocal board
        board.moveRight()
        draw_board()


    def draw_board():
        canvas.delete("all")
        for i in range(rows):
            for j in range(cols):
                x1 = j * cell_width
                y1 = i * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height
                cell_value = board.board[i][j]
                canvas.create_rectangle(x1, y1, x2, y2, fill=get_cell_color(cell_value))
                canvas.create_text(x1 + cell_width // 2, y1 + cell_height // 2, text=str(int(cell_value)))

    def get_cell_color(value):
        colors = {
            0: "#FFFFFF",  # Empty cell
            2: "#EEE4DA",
            4: "#EDE0C8",
            8: "#F2B179",
            16: "#F59563",
            32: "#F67C5F",
            64: "#F65E3B",
            128: "#EDCF72",
            256: "#EDCC61",
            512: "#EDC850",
            1024: "#EDC53F",
            2048: "#EDC22E"
        }
        return colors.get(value, "#FFFFFF")

    root = tk.Tk()
    root.title("2048 Game Visualization")

    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()

    # Calculate cell width and height
    rows, cols = 4, 4
    cell_width = 400 // cols
    cell_height = 400 // rows

    # Generate initial game board
    board = gameBoard()
    board.startGame()

    # Draw initial game board
    draw_board()

    # Bind a button press event to update the game board
    root.bind("w", up)
    root.bind("s", down)
    root.bind("d", right)
    root.bind("a", left)

    try:
        root.mainloop()
    except:
        pass

    total_score = np.sum(board.board)
    return total_score


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

class GameOverException(Exception):
    print("raised")
    pass

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
        tk._exit()
    
    
    def moveDown(self):
        if(self.checkIfFull()):
            self.checkIfMovePossible()

        if(not self.checkIfMoveDownPossible()):
            print("cant move down but other direction possible")
            return

        prevBoard = np.copy(self.board)
        for x in range(4):
            self.board[:,x] = np.flip(slide(np.flip(self.board[:,x])))
            self.board[:,x] = np.flip(merge(np.flip(self.board[:,x])))
            self.board[:,x] = np.flip(slide(np.flip(self.board[:,x])))
        if(self.checkIfMoved(prevBoard)):
            self.addNew()
    
    def moveUp(self):
        if(self.checkIfFull()):
            self.checkIfMovePossible()
                    
        if(not self.checkIfMoveUpPossible()):
            print("cant move up but other direction possible")
            return

        prevBoard = np.copy(self.board)
        for x in range(4):
            self.board[:,x] = slide(self.board[:,x])
            self.board[:,x] = merge(self.board[:,x])
            self.board[:,x] = slide(self.board[:,x])
        if(self.checkIfMoved(prevBoard)):
            self.addNew()
    
    def moveRight(self):
        if(self.checkIfFull()):
            self.checkIfMovePossible()

        if(not self.checkIfMoveRightPossible()):
            print("cant move right but other direction possible")
            return

        prevBoard = np.copy(self.board)
        for x in range(4):
            self.board[x, :] = np.flip(slide(np.flip(self.board[x, :])))
            self.board[x, :] = np.flip(merge(np.flip(self.board[x, :])))
            self.board[x, :] = np.flip(slide(np.flip(self.board[x, :])))
        if(self.checkIfMoved(prevBoard)):
            self.addNew()

    def  moveLeft(self):
        if(self.checkIfFull()):
            self.checkIfMovePossible()
                    
        if(not self.checkIfMoveLeftPossible()):
            print("cant move left but other direction possible")
            return

        prevBoard = np.copy(self.board)
        for x in range(4):
            self.board[x, :] = slide(self.board[x, :])
            self.board[x, :] = merge(self.board[x, :])
            self.board[x, :] = slide(self.board[x, :])
        if(self.checkIfMoved(prevBoard)):
            self.addNew()
        self.addNew()

def playGame():
    game = gameBoard()
    game.startGame()
    value = visualize_game()
    return value

if __name__ == "__main__":
    game = gameBoard()
    game.startGame()
    print(game.board)

    value = visualize_game()
    print(value)