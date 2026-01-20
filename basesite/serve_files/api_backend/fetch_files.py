import os

class FileList:
    def __init__(self, file_list):
        self._file_list = file_list

    @property
    def file_list(self):
        return self._file_list


class RFile:
    def __init__(self, f_path, f_type):
        self.f_path = f_path
        self.f_type = f_type

    def fetch(self):
        """
        Method to walk a directory and gather a list of files
        based on the selected type.
        :return: List containing file names
        """
        # init empty lists
        type_list = []
        file_list = []

        # create type list based on user selected type
        if self.f_type == "images":
            type_list = ['.jpg', '.png', '.gif']
        elif self.f_type == "videos":
            type_list = ['.mp4', '.avi', '.mkv']
        elif self.f_type == "audio":
            type_list = ['.mpg', '.mpeg']
        elif self.f_type == "documents":
            type_list = ['.pdf', '.doc', '.docx', '.txt']
        elif self.f_type == "misc":
            type_list = ['.log']

        # walk user provided directory and look for files with
        # correct type ending
        for l_type in type_list:
            for root, dirs, files in os.walk(self.f_path):
                for file in files:
                    if file.endswith(l_type):
                        file_list.append(file)

        return file_list

