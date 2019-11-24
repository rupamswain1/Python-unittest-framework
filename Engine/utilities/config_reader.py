from configparser import ConfigParser
from Engine.utilities.dir_path_provider import dir_path


class ReadConfig:
    @staticmethod
    def get_property(data,section="driver_data"):
        config_file_path="/Resources/config/config.ini"
        config = ConfigParser()
        config.read(dir_path.get_path()+config_file_path)

        # read values from a section
        data = config.get(section,data)
        return data


