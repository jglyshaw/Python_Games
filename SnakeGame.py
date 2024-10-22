from GameBase import GameBase
import os

class Snake(GameBase):

    def __init__(self, rows, cols, size, refresh_rate = 150):
        super().__init__(rows, cols, size, refresh_rate)
        self.apple = []
        self.snake = []

        base_path = os.path.dirname(os.path.abspath(__file__))
        self.apple_image = base_path + "apple.png"

        self.setup_game()

    def setup_game(self):
        self.delete_all()

        snake_head = [self.random_row(), self.random_col()]
        self.snake = [snake_head]
        self.create_block(snake_head, "black")
        
        self.apple = []
        self.add_apple()


    def game_loop(self):
        # Update the snake
        self.move_snake()
      
        # If there's no apple make a new one
        if(self.apple == []):
           self.add_apple()


    def add_apple(self):
        success = False
        apple_cord = []
        
        while(not success):
            apple_cord = [self.random_row(), self.random_col()]
            success = not self.block_exists(apple_cord)

        self.apple = apple_cord
        self.create_image_block(apple_cord, self.apple_image)
        
    def move_snake(self):
        user_input = self.get_user_input()
        new_head = list(self.snake[0])

        if(user_input == "d"):
            new_head[0] += 1
        elif(user_input == "a"):
            new_head[0] -= 1
        elif(user_input == "s"):
            new_head[1] += 1
        elif(user_input == "w"):
            new_head[1] -= 1

        # Prevent movement into self or wall
        if(not self.inside_grid(new_head) or new_head in self.snake[1:]):
            self.setup_game()

        else:
            # If we eat an apple delete it, else delete the tail
            if(new_head == self.apple):
                self.delete_block(self.apple)
                self.apple = []
            else:
                self.delete_block(self.snake.pop())

            # Update where the new head is
            self.create_block(new_head, "white")
            self.snake.insert(0, new_head)

            # Change the second segment to a different color
            if(len(self.snake) > 1):
                self.change_block_color(self.snake[1], "gray")

if __name__ == "__main__":
    game = Snake(20, 15, 30)
    game.start_game()
