import tkinter as tk
import time

class GameBase:
    def __init__(self, rows, cols, size, refresh_rate = 100):
        
        # Set up root
        self.root = tk.Tk()
        self.root.title("Your Game")

        # Setup the canvas
        self.canvas = tk.Canvas(self.root)
        self.canvas.configure(width=rows*size, height=cols*size)
        self.canvas.pack()

        # Establish game size and grid
        self.rows = rows
        self.cols = cols
        self.square_size = size
        self.grid = [[0]*self.rows for i in range(self.cols)]

        # Establish the refresh rate
        self.refresh_rate = refresh_rate

        # To hold user input
        self.user_input = 0
        self.root.bind("<KeyPress>", self.on_keypress)

    # Determines if a square already exists at a cordinate
    def square_exists(self, cord):
        return self.grid[cord[0]][cord[1]] != 0

    # Create a square at a given cordinate.
    def create_square(self, cord, color):
        if(self.square_exists(cord)):
            raise Exception("error square there already exists")
        else:
            x = cord[0] * self.square_size
            y = cord[1] * self.square_size
            self.grid[cord[0]][cord[1]] = self.canvas.create_rectangle(x, y, x + self.square_size, y + self.square_size, fill=color, outline=color)
    
    # Delete a square at a given cordinate.
    def delete_square(self, cord):
        if(not self.square_exists(cord)):
            raise Exception("error no square there exists")
        else:
            self.canvas.delete(self.grid[cord[0]][cord[1]]) 
            self.grid[cord[0]][cord[1]] = 0

    # Store the pressed key into class state.
    def on_keypress(self, event):
        self.user_input = event.keysym
        print(self.user_input)

    # Return last user input.
    def get_user_input(self):
        return self.user_input

    # Check if a cordinate is within the grid.
    def inside_grid(self, cord):
        if(cord[0] > self.rows-1 or cord[0] < 0):
            return False
        if(cord[1] > self.cols-1 or cord[1] < 0):
            return False
        return True


