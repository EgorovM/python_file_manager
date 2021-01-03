import os
import tkinter as tk
from PIL import ImageTk, Image

from file_manager import FileManager


class GUIWidget:
    def view(self):
        raise NotImplementedError


class PathWidget(GUIWidget):
    def __init__(self, file_manager, window):
        self._file_manager = file_manager

        self.frame = tk.Frame(master=window)
        self.path_widget = tk.Label(master=self.frame)

    def set_path(self):
        self.path_widget['text'] = self._file_manager.current_path

    def view(self):
        self.path_widget.pack()
        self.frame.place(x=0, y=610)


class FilesWidget(GUIWidget):
    def __init__(self, screen, file_manager: FileManager, window, column_count=3):
        self._screen = screen
        self._column_count = column_count
        self._file_manager = file_manager

        self._folder_icon = Image.open('static/folder_pic.png').resize((32, 32))
        self._file_icon   = Image.open('static/file_pic.png').resize((32, 32))

        self._files = []
        self._files_widgets = []

        self.frame = tk.Frame(master=window)
        self.files_frm = tk.Frame(master=self.frame)
        self.step_back_btn = tk.Button(master=self.frame, text="<-", command=lambda: self._step_back())
        self.update_files()
    
    def _open(self, name):
        print("Нажали на", name)
        self._file_manager.open_(name)
        self.update_files()

    def _step_back(self):
        self._screen._step_back()

    def _erase_files_widgets(self):
        [file_widget.destroy() for file_widget in self.files_frm.winfo_children()]
        self._files_widgets = []

    def _view_files(self):
        for i, widget in enumerate(self._files_widgets):
            widget.grid(row=i//self._column_count, 
                        column=i%self._column_count)

    def _view(self):
        self.frame.pack()
        self.step_back_btn.pack()
        self._view_files()
        self.files_frm.pack()

    def _file_widget(self, name):
        new_path = self._file_manager._get_new_path(name)

        command = lambda event, name=name: self._screen._open(name)
        frame = tk.Frame(master=self.files_frm)

        icon_type = self._file_icon if os.path.isfile(new_path) else self._folder_icon
        
        icon = ImageTk.PhotoImage(icon_type)
        label = tk.Label(master=frame, image=icon)
        label.photo = icon
        label.bind("<Button-1>", command)
        label.pack()

        tk.Label(master=frame, text=name).pack()

        return frame

    def update_files(self):
        self._files = self._file_manager.ls()
        self._erase_files_widgets()

        for name in self._files:
            self._files_widgets.append(
                self._file_widget(name)
            )
        
        self._view_files()

    def view(self):
        self._view()


class Screen(GUIWidget):
    def __init__(self, file_manager, window):
        self._file_manager = file_manager

        self._w_path = PathWidget(file_manager, window)
        self._w_files = FilesWidget(self, file_manager, window)
        self._w_path.set_path()

    def _open(self, name):
        print("Открываю файл:", name)
        self._w_files._open(name)
        self._w_path.set_path()

    def _step_back(self):
        self._file_manager.step_back()
        self._w_files.update_files()
        self._w_path.set_path()

    def view(self):
        self._w_files.view()
        self._w_path.view()