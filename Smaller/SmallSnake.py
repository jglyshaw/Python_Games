import tkinter as tk, random

user_input = ""
rows, cols, size = 20, 10, 10
grid, apple, snake = [[0]*cols for _ in range(rows)], [], [[rows//2, cols//2]]

def create_block(cord, color):
    x, y = cord[0] * size, cord[1] * size
    grid[cord[0]][cord[1]] = canvas.create_rectangle(x, y, x + size, y + size, fill=color)

def delete_block(cord):
    canvas.delete(grid[cord[0]][cord[1]])
    grid[cord[0]][cord[1]] = 0

def inside_grid(cord):
    return 0 <= cord[0] < rows and 0 <= cord[1] < cols

def start_game():
    create_block(snake[0], "white")
    add_apple()
    game_loop()
    root.mainloop()

def on_keypress(event):
    global user_input
    user_input = event.keysym

def game_loop():
    global apple
    directions = {"d": [1, 0], "a": [-1, 0], "s": [0, 1], "w": [0, -1]}
    if user_input in directions:
        new_head = [snake[0][i] + directions[user_input][i] for i in range(2)]
        if inside_grid(new_head) and new_head not in snake[1:]:
            if new_head == apple:
                delete_block(apple)
                apple = []
            else:
                delete_block(snake.pop())
            create_block(new_head, "white")
            snake.insert(0, new_head)
            if not apple: add_apple()
    root.after(100, game_loop)

def add_apple():
    global apple
    while True:
        cord = [random.randint(0, rows-1), random.randint(0, cols-1)]
        if grid[cord[0]][cord[1]] == 0:
            apple = cord
            create_block(cord, "red")
            break

root = tk.Tk()
root.title("Snake Game")
root.bind("<KeyPress>", on_keypress)
canvas = tk.Canvas(root, bg='black', width=rows*size, height=cols*size)
canvas.pack()
start_game()
