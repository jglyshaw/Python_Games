import tkinter as tk
import time

class Game:
    def __init__(self, rows, cols, size, refresh_rate = 100):
        
        # Set up root
        self.root = tk.Tk()
        self.root.title("Your Game")

        # Setup the canvas
        self.canvas = tk.Canvas(self.root)
        self.canvas.configure(width=len(self.grid[0])*self.square_size, height=len(self.grid)*self.square_size)
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

        self.snake = []


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

    def start_game(self):
        self.root.bind("<KeyPress>", self.on_keypress)
        
        self.snake.append([5,5])
        head = self.snake[0]
        self.create_square(head, "black")
        
        self.game_loop()
        self.root.mainloop()
    
    def game_loop(self):
        # Game logic methods
        self.user_action()

        # Continue game loop again
        self.root.after(self.refresh_rate, self.game_loop)

    def inside_grid(self, cord):
        if(cord[0] > self.rows-1 or cord[0] < 0):
            return False
        if(cord[1] > self.cols-1 or cord[1] < 0):
            return False
        return True

    def user_action(self):

        head = self.snake[0]
        tail = self.snake[-1]
        new_head = list(head)

        if(self.user_input == "d"):
            new_head[0] += 1
        elif(self.user_input == "a"):
            new_head[0] -= 1
        elif(self.user_input == "s"):
            new_head[1] += 1
        elif(self.user_input == "w"):
            new_head[1] -= 1

        if(self.inside_grid(new_head)):
            # Delete last segment
            self.delete_square(tail)
            self.snake.pop(-1)

            # Add new segment
            self.create_square(new_head, "black")
            self.snake.insert(0, new_head)


if __name__ == "__main__":
    game = Game(20, 20, 50)
    game.start_game()