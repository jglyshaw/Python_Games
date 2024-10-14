import tkinter as tk
import time

class Game:
    def __init__(self, rows, cols, size, refresh_rate = 1):
        
        # Set up root
        self.root = tk.Tk()
        self.root.title("Your Game")

        # Establish game size and grid
        self.rows = rows
        self.cols = cols
        self.square_size = size
        self.grid = [[0]*self.rows for i in range(self.cols)]

        # Establish the refresh rate
        self.refresh_rate = refresh_rate

        # Setup the canvas
        self.canvas = tk.Canvas(self.root)
        self.canvas.configure(width=len(self.grid[0])*self.square_size, height=len(self.grid)*self.square_size)

        # Draw the initial grid and pack
        self.canvas.pack()

        self.key = 0

        self.i = 0
        self.j = 0

    # Determines if a square already exists at a given row and column.
    def square_exists(self, row, col):
        return self.grid[row][col] != 0

    # Create a square at a given row and column.
    def create_square(self, row, col, color):
        if(self.square_exists(row,col)):
            print("error square there already exists")
        else:
            x = row * self.square_size
            y = col * self.square_size
            self.grid[row][col] = self.canvas.create_rectangle(x, y, x + self.square_size, y + self.square_size, fill=color, outline=color)
    
    # Delete a square at a given row and column.
    def delete_square(self, row, col):
        if(not self.square_exists(row,col)):
            print("error no square there exists")
        else:
            self.canvas.delete(self.grid[row][col]) 
            self.grid[row][col] = 0

    # Store the pressed key into class state.
    def on_keypress(self, event):
        self.key = event.keysym

    def start_game(self):
        self.root.bind("<KeyPress>", self.on_keypress)
        self.game_loop()
        self.root.mainloop()
    
    def game_loop(self):
        # Game logic methods
        self.user_action()

        # Continue game loop again
        self.root.after(self.refresh_rate, self.game_loop)

    def user_action(self):
        if(self.key == "space"):

            self.delete_square(self.i,self.j)

            if(self.i >= self.rows - 1):
                self.i = 0
                self.j += 1
            else:
                self.i += 1
            
            self.create_square(self.i,self.j,"black")

            self.key = 0


if __name__ == "__main__":
    game = Game(10, 10, 50)
    game.start_game()