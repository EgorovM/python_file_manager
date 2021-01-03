import os
import pathlib
import tkinter as tk

from file_manager import FileManager
from widgets import Screen


class GUI:
    def __init__(self, width, height, current_path):
        self._width = width
        self._height = height
        
        self.window = tk.Tk()
        self.window.geometry("{}x{}".format(width, height))

        self.file_manager = FileManager(current_path)
        self._display_widgets()

    @property
    def current_path(self):
        return self.file_manager.current_path

    def _display_widgets(self):
        self.screen = Screen(self.file_manager, self.window)
        self.screen.view()

    def run(self):
        self.window.mainloop()

    def __str__(self):
        return "GUI tkinter"

if __name__ == "__main__":
    gui = GUI(640, 640, pathlib.Path().absolute())
    gui.run()


    