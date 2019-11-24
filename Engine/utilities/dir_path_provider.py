import os
class dir_path:
    @staticmethod
    def get_path():
        dirname = os.path.dirname(os.path.realpath('__file__'))
        dirname = dirname.split("\\")
        dirname.pop(len(dirname) - 1)
        dirname.pop(len(dirname) - 1)
        dirname = "\\".join(dirname)
        return dirname