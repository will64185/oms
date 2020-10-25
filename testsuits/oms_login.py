# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.jp_homepage import HomePage



class JpLogin(unittest.TestCase):
    '''登录'''
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()


    def test_oms_login1(self):
        '''正确用户名密码登录'''
        homepage = HomePage(self.driver)
        homepage.username('h1')
        homepage.password('123456')
        homepage.send_submit_btn()
        time.sleep(2)
        b = homepage.get_page_title()
        try:
            assert "极配OMS系统" in b
            print('通过')
            homepage.get_windows_img()
        except Exception as e:
            print('失败', format(e))
            homepage.get_windows_img()




if __name__ == '__main__':
    unittest.main()