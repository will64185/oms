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
        """采购管理：总部-临时采购订单,手动添加配件"""
        homepage = HomePage(self.driver)
        homepage.username('zw1')
        homepage.password('123456')
        homepage.send_submit_btn()
        time.sleep(2)
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
        skunumq = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[10]/div/span').text
        skucaigouzaituq = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[25]/div/span').text
        homepage.purchaseManagement()  # 点击采购管理
        time.sleep(1)
        homepage.lsCaigouOrder()  # 点击临时采购订单
        time.sleep(2)
        homepage.lsadd()  # 点击新增
        time.sleep(1)
        homepage.lsxzgys()  # 点击选择供应商
        time.sleep(1)
        homepage.lsgys(gys)  # 输入供应商
        time.sleep(1)
        homepage.lsgysSearch()  # 点击查询
        time.sleep(2)
        homepage.lsgysxz()  # 双击选择供应商
        time.sleep(1)
        homepage.lssddSku()  # 点击添加配件
        homepage.lsskuSeaech(SKU1)
        homepage.lsskusearchButton()  # 点击查询
        time.sleep(6)
        homepage.lsxzsku()  # 双击配件
        homepage.lsskuNum('10')  # 输入采购数量
        homepage.lsskuPrice('100')  # 输入采购价格
        homepage.lssure()  # 点击确定
        time.sleep(1)
        homepage.lsclose()  # 关闭添加配件的弹框
        time.sleep(1)
        homepage.lsSave()  # 点击保存
        time.sleep(1)
        homepage.lsSub()  # 点击提交
        homepage.lsSubSure()   # 点击确定
        time.sleep(2)
        a = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span').text
        planOrder = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[4]/div/span').text
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        skunumh = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[10]/div/span').text
        skucaigouzaituh1 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[25]/div/span').text
        chayi = int(skucaigouzaituh1) - int(skucaigouzaituq)
        print('skucaigouzaituh1:',skucaigouzaituh1,'skucaigouzaituq:',skucaigouzaituq)
        try:
            assert "审批中" in a and chayi == 10
            print('1.临时采购订单：' + planOrder, '提交成功')
        except Exception as e:
            print('1.临时采购订单：' + planOrder, '提交失败', format(e))
            homepage.get_windows_img()
        homepage.lsCaigouOrder()  # 点击临时采购订单
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[3]/button').click()  # 点击更多查询
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[22]/div[2]/div/div/div[2]/form/div[3]/div/div/input').send_keys(planOrder)  # 输入滚动计划单号
        self.driver.find_element_by_xpath('/html/body/div[22]/div[2]/div/div/div[3]/div/button[1]').click()  # 点击确定
        time.sleep(2)
        a = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text

        try:
            assert "待收货" in a
            print('2.临时采购订单：' + planOrder, '已审批成功')
        except Exception as e:
            print('2.临时采购订单：' + planOrder, '审批失败', format(e))
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
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/div[1]/div[1]/div/span').click()  # 选择查询条件
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/div[1]/div[2]/ul[2]/li[2]').click()  # 选择业务单号
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/div[2]/input').send_keys(
            planOrder)  # 输入业务单号
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/button').click()  # 点击查询按钮
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[2]/div/label/span/input').click()  # 选择入库单
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[2]/button[2]').click()  # 点击批量收货
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/ul/li[2]/div').click()  # 点击收货管理
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[2]/div/label/span/input').click()  # 选择收货单
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[2]/button[1]').click()  # 点击到货入库
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[3]/button[2]').click()  # 点击确定
        time.sleep(2)
        self.driver.find_element_by_xpath(
             '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[5]/div/a').click()  # 点击收货单号
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[2]/div[2]/div/div[2]/table/tbody/tr/td[3]/div/span').click()  # 点击添加明细
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[11]/div[2]/div/div/div[2]/div[3]/div/div[2]/input').clear()
        self.driver.find_element_by_xpath('/html/body/div[11]/div[2]/div/div/div[2]/div[3]/div/div[2]/input').send_keys('5')  # 输入收货数量
        self.driver.find_element_by_xpath('/html/body/div[11]/div[2]/div/div/div[3]/div/button').click()  # 点击确定

        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[2]/div/div[1]/button[2]').click()  # 点击收货完成
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[13]/div[2]/div/div/div/div/div[3]/button[2]').click()  # 点击确定
        time.sleep(2)

        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[2]/div/div[1]/button[3]').click()  # 点击生成上架单
        time.sleep(2)
        shdh = self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[5]/div/a').text
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/ul/li[3]/div').click()  # 点击上架管理
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/div/a').click()  # 点击上架单号
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[2]/div/div[1]/button[1]').click()  # 点击上架完成
        time.sleep(1)
        # self.driver.find_element_by_xpath('/html/body/div[11]/div[2]/div/div/div/div/div[3]/button[2]')  # 点击确定
        sure_results = self.driver.find_elements_by_xpath('//*[@class="ivu-btn ivu-btn-primary ivu-btn-large"]')
        sure_results[4].click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/ul/li[1]/div').click()  # 点击入库任务
        time.sleep(2)
        a = self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[8]/div/span').text
        try:
            assert "已完成" in a
            print('3.临时采购订单：' + planOrder, 'wms已部分入库成功')
        except Exception as e:
            print('3.临时采购订单：' + planOrder, 'wms入库失败', format(e))

        window = self.driver.window_handles
        self.driver.switch_to.window(window[-0])
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[3]/button').click()  # 点击更多
        self.driver.find_element_by_xpath('/html/body/div[22]/div[2]/div/div/div[3]/div/button[1]').click()  # 点击确定
        time.sleep(2)
        a = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        skunumh = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[10]/div/span').text
        skucaigouzaituh = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[25]/div/span').text
        chayi = int(skunumh) - int(skunumq)
        zaitu = int(skucaigouzaituh1) - int(skucaigouzaituh)
        print(skucaigouzaituh1, skucaigouzaituh)
        print(chayi,zaitu)
        try:
            assert "部分入库" in a and chayi == 5  and zaitu == 5
            print('4.WMS回传oms成功，入库前配件' + SKU1, '库存为' + skunumq, '，入库后配件' + SKU1, '库存为' + skunumh, '入库数量为：5')

        except Exception as e:
            print('4.WMS回传oms失败', format(e))
            print('4.WMS回传oms失败，入库前配件' + SKU1, '库存为' + skunumq, '，入库后配件' + SKU1, '库存为' + skunumh, '入库数量为：5')
            homepage.get_windows_img()

        window = self.driver.window_handles
        self.driver.switch_to.window(window[-1])
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/ul/li[6]/div').click()  # 点击收货差异
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div/div/div[4]/div[2]/input').send_keys(shdh)  # 输入收货单号
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div/div/div[4]/button').click()  # 点击查询
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[2]/div/span/span[2]').click()  # 点击再次入库
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div/div/div/div[3]/button[2]').click()  # 点击确定
        time.sleep(1)
        self.driver.refresh()
        time.sleep(2)



        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/ul/li[1]/div').click()  # 点击入库任务
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/div[1]/div[1]/div/span').click()  # 选择查询条件
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/div[1]/div[2]/ul[2]/li[2]').click()  # 选择业务单号
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/div[2]/input').send_keys(
            planOrder)  # 输入业务单号
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/button').click()  # 点击查询按钮
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[2]/td[2]/div/label/span/input').click()  # 选择入库单
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[2]/button[2]').click()  # 点击批量收货
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/ul/li[2]/div').click()  # 点击收货管理
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[2]/div/label/span/input').click()  # 选择收货单
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[2]/button[1]').click()  # 点击到货入库
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[3]/button[2]').click()  # 点击确定
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[5]/div/a').click()  # 点击收货单号
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div[2]/div/div[2]/table/tbody/tr/td[3]/div/span').click()  # 点击添加明细
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[11]/div[2]/div/div/div[2]/div[3]/div/div[2]/input').clear()
        self.driver.find_element_by_xpath('/html/body/div[11]/div[2]/div/div/div[2]/div[3]/div/div[2]/input').send_keys(
            '4')  # 输入收货数量
        self.driver.find_element_by_xpath('/html/body/div[11]/div[2]/div/div/div[3]/div/button').click()  # 点击确定

        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[2]/div/div[1]/button[2]').click()  # 点击收货完成
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[13]/div[2]/div/div/div/div/div[3]/button[2]').click()  # 点击确定
        time.sleep(2)

        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[2]/div/div[1]/button[3]').click()  # 点击生成上架单
        time.sleep(2)
        shdh = self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[5]/div/a').text
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/ul/li[3]/div').click()  # 点击上架管理
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/div/a').click()  # 点击上架单号
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[2]/div/div[1]/button[1]').click()  # 点击上架完成
        time.sleep(1)
        # self.driver.find_element_by_xpath('/html/body/div[11]/div[2]/div/div/div/div/div[3]/button[2]')  # 点击确定
        sure_results = self.driver.find_elements_by_xpath('//*[@class="ivu-btn ivu-btn-primary ivu-btn-large"]')
        sure_results[4].click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/ul/li[1]/div').click()  # 点击入库任务
        time.sleep(2)
        a = self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[2]/td[8]/div/span').text
        try:
            assert "已完成" in a
            print('5.临时采购订单：' + planOrder, 'wms再次入库成功')
        except Exception as e:
            print('5.临时采购订单：' + planOrder, 'wms再次入库失败', format(e))

        window = self.driver.window_handles
        self.driver.switch_to.window(window[-0])
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[2]/ul/li[4]/div').click()  # 点击临时采购订单
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[3]/button').click()  # 点击更多
        self.driver.find_element_by_xpath('/html/body/div[22]/div[2]/div/div/div[3]/div/button[1]').click()  # 点击确定
        time.sleep(2)
        a = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        skunumh = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[10]/div/span').text
        skucaigouzaituh = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[25]/div/span').text
        chayi = int(skunumh) - int(skunumq)
        zaitu = int(skucaigouzaituh1) - int(skucaigouzaituh)
        print(skucaigouzaituh1, skucaigouzaituh)
        print(chayi, zaitu)
        try:
            assert "部分入库" in a and chayi == 9 and zaitu == 9
            print('6.WMS回传oms成功，入库前配件' + SKU1, '库存为' + skunumq, '，入库后配件' + SKU1, '库存为' + skunumh, '入库数量为：5')

        except Exception as e:
            print('6.WMS回传oms失败', format(e))
            print('6.WMS回传oms失败，入库前配件' + SKU1, '库存为' + skunumq, '，入库后配件' + SKU1, '库存为' + skunumh, '入库数量为：5')
            homepage.get_windows_img()






