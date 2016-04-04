import tkinter as tk
from tkinter import ttk
import GameLevels.MenuLevel
import GameLevels.GameLevel


class UserInterface(tk.Tk):

#framework for controlling screens
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0 , weight = 1)

        self.frames = {}

        for level in (GameLevels.MenuLevel.MenuLevel, GameLevels.GameLevel.GameLevel):
            frame = level(container, self)
            self.frames[level] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(GameLevels.MenuLevel.MenuLevel)

#Shows the frame that we want. a_controller is the key to the value in our dictionary that is our frame
    def show_frame(self, a_controller):
        frame = self.frames[a_controller]
        frame.tkraise()

#changes the title of the screen to match what the player is on
    def change_title(self, a_string):
        tk.Tk.wm_title(self,a_string)



app = UserInterface()
app.mainloop()

