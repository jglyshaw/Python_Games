import tkinter as tk

# Window setup
root = tk.Tk()
root.title("Your Game")

def game_logic():
    print("Game Running")

    color = 0
    if(grid[0][0] == 0):    
        color = 1

    grid[0][0] = color
    draw_grid(canvas)

    root.after(100, game_logic)

def draw_square(canvas, x, y, size, color):
    canvas.create_rectangle(x, y, x + size, y + size, fill=color, outline=color)

def draw_grid(canvas):
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            x = j * square_size
            y = i * square_size
            draw_square(canvas, x, y, square_size, colors[value])

def on_keypress(event):
    key = event.keysym
    print("Key:", key)

rows = 5
cols = 5
square_size = 40
colors = {1: "black", 0: "white"}
grid = [ [0]*rows for i in range(cols)]

if __name__ == "__main__":
    # Canvas setup
    canvas = tk.Canvas(root, width=len(grid[0])*square_size, height=len(grid)*square_size)
    canvas.pack()

    # Main loop
    draw_grid(canvas)

    root.bind("<KeyPress>", on_keypress)
    root.after(100, game_logic)

    root.mainloop()