import logging
from Engine.utilities.dir_path_provider import dir_path
class Logger:
    logger=None
    def __init__(self):

        self.path="/Reports/logs/logs.txt"
        logging.basicConfig(filename=dir_path().get_path()+self.path,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %T:%M:%S %p'
                            )
        Logger.logger=logging.getLogger()
        Logger.logger.setLevel(logging.DEBUG)

    @staticmethod
    def log_debug(message):
        Logger.logger.debug(message)

    @staticmethod
    def log_info(message):
        Logger.logger.info(message)

    @staticmethod
    def log_warning(message):
        Logger.logger.warning(message)

    @staticmethod
    def log_error(message):
        Logger.logger.error(message)

    @staticmethod
    def log_critical(message):
        Logger.logger.critical(message)