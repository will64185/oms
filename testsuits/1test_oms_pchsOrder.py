# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.jp_homepage import HomePage
import configparser
import os.path
import win32gui
import win32con


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
        """采购管理：总部-滚动计划,手动添加配件"""
        homepage = HomePage(self.driver)
        homepage.username('zw1')
        homepage.password('123456')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.purchaseManagement()  # 点击采购管理
        time.sleep(1)
        homepage.purchasePlan()  # 点击采购计划
        time.sleep(1)
        homepage.ppadd()  # 点击新增
        homepage.xzgysButton()  # 选择供应商
        time.sleep(1)
        homepage.gysSearch(gys)  # 输入供应商
        homepage.searchButton()  # 点击查询按钮
        time.sleep(2)
        homepage.doubleBill()  # 双击供应商
        time.sleep(1)
        homepage.addsku()  # 点击添加配件
        time.sleep(1)
        homepage.skusearch(SKU1)  # 输入内码
        homepage.skuchaxun()  # 点击查询按钮
        time.sleep(5)
        homepage.doublesku()  # 双击配件
        time.sleep(1)
        homepage.caigouNum('10')  # 输入采购数量
        homepage.caigouPrice('100')  # 输入采购价格
        homepage.caigouSure()  # 点击确定
        time.sleep(1)
        homepage.skuclose()  # 关闭配件选择的弹框
        time.sleep(1)
        homepage.orderplan()  # 点击保存
        time.sleep(2)
        homepage.orderplansub()  # 点击提交
        time.sleep(3)
        a = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text

        planOrder = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[6]/div/span').text
        try:
            assert "审批中" in a
            print('1.滚动计划单：' + planOrder, '提交成功')
        except Exception as e:
            print('1.滚动计划单：' + planOrder, '提交失败', format(e))
            homepage.get_windows_img()
        homepage.gdmore()  # 点击更多查询
        time.sleep(1)
        homepage.gdmoreshuru(planOrder)  # 输入滚动计划单号
        homepage.gdmoresur()  # 点击确定
        time.sleep(2)
        a = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text

        try:
            assert "已审批" in a
            print('2.滚动计划单：' + planOrder, '已审批成功')
        except Exception as e:
            print('2.滚动计划单：' + planOrder, '审批失败', format(e))
            homepage.get_windows_img()

    def test_oms_pchsPlanMain2(self):
        """采购管理：总部-滚动计划-导入配件"""
        homepage = HomePage(self.driver)
        homepage.ppadd()  # 点击新增
        homepage.xzgysButton()  # 选择供应商
        time.sleep(1)
        homepage.gysSearch(gys)  # 输入供应商
        homepage.searchButton()  # 点击查询按钮
        time.sleep(2)
        homepage.doubleBill()  # 双击供应商
        time.sleep(1)
        homepage.orderplan()  # 点击保存
        time.sleep(2)
        # homepage.gddaoru()  # 点击导入
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[3]/div/div[3]/div/div[2]/div/div[1]/button').click()
        time.sleep(2)
        # homepage.gddaoruneima()  # 点击内码导入
        upload = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[3]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/button')
        upload.click()
        time.sleep(3)
        dialog = win32gui.FindWindow("#32770", "打开")
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'C:\\Users\will\Desktop\pp\\滚动计划内码导入.xlsx')  # 往输入框输入绝对地址
        time.sleep(2)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
        # print(upload.get_attribute('value'))
        time.sleep(3)
        a = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[3]/div/div[4]/div[3]/div[2]/table/tbody/tr/td[5]/div/span').text
        try:
            assert a == SKU1
            print('1.配件：' + SKU1, '导入成功')
        except Exception as e:
            print('1.配件：' + SKU1, '导入失败', format(e))
            homepage.get_windows_img()

        homepage.orderplansub()  # 点击提交
        time.sleep(3)
        a = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text

        planOrder = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[6]/div/span').text
        try:
            assert "审批中" in a
            print('2.滚动计划单：' + planOrder, '提交成功')
        except Exception as e:
            print('2.滚动计划单：' + planOrder, '提交失败', format(e))
            homepage.get_windows_img()
        homepage.gdmore()  # 点击更多查询
        time.sleep(1)
        homepage.gdmoreshuru(planOrder)  # 输入滚动计划单号
        homepage.gdmoresur()  # 点击确定
        time.sleep(2)
        a = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text

        try:
            assert "已审批" in a
            print('3.滚动计划单：' + planOrder, '已审批成功')
        except Exception as e:
            print('3.滚动计划单：' + planOrder, '审批失败', format(e))
            homepage.get_windows_img()

    def test_oms_pchsPlanMain3(self):
        """采购管理：总部-计划采购订单"""
        homepage = HomePage(self.driver)
        planOrder = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[6]/div/span').text
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/div/div').click()  # 点击库存管理
        self.driver.switch_to_default_content()  # 到最外层
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').send_keys(
            SKU1)  # 输入内码查询
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        skunumq = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[10]/div/span').text
        skucaigouzaituq = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[25]/div/span').text
        homepage.planCaigouPlan()  # 点击计划采购订单
        time.sleep(2)
        homepage.pcadd()  # 点击新增按钮
        time.sleep(1)
        homepage.pcxzgys()  # 打开新增供应商弹框
        homepage.pcxzgymc(gys)  # # 输入供应商名称
        homepage.pcxzgyscx()
        time.sleep(1)
        homepage.doublegys()  # 双击供应商
        time.sleep(1)
        homepage.pcuxgdjh()  # 点击选择滚动计划
        time.sleep(1)
        homepage.jhorder(planOrder)   # 输入计划采购单号
        homepage.jhsearchbutton()  # 点击查询
        time.sleep(1)
        homepage.pcxzgdjh()
        time.sleep(2)
        homepage.pcxz()  # 点击选择
        time.sleep(2)
        homepage.pcsave()  # 点击保存按钮
        time.sleep(2)
        homepage.pcsub()  # 点击提交按钮
        homepage.pcsre()  # 点击确定按钮
        time.sleep(2)
        a = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text
        orderServiceId = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[4]/div/span').text
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        skunumh = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[10]/div/span').text
        skucaigouzaituh = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[25]/div/span').text
        chayi = int(skucaigouzaituh) - int(skucaigouzaituq)
        try:
            assert "待收货" in a and chayi==10
            print('1.计划采购订单：' + orderServiceId, '已提交')
        except Exception as e:
            print('1.计划采购订单：' + orderServiceId, '提交失败', format(e))
            homepage.get_windows_img()

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
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/div/div').click()  # 点击入库管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/ul/li[1]/div').click()  # 点击入库任务
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/div[1]/div[1]/div/span').click()  # 选择查询条件
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/div[1]/div[2]/ul[2]/li[2]').click()  # 选择业务单号
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/div[2]/input').send_keys(orderServiceId)  # 输入业务单号
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/button').click()  # 点击查询按钮
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[2]/div/label/span/input').click()  # 选择入库单
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[2]/button[2]').click()  # 点击批量收货
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/ul/li[2]/div').click()  # 点击收货管理
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[2]/div/label/span/input').click()  # 选择收货单
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[2]/button[1]').click()  # 点击到货入库
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[3]/button[2]').click()  # 点击确定
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[5]/div/a').click()  # 点击收货单号
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[2]/div[1]/button[2]').click()  # 点击一键收货
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[13]/div[2]/div/div/div/div/div[3]/button[2]').click()  # 点击确定
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[2]/div/div[1]/button[2]').click()  # 点击收货完成
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[13]/div[2]/div/div/div/div/div[3]/button[2]').click()  # 点击确定
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[2]/div/div[1]/button[3]').click()  # 点击生成上架单
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/ul/li[3]/div').click()  # 点击上架管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/div/a').click()  # 点击上架单号
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[2]/div/div[1]/button[1]').click()  # 点击上架完成
        time.sleep(1)
        # self.driver.find_element_by_xpath('/html/body/div[11]/div[2]/div/div/div/div/div[3]/button[2]')  # 点击确定
        sure_results = self.driver.find_elements_by_xpath('//*[@class="ivu-btn ivu-btn-primary ivu-btn-large"]')
        sure_results[4].click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/ul/li[1]/div').click()  # 点击入库任务
        time.sleep(2)
        a = self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[8]/div/span').text
        try:
            assert "已完成" in a
            print('2.计划采购订单：' + orderServiceId, 'wms已成功出库')
        except Exception as e:
            print('2.计划采购订单：' + orderServiceId, 'wms出库失败', format(e))
            homepage.get_windows_img()
        window = self.driver.window_handles
        self.driver.switch_to.window(window[-0])
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(3)
        skunumh1 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[10]/div/span').text
        skucaigouzaituh1 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[25]/div/span').text
        chayi1 = int(skunumh1)-int(skunumq)

        homepage.planCaigouPlan()  # 点击计划采购订单
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[3]/button').click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div[44]/div[2]/div/div/div[2]/form/div[3]/div/div/input').send_keys(orderServiceId)
        self.driver.find_element_by_xpath('/html/body/div[44]/div[2]/div/div/div[3]/div/button[1]').click()
        time.sleep(2)
        a = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text
        try:
            assert "全部入库" in a and chayi1 ==10 and skucaigouzaituh1 == skucaigouzaituq
            print('3.WMS回传oms成功，入库前配件' + SKU1, '库存为' + skunumq, '，入库后配件' + SKU1, '库存为' + skunumh1, '入库数量为：10')

        except Exception as e:
            print('3.WMS回传oms失败', format(e))
            print('3.WMS回传oms成功，入库前配件' + SKU1, '库存为' + skunumq, '，入库后配件' + SKU1, '库存为' + skunumh1, '入库数量为：10')
            homepage.get_windows_img()
