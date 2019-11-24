from selenium.webdriver.common.keys import Keys
from Engine.utilities.config_reader import ReadConfig
import time
class Elements_Wait:

    def __init__(self):
        self.driver_implicit_wait=int(ReadConfig.get_property(("driver_implicit_wait")))*1000
        self.driver=None
    def wait_for_elements(self,driver,locator_type,locator):
        elements=None
        while(self.driver_implicit_wait>0 and elements is None):
            #implement for all locator
            if(locator_type=="xpath"):
               elements=driver.find_elements_by_xpath(locator)
            elif(locator=="id"):
                elements=driver.find_elements_by_id(locator)
            elif(locator=="name"):
                elements=driver.find_elements_by_name(locator)
            elif(locator=="class_name"):
                elements=driver.find_elements_by_class_name(locator)
            elif(locator=="tag_name"):
                elements=driver.find_elements_by_tag_name(locator)
            elif(locator=="link_text"):
                elements=driver.find_elements_by_link_text(locator)
            elif(locator=="partial_link_text"):
                elements=driver.find_elements_by_partial_link_text(locator)
            else:
                raise NameError("locator "+locator+" not found")
            self.driver_implicit_wait=self.driver_implicit_wait-1
            time.sleep(1/1000)

        return elements
