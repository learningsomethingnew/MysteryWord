import tkinter as tk
from tkinter import ttk
from GameLevels.menu_level import menu_level
from GameLevels.game_level import game_level
from Styles import FontStyle


class UserInterface(tk.Tk):

#framework for controlling screens
    def __init__(self, *args, **kwargs):

        #import font styles
        _large_font = FontStyle.font_style.get_label_header_style(self)

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0 , weight = 1)

        self.frames = {}

        for level in (menu_level, game_level, normal_level):
            frame = level(container, self)
            self.frames[level] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(menu_level)

#Shows the frame that we want. a_controller is the key to the value in our dictionary that is our frame
    def show_frame(self, a_controller):
        frame = self.frames[a_controller]
        frame.tkraise()

#changes the title of the screen to match what the player is on
    def change_title(self, a_string):
        tk.Tk.wm_title(self,a_string)


# class menu_level(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self,parent)
#
#         controller.change_title("Main Menu")
#
#         label = tk.Label(self, text="Menu Level", font=_large_font)
#         label.pack(pady=10,padx=10)
#
#         button = tk.Button(self, text="Easy Level",
#                             command=lambda: controller.show_frame(game_level))
#         button.pack()
#
#         button2 = tk.Button(self, text="Normal Level",
#                             command=lambda: controller.show_frame(normal_level))
#         button2.pack()

#easy_level
# class game_level(tk.Frame):
#     def __init__(self, a_parent, a_controller):
#
#         #change the title to easy level
#         a_controller.change_title("Easy Level")
#
#         #init the tk and inherit
#         tk.Frame.__init__(self, a_parent)
#
#         label = tk.Label(self, text="Level: Easy", font = _large_font)
#         label.grid(row=0, column =0, sticky = 'n')
#
#         button1 = tk.Button(self, text = "Back to Home",
#                             command = lambda: a_controller.show_frame(menu_level))
#         button1.grid(row = 4, column = 0, sticky = 'w')
#
#         #adding canvas for player interaction
#         w = tk.Canvas(self, width=600, height=400)
#         w.grid(row = 0, column = 1, stick = 'w')
#         #w.create_line(0, 100, 200, 0, fill="red", dash=(9, 9))
#         line1 = draw_line((100,100, 125, 100), 'black')
#         line1.draw(w)



#normal game level
class normal_level(tk.Frame):
    def __init__(self, a_parent, a_controller):
        tk.Frame.__init__(self, a_parent)
        label = tk.Label(self, text="Normal Level", font = _large_font)
        label.pack(pady = 10, padx = 10)
        button1 = tk.Button(self, text = "Back to Home",
                            command = lambda: a_controller.show_frame(menu_level))
        button1.pack()


class draw_line():
    def __init__(self, a_coordinates, a_color):
        self.coordinates = a_coordinates
        self.color = a_color

    def draw(self, canvas):
        canvas.create_line(*self.coordinates, fill = self.color)


#class hard_level(tk.Frame):
    #pass

app = UserInterface()
app.mainloop()

