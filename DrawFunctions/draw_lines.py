import tkinter as tk

class draw_line():
    def __init__(self, a_coordinates, a_color):
        self.coordinates = a_coordinates
        self.color = a_color

    def draw(self, a_canvas):
        #draws a line
        a_canvas.create_line(*self.coordinates, fill = self.color)

    def draw_lines_num_of_letters(self, a_num_of_letters):
        pass