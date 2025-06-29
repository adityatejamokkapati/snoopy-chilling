
import tkinter as tk
from PIL import Image, ImageTk
import random

FRAME_COUNT = 6
FRAME_DELAY = 100
MOVE_DELAY = 50
SPRITE_WIDTH = 69
SPRITE_HEIGHT = 67

root = tk.Tk()

class SnoopyApp:
    def __init__(self, root):
        self.root = root
        # frm = tk.Frame(root, padx=10, pady=10)
        # frm.grid()
        # tk.Label(frm, text="Hello World!").grid(column=0, row=0)
        # tk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)


        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-alpha", 0.5)

        self.label = tk.Label(root, bg="black", bd=0)
        self.label.pack()

        self.frame_index = 0
        self.frames = self.load_frames()

        screen_w = root.winfo_screenwidth()
        screen_h = root.winfo_screenheight()
        self.pos_x = random.randint(100, screen_w - 100)
        self.pos_y = random.randint(100, screen_h - 100)
        self.dx = 2
        self.dy = 2

        self.animate()
        self.move()
        self.root.mainloop()


    def load_frames(self):
        frames = []
        
        for i in range(FRAME_COUNT):
            img = Image.open(f"snoopy_frame_{i+1}.png")
            tk_img = ImageTk.PhotoImage(img, master=self.root)
            frames.append(tk_img)
        return frames

    def animate(self):
        self.label.config(image=self.frames[self.frame_index])
        self.frame_index = (self.frame_index + 1) % FRAME_COUNT
        self.root.after(FRAME_DELAY, self.animate)

    def move(self):
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()

        if not (0 < self.pos_x < screen_w - SPRITE_WIDTH):
            self.dx = -self.dx
        if not (0 < self.pos_y < screen_h - SPRITE_HEIGHT):
            self.dy = -self.dy

        self.pos_x += self.dx
        self.pos_y += self.dy
        self.root.geometry(f"{SPRITE_WIDTH}x{SPRITE_HEIGHT}+{self.pos_x}+{self.pos_y}")
        self.root.after(MOVE_DELAY, self.move)



snoopy = SnoopyApp(root)