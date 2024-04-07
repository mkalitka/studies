import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


class SnakeGame:
    def __init__(self, size=10):
        self.size = size
        self.snake = [(0, 0)]
        self.direction = np.random.choice(["up", "down", "left", "right"])
        self.food = self.generate_food()
        self.ani = None

    def generate_food(self):
        while True:
            food = (np.random.randint(0, self.size), np.random.randint(0, self.size))
            if food not in self.snake:
                return food

    def update_screen(self):
        plt.clf()
        plt.title("Snake")
        plt.xlim(0, self.size)
        plt.ylim(0, self.size)

    def update(self, frame):
        self.update_screen()

        head = self.snake[0]
        if self.direction == "up":
            new_head = (head[0], (head[1] + 1) % self.size)
        elif self.direction == "down":
            new_head = (head[0], (head[1] - 1) % self.size)
        elif self.direction == "left":
            new_head = ((head[0] - 1) % self.size, head[1])
        elif self.direction == "right":
            new_head = ((head[0] + 1) % self.size, head[1])

        if new_head == self.food:
            self.snake.insert(0, new_head)
            self.food = self.generate_food()
        elif new_head in self.snake:
            self.game_over()
            return

        self.snake.insert(0, new_head)
        if len(self.snake) > 1:
            if new_head != self.food:
                self.snake.pop()

        for segment in self.snake:
            plt.fill_between(
                [segment[0], segment[0] + 1], segment[1], segment[1] + 1, color="blue"
            )

        plt.fill_between(
            [self.food[0], self.food[0] + 1],
            self.food[1],
            self.food[1] + 1,
            color="red",
        )

    def on_key(self, event):
        if event.key in ["up", "down", "left", "right"]:
            self.direction = event.key

    def game_over(self):
        plt.clf()
        plt.axis("off")
        plt.text(0.5, 0.5, "Game Over", horizontalalignment="center", verticalalignment="center")
        self.ani.event_source.stop()

    def start(self):
        fig, ax = plt.subplots(figsize=(5, 5))
        fig.canvas.mpl_connect("key_press_event", self.on_key)

        self.ani = animation.FuncAnimation(fig, self.update, frames=100000, interval=350, repeat=False)
        plt.show()


if __name__ == "__main__":
    game = SnakeGame()
    game.start()
