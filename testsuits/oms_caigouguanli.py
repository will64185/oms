# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.jp_homepage import HomePage
from framework.logger import Logger
logger = Logger(logger="OutTask").getlog()

aaa = 20

class caigou(unittest.TestCase):
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



    def test_caigou_1(self):
        '''滚动计划单'''
        homepage = HomePage(self.driver)
        homepage.purchaseManagement()    # 点击采购管理
        time.sleep(1)
        homepage.purchasePlan()    # 进入滚动计划界面
        time.sleep(1)
        homepage.ppadd()   # 点击新增按钮
        time.sleep(1)
        homepage.xzgysButton()  # 选择供应商
        time.sleep(1)
        self.driver.switch_to_default_content()  #  到最外层
        homepage.gysSearch("测试供应商全称")
        homepage.searchButton()
        time.sleep(1)
        homepage.doubleBill()   # 双击供应商
        time.sleep(1)
        self.driver.switch_to_default_content()  #  到最外层
        homepage.addsku()  # 新增配件按钮
        self.driver.switch_to_default_content()  #  到最外层
        homepage.sleep(4)
        homepage.skusearch("04000179")  # 输入配件
        homepage.skuxuanze()  # 点击搜索按钮
        time.sleep(4)
        homepage.doublesku()  # 双击配件
        homepage.sleep(1)
        homepage.caigouNum("100")  # 输入数量
        homepage.caigouPrice("100")  # 输入单价
        homepage.caigouSure()  # 点击确定
        time.sleep(2)
        homepage.skuclose()  # 关闭配件选择弹框
        time.sleep(2)
        self.driver.switch_to_default_content()  # 到最外层
        homepage.orderplan()  # 保存滚动计划单
        time.sleep(2)
        homepage.caigouplan()  # 选择保存的滚动计划单
        time.sleep(2)
        homepage.orderplansub()  # 提交滚动计划
        self.driver.switch_to_default_content()  # 到最外层
        time.sleep(3)
        a = self.driver.find_element_by_xpath(
    "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span").text
        print(a)

        try:
            assert "已审批" in a
            print('通过')
        except Exception as e:
            print('失败', format(e))
            homepage.get_windows_img()

    def test_caigou_2(self):
        '''计划采购订单'''
        homepage = HomePage(self.driver)
        time.sleep(1)
        homepage.planCaigouPlan()  # 进入滚动计划界面
        time.sleep(1)
        homepage.pcadd()  # 点击新增按钮
        time.sleep(1)
        homepage.pcxzgys()  # 选择供应商
        time.sleep(5)
        homepage.pcxzgymc("测试供应商全称")
        homepage.pcxzgyscx()
        time.sleep(1)
        homepage.doublegys()  # 双击供应商
        time.sleep(2)
        homepage.pcuxgdjh()  # 选择滚动计划按钮
        time.sleep(4)
        homepage.pcxzgdjh()  # 选择具体的滚动计划
        time.sleep(2)
        homepage.pcxz()  # 点击选择按钮
        time.sleep(2)
        homepage.pcsave()  # 点击保存按钮
        time.sleep(2)
        homepage.pcsub()# 点击提交按钮
        a = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/section[2]/div"
            "/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span").text
        print(a)
        try:
            assert "已审批" in a
            print('通过')
            homepage.get_windows_img()
        except Exception as e:
            print('失败', format(e))
            homepage.get_windows_img()

    def test_caigou_3(self):
        '''临时采购订单'''
        homepage = HomePage(self.driver)
        time.sleep(2)
        homepage.lsCaigouOrder()  # 进入临时采购订单
        time.sleep(2)
        homepage.lsadd()  # 点击新增按钮
        time.sleep(2)
        homepage.lsxzgys()  # 点击选择供应商
        time.sleep(3)
        homepage.lsgys("测试供应商全称")
        time.sleep(2)
        homepage.lsgysSearch()  # 点击搜索按钮
        time.sleep(2)
        homepage.lsgysxz()  # 双击供应商
        time.sleep(2)
        homepage.lssddSku()  # 点击新增配件按钮
        time.sleep(2)
        homepage.lsskuSeaech("04000179")  # 输入配件内码
        time.sleep(2)
        homepage.lsskusearchButton()  # 点击查询按钮
        time.sleep(3)
        homepage.lsxzsku()  # 双击选择配件
        time.sleep(2)
        homepage.lsskuNum("5")  # 输入数量
        time.sleep(1)
        homepage.lsskuPrice("100")  # 输入单价
        time.sleep(1)
        homepage.lssure()  # 点击确定按钮
        time.sleep(2)
        homepage.lsclose()  # 点击取消按钮
        time.sleep(1)
        homepage.lsSave()  # 点击保存按钮
        time.sleep(2)
        homepage.lsSub()  # 点击提交按钮
        time.sleep(1)
        homepage.lsSubSure()  # 点击确定
        time.sleep(3)
        a = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div'
                                              '/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span').text
        print(a)
        try:
            assert "待收货" in a
            print('通过')
        except Exception as e:
            print('失败', format(e))
            homepage.get_windows_img()


    def test_caigou_4(self):
        '''外采订单'''
        homepage = HomePage(self.driver)
        homepage.wcCaigouOrder()  # 点击外采订单
        time.sleep(2)
        homepage.wcadd()  # 点击新增按钮
        time.sleep(2)
        homepage.wcxzgys()  # 点击选择供应商
        time.sleep(3)
        homepage.wcgys("测试供应商全称")
        time.sleep(2)
        homepage.wcgysSearch()  # 点击搜索按钮
        time.sleep(2)
        homepage.wcgysxz()  # 双击供应商
        time.sleep(2)
        homepage.wcsddSku()  # 点击新增配件按钮
        time.sleep(4)
        homepage.wcskuSeaech("04000179")  # 输入配件内码
        time.sleep(1)
        homepage.wcskusearchButton()  # 点击查询按钮
        time.sleep(4)
        homepage.wcxzsku()  # 双击选择配件
        time.sleep(2)
        homepage.wcskuNum("5")  # 输入数量
        time.sleep(1)
        homepage.wcskuPrice("100")  # 输入单价
        time.sleep(1)
        homepage.wcsure()  # 点击确定按钮
        time.sleep(2)
        homepage.wcclose()  # 点击取消按钮
        time.sleep(3)
        homepage.wcSave()  # 点击保存按钮
        time.sleep(2)
        homepage.skuM()  # 点击库存管理
        time.sleep(2)
        homepage.skuMsearch()  # 点击库存查询
        time.sleep(2)
        homepage.skushuru("04000179")  # 输入内码
        homepage.skuchaxuan()  # 点击查询
        time.sleep(4)
        totalNum = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]'
                                                '/div[2]/div[1]/div[2]/table/tbody/tr/td[9]/div/div/div/span').text  # 获取入库前库存
        print(totalNum)
        homepage.wcCaigouOrder()
        homepage.wcSub()  # 点击提交按钮
        time.sleep(1)
        homepage.wcSubSure()  # 点击确定
        time.sleep(5)
        a = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div'
            '/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span').text
        print(a)
        homepage.skuMsearch()  # 点击库存查询
        time.sleep(2)
        homepage.skuchaxuan()  # 点击查询
        time.sleep(4)
        totalNum1 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[1]/div[2]/table/tbody/tr/td[9]/div/div/div/span').text  # 获取入库后库存
        print(totalNum1)

        try:
            assert "全部入库" in a and int(totalNum1) == int(totalNum) + 5
            print('通过')
        except Exception as e:
            print('失败', format(e))
            homepage.get_windows_img()






if __name__ == '__main__':
    unittest.main()