#This class handles all file related things
#Open File
#Test if file exists

from os import path
import os

class FileHanlder:

#importing path to determine if file is there
    def __init__(self):
        self._dictionary = "/usr/share/dict/words"
        self._current_dir = os.getcwd()

#Tests to see if file exists. Afterwards, it opens it, reads line by line, and then adds it to a dictionary.
    def open_file(self):
        if self.test_if_file_exists(self._dictionary):
            with open(self._dictionary, 'r') as f:
                for line in f:
                    return line


    def test_if_file_exists(self, a_file):
        return path.isfile(a_file)

    def create_file_if_none_exists(self, a_directory):
        pass

#Runs tests on the functions to make sure that they work
if __name__ == '__main__':
    f = FileHanlder()
