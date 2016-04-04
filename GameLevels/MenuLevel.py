import tkinter as tk
from GameLevels.GameLevel import GameLevel

_large_font = ("Verdana", 12)

class MenuLevel(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        controller.change_title("Main Menu")

        label = tk.Label(self, text="Menu Level", font=_large_font)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Easy Level",
                            command=lambda: controller.show_frame(GameLevel))
        button.pack()
