import os


class FileManager:
    def __init__(self, start_path:int, history:list=[]) -> None: 
        self._current_path = start_path
        self._history = history or []
        print("started file_manager at {}".format(start_path))

    def _add_path(self, path_name:str) -> None:
        if not os.path.exists(path_name):
            raise ValueError("Несуществующая папка")

        self._current_path = path_name
        self._history.append(path_name)
        

    def _get_new_path(self, file_name:str) -> None:
        return os.path.join(self._current_path, file_name)

    def open_folder(self, folder_name:str) -> str:
        new_path = self._get_new_path(folder_name)
        self._add_path(new_path)

        return new_path

    def open_file(self, file_name:str) -> str:
        new_path = self._get_new_path(file_name)
        self._add_path(new_path)

        return new_path
    
    def ls(self) -> list:
        return os.listdir(self.current_path)

    @property
    def current_path(self):
        return self._current_path