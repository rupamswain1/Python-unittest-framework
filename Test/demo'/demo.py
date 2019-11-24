from Main.pages.loginPage import LoginPage
from Engine.logger.logger import Logger
import unittest
import time
class demo(unittest.TestCase):
    def test_one(self):
        log=Logger()
        login_page=LoginPage()
        login_page.open_webpage()
        print(login_page.get_driver().title)
        log.log_debug("debud")
        login_page.get_close_pop_up()
        time.sleep(10)
        print(login_page.get_driver().title)
    def test_two(self):
        login_page=LoginPage()
        login_page.open_webpage()
        print(login_page.get_driver().title)

if __name__=='__main__':
    unittest.main()