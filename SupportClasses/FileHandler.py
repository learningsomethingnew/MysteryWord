#This class handles all file related things
#Open File
#Test if file exists

from os import path
import os

class FileHanlder:
    def __init__(self):
        #importing path to determine if file is there
        self._dictionary = "/usr/share/dict/words"
        self._current_dir = os.getcwd()


    def open_dictionary():
        with open('sample1.txt', 'r') as f:
            for line in f:
                line = clean_line(line)
                a_list = split_string(line)
                a_list = scrub_list_for_empty_entries(a_list)
                print(a_list)

    def test_if_file_exists(self, a_file_location):
        return path.isfile(a_file_location)

    def create_file_if_none_exists(self, a_directory):
        pass
#Runs tests on the functions to make sure that they work
if __name__ == '__main__':
    f = FileHanlder()
    print(f.test_if_file_exists("/usr/share/dict/words"))
    print(f._current_dir)