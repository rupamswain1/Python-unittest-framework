from Engine.excel_utils.excel_reader import read_xlsx
from selenium.webdriver.common.keys import Keys
from Engine.wait.elements_wait import Elements_Wait
class webelement:

    driver=None

    def __init__(self):
        self.driver=None

    def single_multiple_element(self, webelements):
        if len(webelements)>1:
            return webelements
        elif len(webelements)==1:
            return webelements[0]
    def get_locator(self,driver,locator_string):
        locator_details = locator_string.split('.')
        sheetName = locator_details[0]
        locator_name = locator_details[1].lower()
        reader_obj=read_xlsx()
        excel_data=reader_obj.read_locator_excel(sheetName)
        self.driver = driver
        obj = webelement()
        for items in excel_data:

            if items['element_name'].lower() == locator_name.lower():

                if items['xpath'] is not None:
                    #implemenr for all locator
                    ele = Elements_Wait().wait_for_elements(self.driver,'xpath',items['xpath'])
                    return obj.single_multiple_element(ele)
                elif items['id'] is not None:
                    ele = Elements_Wait().wait_for_elements(self.driver, 'id', items['id'])
                    return obj.single_multiple_element(ele)
                elif items['name'] is not None:
                    ele =Elements_Wait().wait_for_elements(self.driver, 'name', items['name'])
                    return obj.single_multiple_element(ele)
                elif items['class_name'] is not None:
                    ele=Elements_Wait().wait_for_elements(self.driver, 'class_name', items['class_name'])
                    return obj.single_multiple_element(ele)
                elif items['tag_name'] is not None:
                    ele = Elements_Wait().wait_for_elements(self.driver, 'tag_name', items['tag_name'])
                    return obj.single_multiple_element(ele)
                elif items['link_text'] is not None:
                    ele = Elements_Wait().wait_for_elements(self.driver, 'link_text', items['link_text'])
                    return obj.single_multiple_element(ele)
                elif items['partial_link_text'] is not None:
                    ele = Elements_Wait().wait_for_elements(self.driver, 'partial_link_text', items['partial_link_text'])
                    return obj.single_multiple_element(ele)
                elif items['css_selector'] is not None:
                    ele = Elements_Wait().wait_for_elements(self.driver, 'css_selector',
                                                            items['css_selector'])
                    return obj.single_multiple_element(ele)







