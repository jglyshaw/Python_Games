import tkinter as tk

class GameBase:
    def __init__(self, rows, cols, size, refresh_rate = 100):
        
        # Set up root
        self.root = tk.Tk()
        self.root.title("Your Game")

        # Setup the __canvas
        self.__canvas = tk.Canvas(self.root, bg='black')
        self.__canvas.configure(width=rows*size, height=cols*size)
        self.__canvas.pack()

        # Establish game size and grid
        self.rows = rows
        self.cols = cols
        self.__block_size = size
        self.__grid = [[0]*self.cols for i in range(self.rows)]

        # Establish the refresh rate
        self.refresh_rate = refresh_rate

        # To hold user input
        self.user_input = 0
        self.root.bind("<KeyPress>", self.__on_keypress)

    # Determines if a block already exists at a cordinate
    def block_exists(self, cord):
        return self.__grid[cord[0]][cord[1]] != 0

    # Create a block at a given cordinate.
    def create_block(self, cord, color, shape = 0):
        if(self.block_exists(cord)):
            raise Exception("ERROR: block there already exists.")
        else:
            x = cord[0] * self.__block_size
            y = cord[1] * self.__block_size

            if(shape == "circle"):
                self.__grid[cord[0]][cord[1]] = self.__canvas.create_oval(x, y, x + self.__block_size, y + self.__block_size, fill=color, outline="black")
            else:
                self.__grid[cord[0]][cord[1]] = self.__canvas.create_rectangle(x, y, x + self.__block_size, y + self.__block_size, fill=color, outline="black")
    
    # Delete a block at a given cordinate.
    def delete_block(self, cord):
        if(not self.block_exists(cord)):
            raise Exception("ERROR: no block there exists.")
        else:
            self.__canvas.delete(self.__grid[cord[0]][cord[1]]) 
            self.__grid[cord[0]][cord[1]] = 0
   
    # Change the color of a existing block.
    def change_block_color(self, cord, color):
        self.__canvas.itemconfigure(self.__grid[cord[0]][cord[1]], fill=color)

    # Check if a cordinate is within the grid.
    def inside_grid(self, cord):
        return 0 <= cord[0] < self.rows and 0 <= cord[1] < self.cols

    def start_game(self):
        self.run_game()
        self.root.mainloop()

    def run_game(self):
       self.game_loop()
       self.root.after(self.refresh_rate, self.run_game)
        
    def game_loop(self):
       raise Exception("This Function is abstract.")

    # Return last user input.
    def get_user_input(self):
        return self.user_input

    # Store the pressed key into class state.
    def __on_keypress(self, event):
        self.user_input = event.keysym
