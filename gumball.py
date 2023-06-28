import tkinter as tk
import random

class GumballGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Gumball Game")

        self.gumball_colors = ["red", "blue", "green", "yellow", "orange", "purple"]
        self.current_color = ""

        self.color_label = tk.Label(self.master, text="Press the button to get a gumball!", font=("Arial", 16))
        self.color_label.pack(pady=10)

        self.button = tk.Button(self.master, text="Get Gumball", command=self.get_gumball)
        self.button.pack(pady=10)

    def get_gumball(self):
        self.current_color = random.choice(self.gumball_colors)
        self.color_label.config(text="You got a {} gumball!".format(self.current_color), fg=self.current_color)

if __name__ == "__main__":
    root = tk.Tk()
    game = GumballGame(root)
    root.mainloop()
