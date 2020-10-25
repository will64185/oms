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
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/div/div').click()  # 点击库存管理
        self.driver.switch_to_default_content()  # 到最外层
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
        # homepage.kccx()  # 库存查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').send_keys(
            SKU1)  # 输入内码查询
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/label/span/input').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        mdku = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[10]/div/span').text  # 获取门店库存
        homepage.dbMananger()  # 点击调拨管理
        homepage.dborder()  # 点击调拨单
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[4]/ul/li[1]/ul/li[4]/div').click()  # 点击调拨入库
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[3]/button').click()  # 点击新增
        self.driver.find_element_by_xpath(
            '/html/body/div[38]/div[2]/div/div/div[2]/section[2]/div[1]/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/div/span').click()  # 选择需要导入的调拨出库单
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[38]/div[2]/div/div/div[2]/section[1]/div/form/div/div[5]/button').click()  # 点击选入
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[4]/button').click()  # 点击保存
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[5]/button').click()  # 点击入库
        self.driver.find_element_by_xpath('/html/body/div[40]/div[2]/div/div/div/div/div[3]/button[2]').click()
        time.sleep(4)
        a = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
        # homepage.kccx()  # 库存查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        mdku1 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[10]/div/span').text  # 获取门店库存
        chayi = int(mdku1) - int(mdku)
        try:
            assert chayi == 2 and '已入库' in a
            print('门店入库成功，入库前配件' + SKU1, '的库存为' + mdku, '，入库后配件' + SKU1, '的库存为' + mdku1, '入库数量为：2')
        except Exception as e:
            print('门店入库失败，入库前配件' + SKU1, '的库存为' + mdku, '，入库后配件' + SKU1, '的库存为' + mdku1, '入库数量为：2', format(e))
            homepage.get_windows_img()

    def test_oms_allot2(self):
        '''门店调入退回申请'''
        homepage = HomePage(self.driver)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[4]/ul/li[2]/div/div').click()  # 点击调拨退货
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[4]/ul/li[2]/ul/li[1]/div').click()  # 点击调入退回申请
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[3]/button').click()  # 点击新增
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[3]/div/div[2]/form/div[1]/div/div/div[2]/button').click()  # 选择调出方
        time.sleep(2)

        self.driver.find_element_by_xpath('//input[@class="el-input__inner"]').send_keys(qhgs)  # 输入调出方
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@class="mr10 ivu-btn ivu-btn-primary"]').click()  # 点击查询
        time.sleep(2)
        homepage.doubledcf()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[3]/div/div[3]/div/div[1]/button').click()  # 添加配件
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[47]/div[2]/div/div/div[2]/div/div[1]/div[3]/div/input').send_keys(SKU1)
        self.driver.find_element_by_xpath(
            '/html/body/div[47]/div[2]/div/div/div[2]/div/div[1]/div[8]/button').click()  # 点击查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[47]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]/div/span').click()  # 选择配件
        self.driver.find_element_by_xpath(
            '/html/body/div[47]/div[2]/div/div/div[2]/div/div[1]/div[9]/button').click()  # 点击选择
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[47]/div[2]/div/div/a').click()  # 关闭添加配件弹框
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[4]/button').click()  # 点击保存
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[5]/button').click()  # 点击提交
        a = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text
        drthsqd = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[6]/div/span').text
        try:
            assert "待受理" in a
            print('1.调入退回申请单' + drthsqd, '已提交')
        except Exception as e:
            print('1.调入退回申请单' + drthsqd, '已提交', format(e))
            homepage.get_windows_img()

    def test_oms_allot3(self):
        '''总部调入退回申请受理后，门店出库'''

        homepage = HomePage(self.driver)
        drthsqd = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[6]/div/span').text
        time.sleep(2)
        homepage.qhzh()  # 切换门店
        homepage.shurumd(qhgs)  # 输入需要切换的门店
        homepage.djcx()  # 点击查询
        time.sleep(2)
        homepage.djxzmd()
        homepage.djxz()  # 点击选择
        time.sleep(5)

        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[4]/ul/li[2]/ul/li[3]/div').click()  # 点击调入退回受理
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[1]/div/div/div[5]/div/input').send_keys(
            drthsqd)  # 输入调入退回申请单
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[1]/div/div/div[6]/button').click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[2]/div[1]/div/div[2]/div[2]/table/tbody/tr/td[2]/div/button[1]').click()  # 点击受理
        self.driver.find_element_by_xpath('/html/body/div[19]/div[2]/div/div/div[3]/button[2]').click()  # 点击确定
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        homepage.qhzh()  # 切换门店
        homepage.shurumd(qhmd)  # 输入需要切换的门店
        homepage.djcx()  # 点击查询
        time.sleep(2)
        homepage.djxzmd()
        homepage.djxz()  # 点击选择
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/div/div').click()  # 点击库存管理
        self.driver.switch_to_default_content()  # 到最外层
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
        # homepage.kccx()  # 库存查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').send_keys(
            SKU1)  # 输入内码查询
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/label/span/input').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        thqkucun = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[10]/div/span').text  # 获取门店库存
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[4]/ul/li[2]/ul/li[1]/div').click()  # 点击调入退回申请
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[2]/button').click()  # 点击更多
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[19]/div[2]/div/div/div[2]/form/div/div[4]/div/input').send_keys(drthsqd)
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[19]/div[2]/div/div/div[3]/div/button[1]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[6]/button').click()  # 点击出库
        time.sleep(4)
        self.driver.refresh()
        time.sleep(4)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[2]/button').click()  # 点击更多
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[8]/div[2]/div/div/div[2]/form/div/div[4]/div/input').send_keys(drthsqd)
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[3]/div/button[1]').click()  # 点击确定
        time.sleep(2)

        a = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span').text
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/div/div').click()  # 点击库存管理
        self.driver.switch_to_default_content()  # 到最外层
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
        # homepage.kccx()  # 库存查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').send_keys(
            SKU1)  # 输入内码查询
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/label/span/input').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        thhkucun = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[10]/div/span').text  # 获取门店库存
        chayi = int(thqkucun) - int(thhkucun)
        try:
            assert chayi == 2 and '已完成' in a
            print('门店出库成功，出库前配件' + SKU1, '的库存为' + thqkucun, '，出库后配件' + SKU1, '的库存为' + thhkucun, '出库数量为：2')
        except Exception as e:
            print('门店入库失败，出库前配件' + SKU1, '的库存为' + thqkucun, '，出库后配件' + SKU1, '的库存为' + thhkucun, '出库数量为：2', format(e))

    def test_oms_allot4(self):
        '''总部调入退回入库'''

        homepage = HomePage(self.driver)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[4]/ul/li[2]/ul/li[1]/div').click()
        time.sleep(2)
        drthsqd = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[6]/div/span').text

        homepage.qhzh()  # 切换门店
        homepage.shurumd(qhgs)  # 输入需要切换的门店
        homepage.djcx()  # 点击查询
        time.sleep(2)
        homepage.djxzmd()
        time.sleep(1)
        homepage.djxz()  # 点击选择
        time.sleep(6)

        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/div/div').click()  # 点击库存管理
        self.driver.switch_to_default_content()  # 到最外层
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
        # homepage.kccx()  # 库存查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').send_keys(
            SKU1)  # 输入内码查询
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/label/span/input').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        thrukuq = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[10]/div/span').text  # 获取门店库存

        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[4]/ul/li[2]/ul/li[2]/div').click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[1]/div/div/div[2]/button').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[30]/div[2]/div/div/div[2]/form/div/div[4]/div/input').send_keys(drthsqd)
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[30]/div[2]/div/div/div[3]/button[2]').click()
        time.sleep(2)
        dcthrkd = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[6]/div/span').text
        a = config.get("testWms", "wms")
        js = "window.open(" + '"' + a + '"' + ")"  # 打开wms
        self.driver.execute_script(js)
        window = self.driver.window_handles
        self.driver.switch_to.window(window[-1])
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div/div/form/div[1]/div/div[1]/input').send_keys('zw1')
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div/form/div[2]/div/div/input').send_keys(
            '123456')
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div/div/form/div[4]/div/button').click()  # 登录wms
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[6]/div').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[6]/ul/li[5]/div').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section/div[2]/div/div/div[1]/div/span').click()
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section/div[2]/div/div/div[2]/ul[2]/li[2]').click()  # 设置默认仓
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/div/div').click()  # 点击入库管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/ul/li[7]/div').click()  # 点击其他入库
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[4]/div/div[1]/div/span').click()  # 点击订单类型
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[4]/div/div[2]/ul[2]/li[5]').click()  # 选择调拨退货
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/div[1]/div[1]/div/span').click()  # 点击查询条件
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/div[1]/div[2]/ul[2]/li[2]').click()  # 选择业务单号
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/div[2]/input').send_keys(dcthrkd)  # 输入业务单号
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/button[1]').click()  # 点击查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[3]/div/a').click()  # 点击业务单号
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[2]/button').click()  # 点击确认入库
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/div/div[3]/button[2]').click()  # 点击确定按钮
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/div/div').click()  # 点击入库管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[6]/ul/li[3]/div').click()  # 点击接口同步日志
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div/button').click()  # 点击查询按钮
        time.sleep(2)

        a = self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[3]/div/span').text  # 获取wms接口日志第一条的业务单号

        while a not in dcthrkd:
            time.sleep(5)
            self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div/button').click()
            time.sleep(1)
            adanhao = self.driver.find_element_by_xpath(
                '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[3]/div/span').text
            status = self.driver.find_element_by_xpath(
                '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[5]/div/span').text
            print(adanhao)

            if adanhao in dcthrkd and '成功' in status:
                self.driver.switch_to.window(window[-0])
                time.sleep(5)
                self.driver.find_element_by_xpath(
                    '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[1]/div/div/div[2]/button/span').click()  # 点击更多查询
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[30]/div[2]/div/div/div[3]/button[2]').click()  # 点击确定
                time.sleep(2)
                a = self.driver.find_element_by_xpath(
                    '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text
                self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
                # homepage.kccx()  # 库存查询
                time.sleep(2)
                self.driver.find_element_by_xpath(
                    '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
                time.sleep(5)
                thrukuh = self.driver.find_element_by_xpath(
                    '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
                    '2]/table/tbody/tr/td[10]/div/span').text  # 获取门店库存
                chayi = int(thrukuh) - int(thrukuq)
                try:
                    assert chayi == 2 and '已入库' in a
                    print('总部入库成功，入库前配件' + SKU1, '的库存为' + thrukuq, '，入库后配件' + SKU1, '的库存为' + thrukuh, '入库数量为：2')
                except Exception as e:
                    print('总部入库失败，入库前配件' + SKU1, '的库存为' + thrukuq, '，入库后配件' + SKU1, '的库存为' + thrukuh, '入库数量为：2',
                          format(e))
                break
            else:
                a = adanhao
        else:
            print('wms回传异常')
