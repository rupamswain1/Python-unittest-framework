from Engine.utilities.config_reader import ReadConfig
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

class InitializeDriver:



    def __init__(self):
        self.driver_name=ReadConfig.get_property("driver").lower()
        self.driver_path=ReadConfig.get_property("driver_path").lower()
        self.driver_window_mode=ReadConfig.get_property("driver_window_size").lower()
        self.url=ReadConfig.get_property("url","execution_data").lower()
        self.driver_implicit_wait=ReadConfig.get_property(("driver_implicit_wait"))
        self.base_driver = None

    def start_driver(self):
        _driver=None
        if (self.driver_path == "none"):
            if ('chrome' in self.driver_name):
                driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
            elif ('ff' in self.driver_name) or ('fox' in self.driver_name):
                driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            elif ('ie' in self.driver_name) or ('explore' in self.driver_name):
                driver = webdriver.Ie(executable_path=IEDriverManager().install())
        else:
            if ('chrome' in self.driver_name):
                driver = webdriver.Chrome(executable_path=self.driver_path)
            elif ('ff' in self.driver_name) or ('fox' in self.driver_name):
                driver = webdriver.Firefox(executable_path=self.driver_path)
            elif ('ie' in self.driver_name) or ('explore' in self.driver_name):
                driver = webdriver.Firefox(executable_path=self.driver_path)
        if self.driver_window_mode is "maximize":
            driver.maximize_window()
        elif self.driver_window_mode is "minimize":
            driver.minimize_window()
        driver.get(self.url)
        driver.implicitly_wait(self.driver_implicit_wait)
        self.base_driver = driver
        return driver

    def get_driver(self):
        return self.base_driver