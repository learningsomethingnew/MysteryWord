import tkinter as tk
from tkinter import ttk

class UserInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.init_window()



#generic function to change the background color
    def set_bgc(self, a_color):
        self.window.configure(background = a_color)

#generic function to change the window size
    def set_window_size(self, a_size):
        self.window.geometry(a_size)

#generic function to change the window title
    def set_window_title(self, a_string):
        self.window.title(a_string)

#generic function to create a button
    def create_button(self, a_name_for_button, a_x, a_y, a_command, a_button_state):
        temp = tk.Button(text = a_name_for_button,command = a_command, state=a_button_state)
        temp.place(x = a_x, y = a_y)
        return temp

#fucntion to quit the app
    def quit_app(self):
        exit()

#init the window settings
    def init_window(self):
        #sets the title
        self.set_window_title("TIY Hangman Edition")
        #sets the window size
        self.set_window_size("800x600")
        #sets the background color
        self.set_bgc('black')

#main loop for controlling the gui
    def draw_main_window(self):
        self.window.mainloop()

if __name__ == '__main__':
    f = UserInterface()
    f.create_button("Test Button", 0, 10, f.quit_app, "disabled")
    f.draw_main_window()
