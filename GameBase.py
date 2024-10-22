import tkinter as tk
import random


class GameBase:
    def __init__(self, rows, cols, size, refresh_rate):
        
        # Set up __root
        self.__root = tk.Tk()
        self.__root.title("Your Game")

        # Setup the canvas
        self.__canvas = tk.Canvas(self.__root, bg='black')
        self.__canvas.configure(width=rows*size, height=cols*size)
        self.__canvas.pack()

        # Establish game size and grid
        self.rows = rows
        self.cols = cols
        self.__block_size = size
        self.__grid = [[0]*self.cols for i in range(self.rows)]

        # Establish the refresh rate
        self.__refresh_rate = refresh_rate

        # To hold user input
        self.__user_input = 0
        self.__root.bind("<KeyPress>", self.__on_keypress)

        # To hold references to images
        self.__images = []

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

    # Create a block with an image
    def create_image_block(self, cord, image_path):
        if self.block_exists(cord):
            raise Exception("ERROR: block there already exists.")
        x, y = cord[0] * self.__block_size, cord[1] * self.__block_size
        image = tk.PhotoImage(file=image_path)
        # Calculate the resize factors (target dimensions should be your block size)
        width_factor = image.width() // self.__block_size
        height_factor = image.height() // self.__block_size

        # Resize the image (ensure factors are positive)
        if width_factor > 0 and height_factor > 0:
            image = image.subsample(width_factor, height_factor)
        else:
            image = image.zoom(-width_factor, -height_factor)

        self.__grid[cord[0]][cord[1]] = self.__canvas.create_image(x, y, anchor="nw", image=image)
        self.__images.append(image)
    
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

    # Return last user input.
    def get_user_input(self):
        return self.__user_input

    def start_game(self):
        self.__run_game()
        self.__root.mainloop()

    def delete_all(self):
        self.__canvas.delete("all")
        self.__grid = [[0]*self.cols for i in range(self.rows)]

    def random_row(self):
        return random.randint(0, self.rows-1)

    def random_col(self):
        return random.randint(0, self.cols-1)

    def __run_game(self):
       self.game_loop()
       self.__root.after(self.__refresh_rate, self.__run_game)
        
    def game_loop(self):
       raise Exception("This Function is abstract.")

    # Store the pressed key into class state.
    def __on_keypress(self, event):
        self.__user_input = event.keysym
