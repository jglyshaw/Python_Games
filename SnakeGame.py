from GameBase import GameBase

class Snake(GameBase):

    def __init__(self, rows, cols, size, refresh_rate = 100):
        super().__init__(rows, cols, size, refresh_rate)
        self.snake = []

    def start_game(self):
        head = [5,5]
        self.snake.append(head)
        self.create_square(head, "black")
        
        self.game_loop()
        self.root.mainloop()

    def game_loop(self):
        # Game logic methods
        self.user_action()

        # Continue game loop again
        self.root.after(self.refresh_rate, self.game_loop)

    def user_action(self):
        user_input = self.get_user_input()
        head = self.snake[0]
        tail = self.snake[-1]
        new_head = list(head)

        if(user_input == "d"):
            new_head[0] += 1
        elif(user_input == "a"):
            new_head[0] -= 1
        elif(user_input == "s"):
            new_head[1] += 1
        elif(user_input == "w"):
            new_head[1] -= 1

        if(self.inside_grid(new_head)):
            # Delete last segment
            self.delete_square(tail)
            self.snake.pop(-1)

            # Add new segment
            self.create_square(new_head, "black")
            self.snake.insert(0, new_head)


if __name__ == "__main__":
    game = Snake(20, 20, 50)
    game.start_game()