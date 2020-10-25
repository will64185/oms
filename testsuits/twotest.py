import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.jp_homepage import HomePage
import configparser
import os.path

SKU1 = '02000034'  # 非紧俏品
qhgs = '测试公司（总部）'
qhmd = '东方店'
dbsqnum = 5  # 调拨申请数量
chuku1 = 2  # 第一次出库数量

config = configparser.ConfigParser()
file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
config.read(file_path)


class MdaoZ(unittest.TestCase):
    '''门店调拨入库及退货流程'''

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_oms_allot1(self):
        '''门店调拨入库'''

        homepage = HomePage(self.driver)
        homepage.username('dfd')
        homepage.password('123456')
        homepage.send_submit_btn()
        homepage.dbMananger()  # 点击调拨管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[4]/ul/li[2]/div/div').click()  # 点击调拨退货
        time.sleep(1)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[4]/ul/li[2]/ul/li[1]/div').click()  # 点击调入退回申请
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[3]/button').click()  # 点击新增
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[3]/div/div[2]/form/div[1]/div/div/div[2]/button').click()  # 选择调出方
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@class="el-input__inner"]').send_keys(
            qhgs)  # 输入调出方
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@class="mr10 ivu-btn ivu-btn-primary"]').click()  # 点击查询
        time.sleep(2)
        homepage.doubledcf()






