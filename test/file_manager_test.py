import unittest

from file_manager import FileManager


class FileManagerTest(unittest.TestCase):
    def setUp(self):
        self.path = "/Users/michil/fanprojects/custom_file_manager/test/test_folder"
        self.file_manager = FileManager(self.path)

    def test_current_path(self):
        self.assertEqual(
            self.file_manager.current_path,
            "/Users/michil/fanprojects/custom_file_manager/test/test_folder"
        )

    def test_open_exist_folder(self):
        self.file_manager.open_('folder')

        self.assertEquals(
            self.file_manager.current_path,
            "/Users/michil/fanprojects/custom_file_manager/test/test_folder/folder"
        )

        self.assertCountEqual(
            self.file_manager.ls(),
            ['new_file.py']
        )

    def test_open_non_exist_folder(self):
        with self.assertRaises(ValueError):
            self.file_manager.open_('non-exist_folder')

    def test_ls(self):
        self.assertCountEqual(
            self.file_manager.ls(),
            ['abs.py', 'folder']
        )