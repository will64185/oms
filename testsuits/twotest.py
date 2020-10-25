import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.jp_homepage import HomePage
import configparser
import os.path



SKU1 = '02000034'  # 非紧俏品
qhgs = '测试公司（总部）'
qhmd = '东方店'
gys = '上海测试有限公司'

config = configparser.ConfigParser()
file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
config.read(file_path)


class ZdaoM(unittest.TestCase):
    """采购管理"""

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_oms_pchsPlanMain1(self):
        """采购管理：总部-临时采购订单,手动添加配件"""
        homepage = HomePage(self.driver)
        homepage.username('zw1')
        homepage.password('123456')
        homepage.send_submit_btn()
        homepage.wait(10)
        homepage.purchaseManagement()  # 点击采购管理
        time.sleep(1)
        homepage.lsCaigouOrder()  # 点击临时采购订单
        homepage.wait(10)
        homepage.lsadd()  # 点击新增
        homepage.wait(10)
        homepage.lsxzgys()  # 点击选择供应商
        homepage.lsgys(gys)  # 输入供应商
        homepage.lsgysSearch()  # 点击查询
        homepage.wait(10)
        homepage.lsgysxz()  # 双击选择供应商
        homepage.wait(10)
        homepage.lssddSku()  # 点击添加配件
        homepage.lsskuSeaech(SKU1)
        homepage.lsskusearchButton()  # 点击查询
        homepage.wait(10)
        homepage.lsxzsku()  # 双击配件
        homepage.lsskuNum('10')  # 输入采购数量
        homepage.lsskuPrice('100')  # 输入采购价格
        homepage.lssure()  # 点击确定
        homepage.wait(10)
        homepage.lsclose()  # 关闭添加配件的弹框
        homepage.wait(10)
        homepage.lsSave()  # 点击保存
        homepage.wait(10)
        homepage.lsSub()  # 点击提交
        homepage.lsSubSure()   # 点击确定
        homepage.wait(10)
        a = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span').text

        planOrder = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[4]/div/span').text
        try:
            assert "审批中" in a
            print('1.临时采购订单：' + planOrder, '提交成功')
        except Exception as e:
            print('1.临时采购订单：' + planOrder, '提交失败', format(e))
            homepage.get_windows_img()
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[3]/button').click()  # 点击更多查询
        homepage.wait(10)
        self.driver.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[2]/form/div[3]/div/div/input').send_keys(planOrder)  # 输入滚动计划单号
        self.driver.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div[3]/div/button[1]').click()  # 点击确定
        homepage.wait(10)
        a = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text

        try:
            assert "待收货" in a
            print('2.临时采购订单：' + planOrder, '已审批成功')
        except Exception as e:
            print('2.临时采购订单：' + planOrder, '审批失败', format(e))
            homepage.get_windows_img()





