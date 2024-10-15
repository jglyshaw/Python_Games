from GameBase import GameBase
import random

class Snake(GameBase):

    def __init__(self, rows, cols, size, refresh_rate = 150):
        super().__init__(rows, cols, size, refresh_rate)
        
        self.apple = []
        self.snake = []

        snake_head = [int(rows/2), int(cols/2)]
        self.snake.append(snake_head)
        self.create_block(snake_head, "black")
        self.add_apple()

    def game_loop(self):
        self.user_action()

    def add_apple(self):
        success = False
        apple_cord = []
        
        while(not success):
            row = random.randint(0, self.rows-1)
            col = random.randint(0, self.cols-1)
            apple_cord = [row,col]
            success = not self.block_exists(apple_cord)

        self.apple = apple_cord
        self.create_block(apple_cord, "red", "circle")
        
    def user_action(self):
        user_input = self.get_user_input()
        snake_head = self.snake[0]
        tail = self.snake[-1]
        new_head = list(snake_head)

        if(user_input == "d"):
            new_head[0] += 1
        elif(user_input == "a"):
            new_head[0] -= 1
        elif(user_input == "s"):
            new_head[1] += 1
        elif(user_input == "w"):
            new_head[1] -= 1

        # If ran into self, lost
        if(self.inside_grid(new_head) and not new_head in self.snake[1:]):

            # If we ate an apple delete it, else delete the tail
            if(new_head == self.apple):
                self.delete_block(self.apple)
                self.apple = []
            else:
                self.delete_block(tail)
                self.snake.pop(-1)

            # Update where the new head is
            self.create_block(new_head, "white")
            self.snake.insert(0, new_head)

            # Change the second element to a different color
            if(len(self.snake) > 1):
                self.change_block_color(self.snake[1], "gray")

            # If there's no apple make a new one
            if(self.apple == []):
                self.add_apple()

if __name__ == "__main__":
    game = Snake(20, 15, 20)
    game.start_game()
