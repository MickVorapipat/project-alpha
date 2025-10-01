import tkinter as tk
import random
import time

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Matching Game")
        self.size = 4  # 4x4 grid
        self.images = list(range(1, 9)) * 2  # 8 pairs
        random.shuffle(self.images)
        self.buttons = []
        self.flipped = []
        self.matched = set()
        self.create_board()

    def create_board(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                btn = tk.Button(self.root, text="", width=8, height=4,
                                command=lambda i=i, j=j: self.on_click(i, j), font=("Arial", 16))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)

    def on_click(self, i, j):
        idx = i * self.size + j
        if idx in self.matched or idx in [f[0] for f in self.flipped]:
            return
        self.buttons[i][j].config(text=str(self.images[idx]), state="disabled")
        self.flipped.append((idx, (i, j)))
        if len(self.flipped) == 2:
            self.root.after(500, self.check_match)

    def check_match(self):
        idx1, pos1 = self.flipped[0]
        idx2, pos2 = self.flipped[1]
        if self.images[idx1] == self.images[idx2]:
            self.matched.add(idx1)
            self.matched.add(idx2)
        else:
            self.buttons[pos1[0]][pos1[1]].config(text="", state="normal")
            self.buttons[pos2[0]][pos2[1]].config(text="", state="normal")
        self.flipped = []
        if len(self.matched) == self.size * self.size:
            self.show_win()

    def show_win(self):
        win_label = tk.Label(self.root, text="คุณชนะแล้ว!", font=("Arial", 24), fg="green")
        win_label.grid(row=self.size, column=0, columnspan=self.size)

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
