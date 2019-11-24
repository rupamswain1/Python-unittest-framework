from Engine.locator_assigner.locator_fetcher import webelement
from Engine.structures.webpage import Webpage
from Engine.driver_manager.initialize import InitializeDriver
class LoginPage(Webpage):

    def open_webpage(self):
        self.driver=InitializeDriver().start_driver()

    def __init__(self):
       self._close_pop_up="LoginPage.closePopUp"
       self.driver=None

    def get_close_pop_up(self):
        webelement().get_locator(self.driver,self._close_pop_up).click()

    def get_driver(self):
        return self.driver

