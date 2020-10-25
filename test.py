# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.jp_homepage import HomePage
from framework.logger import Logger
logger = Logger(logger="OutTask").getlog()

aaa = 20

class loginone(unittest.TestCase):
    ''''''
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)
        homepage = HomePage(cls.driver)
        homepage.username('h1')  # 调用页面对象中的方法
        homepage.password('123456')
        homepage.send_submit_btn()
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()


    def test_caigouOrderPlan(self):
        '''采购计划单'''

        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div/div[4]/ul/li[2]/ul/li[2]").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[4]/button").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[3]/div/div[2]/form/div[1]/div/div/div[2]/button").click()









if __name__ == '__main__':
    unittest.main()