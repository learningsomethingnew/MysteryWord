from Tkinter import *

class Rectangle():
    def __init__(self, coords, color):
        self.coords = coords
        self.color = color

    def draw(self, canvas):
        """Draw the rectangle on a Tk Canvas."""
        canvas.create_rectangle(*self.coords, fill=self.color)

master = Tk()
w = Canvas(master, width=300, height=300)
w.pack()

rect1 = Rectangle((0, 0, 100, 100), 'blue')
rect1.draw(w)

mainloop()