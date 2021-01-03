import os


class FileManager:
    OPEN_FILE_CODE = 0
    OPEN_FOLDER_CODE = 1

    def __init__(self, start_path:int, history:list=[]) -> None: 
        self._current_path = ""
        self._history = []
        self.current_code = self.OPEN_FOLDER_CODE
        
        self._add_path(start_path)

        print("started file_manager at {}".format(start_path))

    def _add_path(self, path_name:str) -> None:
        if not os.path.exists(path_name):
            raise ValueError("Несуществующая папка")

        self._current_path = path_name
        self._history.append(path_name)

    def _step_back(self):
        self._history.pop()
        if len(self._history) == 0:
            raise IndexError("Дальше нельзя")
        self._current_path = self._history[-1]

    def _get_new_path(self, file_name:str) -> None:
        return os.path.join(self._current_path, file_name)

    def _open_folder(self, new_path:str) -> str:
        self.current_code = self.OPEN_FOLDER_CODE
        return new_path

    def _open_file(self, new_path:str) -> str:
        self.current_code = self.OPEN_FILE_CODE
        return new_path

    def ls(self) -> list:
        return os.listdir(self.current_path)

    def open_(self, name:str) -> str:
        new_path = self._get_new_path(name)
        print("open", new_path)

        self._add_path(new_path)

        if os.path.isfile(new_path):
            return self._open_file(new_path)

        return self._open_folder(new_path)

    def step_back(self):
        self._step_back()
    
    def current_is_folder(self):
        return self.current_code == self.OPEN_FOLDER_CODE

    @property
    def current_path(self) -> str:
        return self._current_path

    @property
    def can_go_back(self):
        return len(self._history) > 0