from GameBase import GameBase
import random

class Snake(GameBase):

    def __init__(self, rows, cols, size, refresh_rate = 100):
        super().__init__(rows, cols, size, refresh_rate)
        
        self.apple = []
        self.snake = []

        snake_head = [5,5]
        self.snake.append(snake_head)
        self.create_square(snake_head, "black")
        self.add_apple()

    def game_loop(self):
        # Game logic methods
        self.user_action()

        # Continue game loop again
        self.root.after(self.refresh_rate, self.game_loop)

    def add_apple(self):
        success = False
        apple_cord = []
        
        while(not success):
            row = random.randint(0, self.rows-1)
            col = random.randint(0, self.cols-1)
            apple_cord = [row,col]
            success = not self.square_exists(apple_cord)

        self.apple = apple_cord
        self.create_square(apple_cord, "red")
        

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

        if(self.inside_grid(new_head)):
   
            if(new_head == self.apple):
                self.delete_square(self.apple)
                self.apple = []
            else:
                self.delete_square(tail)
                self.snake.pop(-1)

            # Update the head
            self.create_square(new_head, "green")
            self.snake.insert(0, new_head)

            if(self.apple == []):
                self.add_apple()

if __name__ == "__main__":
    game = Snake(20, 20, 40)
    game.start_game()