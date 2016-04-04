import tkinter as tk
from DrawFunctions.draw_lines import draw_line
import GameLevels.MenuLevel
from Styles.FontStyle import font_style

class GameLevel(tk.Frame):
    def __init__(self, a_parent, a_controller):

        parent = a_parent
        controller = a_controller

        print("Game Level")

        #font style
        _large_font = font_style.get_label_header_style(self)

        #change the title to easy level
        a_controller.change_title("Easy Level")

        #init the tk and inherit
        tk.Frame.__init__(self, a_parent)

        label = tk.Label(self, text="Level: Easy", font = _large_font)
        label.grid(row=0, column =0, sticky = 'n')

        button1 = tk.Button(self, text = "Back to Home",
                            command = lambda: a_controller.show_frame(GameLevels.MenuLevel.MenuLevel))
        button1.grid(row = 4, column = 0, sticky = 'w')

        #adding canvas for player interaction
        w = tk.Canvas(self, width=600, height=400, bg= 'black')
        w.grid(row = 0, column = 1, stick = 'w')

        d1 = draw_line((20,100,40,120), 'white')
        d1.draw(w)
        #w.create_line(0,100,0,120, fill = 'white')






