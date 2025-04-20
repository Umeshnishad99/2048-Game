import tkinter as tk
import random
import constants as c
# import login

class Game2048:
    def __init__(self, master):
        self.master = master
        self.master.title("2048 Game")
        self.master.resizable(False, False)

        self.grid_len = c.GRID_LEN
        self.grid_size = c.SIZE
        self.grid_padding = c.GRID_PADDING
        self.cell_size = (self.grid_size - (self.grid_len + 1) * self.grid_padding) / self.grid_len

        self.game = login.new_game(self.grid_len)
        self.score = 0

        self.canvas = tk.Canvas(self.master, width=self.grid_size, height=self.grid_size, bg=c.BACKGROUND_COLOR_GAME)
        self.canvas.pack()

        self.update_display()

        self.master.bind("<KeyPress>", self.key_pressed)

    def update_display(self):
        """Update the game grid display on the canvas."""
        self.canvas.delete("all")

        for i in range(self.grid_len):
            for j in range(self.grid_len):
                value = self.game[i][j]
                x1 = j * (self.cell_size + self.grid_padding) + self.grid_padding
                y1 = i * (self.cell_size + self.grid_padding) + self.grid_padding
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                # Background color for the cells
                bg_color = c.BACKGROUND_COLOR_CELL_EMPTY if value == 0 else c.BACKGROUND_COLOR_DICT.get(value, "#edc22e")
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=bg_color, outline=c.BACKGROUND_COLOR_GAME)

                # Cell values (text)
                if value != 0:
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(value), font=c.FONT)

        self.update_score()

    def update_score(self):
        """Display the score on the canvas."""
        self.canvas.create_text(self.grid_size / 2, self.grid_size - 40, text=f"Score: {self.score}", font=("Verdana", 20, "bold"))

    def key_pressed(self, event):
        """Handle user input."""
        move = None

        if event.keysym == "Up" or event.keysym == "w":
            move = "Up"
        elif event.keysym == "Down" or event.keysym == "s":
            move = "Down"
        elif event.keysym == "Left" or event.keysym == "a":
            move = "Left"
        elif event.keysym == "Right" or event.keysym == "d":
            move = "Right"

        if move:
            self.make_move(move)

    def make_move(self, move):
        """Make a move and update the game state."""
        self.game, moved = login.MOVE_FUNCTIONS[move](self.game)

        if moved:
            self.game = login.add_two(self.game)
            self.score = login.get_score(self.game)
            self.update_display()

            state = login.game_state(self.game)
            if state == "win":
                self.show_game_over("You Win!")
            elif state == "lose":
                self.show_game_over("Game Over!")

    def show_game_over(self, message):
        """Display the game over message."""
        self.canvas.create_text(self.grid_size / 2, self.grid_size / 2, text=message, font=("Verdana", 30, "bold"))

def main():
    root = tk.Tk()
    app = Game2048(root)
    root.mainloop()

if __name__ == "__main__":
    main()
