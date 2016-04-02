import tkinter as tk

class UserInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Random Letters")
        self.window.geometry("800x600")

    def draw_main_window(self):
        self.window.mainloop()

if __name__ == '__main__':
    f = UserInterface()
    f.draw_main_window()