from os import path

from django.test import TestCase

from honey.mako.loaders import MakoFileSystemLoader, MakoAppDirLoader

class LoaderTester(object):
    def _load_file_name(self, input_path, *path_parts):
        loader = self.loader_class()
        _, actual = loader.load_template(input_path)
        expected = path.realpath(path.join(path.dirname(__file__), *path_parts))
        self.assertEqual(actual, expected)


class test_MakoFileSystemLoader(TestCase, LoaderTester):
    loader_class = MakoFileSystemLoader

    def test_load_from_root(self):
        self._load_file_name("root_project.mako", 'templates', 'root_project.mako')

    def test_load_from_sub_folder(self):
        self._load_file_name("an_app/sub_folder_project.mako", 'templates', 'an_app', 'sub_folder_project.mako')


class test_MakoAppDirLoader(TestCase, LoaderTester):
    loader_class = MakoAppDirLoader

    def test_load_from_root(self):
        self._load_file_name("root_app.mako", 'testapp', 'templates', 'root_app.mako')

    def test_load_from_sub_folder(self):
        self._load_file_name("sub_folder/sub_folder_app.mako", 'testapp', 'templates', 'sub_folder', 'sub_folder_app.mako')
