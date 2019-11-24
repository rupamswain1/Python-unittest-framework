import abc
from abc import ABC,abstractmethod
from Engine.driver_manager.initialize import InitializeDriver
class Webpage(ABC):
    drive=None
    def __init__(self):
        self.driver=None
    @abstractmethod
    def open_webpage(self):
        InitializeDriver.start_driver()
    @abstractmethod
    def get_driver(self):
        pass
