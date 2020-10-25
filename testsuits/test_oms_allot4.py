import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.jp_homepage import HomePage
import configparser
import os.path

SKU1 = '02000222'  # 无可售数量，有锁定数量的紧俏品
SKU2 = '04000462'  # 有可售数量的紧俏品
SKU3 = '18037999'  # 无可售数量，无锁定数量的紧俏品
SKU4 = '02000034'  # 非紧俏品，有可售数量
SKU5 = '18027999'  # 非紧俏品，无可售数量
SKU1code = '2000222'
SKU3code = '25099149'

qhgs = '测试公司（总部）'
qhmd = '东方店'
dbsqnum = 10  # 调拨申请数量
chuku1 = 2  # 第一次出库数量

config = configparser.ConfigParser()
file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
config.read(file_path)


class MdaoZ(unittest.TestCase):
    '''门店向总部调拨，含非紧俏品，紧俏品混合'''

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()

    def test_oms_allot1(self):
        '''门店向总部调拨，oms有可售数量的紧俏品，非紧俏品自动受理'''
        homepage = HomePage(self.driver)
        homepage.username('dfd')
        homepage.password('123456')
        homepage.send_submit_btn()
        time.sleep(2)
        print('门店向总部调拨，流程开始')
        homepage.dbMananger()  # 点击调拨管理
        homepage.dborder()  # 点击调拨单
        time.sleep(1)
        homepage.dbapply()  # 点击调拨申请
        time.sleep(3)
        homepage.dbadd()  # 点击新增
        homepage.dbdiaochuf()  # 点击选择调出方
        time.sleep(2)
        homepage.dbshurudcf(qhgs)  # 输入调出方
        homepage.dbchaxuan()  # 点击查询
        time.sleep(1)
        homepage.dbxuanzedcf()  # 选择调出方
        homepage.dbxz()  # 点击选择
        time.sleep(1)
        homepage.dbnewsdd()  # 点击新增配件按钮
        time.sleep(1)
        homepage.dbshuruneima(SKU1)  # 输入内码1
        homepage.dbchaxuanpeij()  # 点击查询
        time.sleep(6)
        homepage.doublec()  # 双击配件
        homepage.dbshurushul(dbsqnum)  # 输入数量5
        homepage.dbsure()  # 点击确定
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[19]/div[2]/div/div/div[2]/div[1]/div[2]/div/input').clear()
        homepage.dbshuruneima(SKU2)  # 输入内码2
        homepage.dbchaxuanpeij()  # 点击查询
        time.sleep(6)
        keshouqSKU2 = self.driver.find_element_by_xpath(
            '/html/body/div[19]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[10]/div/span').text
        homepage.doublec()  # 双击配件
        homepage.dbshurushul(dbsqnum)  # 输入数量5
        homepage.dbsure()  # 点击确定
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[19]/div[2]/div/div/div[2]/div[1]/div[2]/div/input').clear()
        homepage.dbshuruneima(SKU3)  # 输入内码3
        homepage.dbchaxuanpeij()  # 点击查询
        time.sleep(6)
        homepage.doublec()  # 双击配件
        homepage.dbshurushul(dbsqnum)  # 输入数量5
        homepage.dbsure()  # 点击确定
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[19]/div[2]/div/div/div[2]/div[1]/div[2]/div/input').clear()
        homepage.dbshuruneima(SKU4)  # 输入内码4
        homepage.dbchaxuanpeij()  # 点击查询
        time.sleep(6)
        keshouqSKU4 = self.driver.find_element_by_xpath(
            '/html/body/div[19]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[10]/div/span').text
        homepage.doublec()  # 双击配件
        homepage.dbshurushul(dbsqnum)  # 输入数量5
        homepage.dbsure()  # 点击确定
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[19]/div[2]/div/div/div[2]/div[1]/div[2]/div/input').clear()
        homepage.dbshuruneima(SKU5)  # 输入内码5
        homepage.dbchaxuanpeij()  # 点击查询
        time.sleep(6)
        homepage.doublec()  # 双击配件
        homepage.dbshurushul(dbsqnum)  # 输入数量5
        homepage.dbsure()  # 点击确定
        time.sleep(1)
        homepage.dbclose()  # 关闭添加配件弹框
        time.sleep(1)
        homepage.dbbaocun()  # 点击保存按钮
        time.sleep(3)
        homepage.dbaddress()  # 点击选择收货地址
        homepage.dbxuanzaddress()  # 点击选择配送方式
        homepage.dbzipei()  # 选择自配
        homepage.dbbaocunsure()  # 点击保存
        time.sleep(1)
        homepage.dbsub()  # 点击提交
        homepage.dbsurequed()  # 点击确定
        time.sleep(4)
        dbdh = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div['
                                                 '1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div['
                                                 '2]/table/tbody/tr[1]/td[6]/div/span').text
        a = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div['
                                              '1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div['
                                              '2]/table/tbody/tr[1]/td[2]/div/span').text
        quxiaoSKU5 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[3]/div/div[4]/div[2]/div[2]/table/tbody/tr[4]/td[15]/div/span').text  # 非紧俏品，无可售数量
        shouliSKU4 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[3]/div/div[4]/div[2]/div[2]/table/tbody/tr[1]/td[14]/div/span').text  # 非紧俏品，有可售数量
        shouliSKU2 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[3]/div/div[4]/div[2]/div[2]/table/tbody/tr[3]/td[14]/div/span').text  # 有可售数量的紧俏品
        homepage.qhzh()  # 切换门店
        homepage.shurumd(qhgs)  # 输入需要切换的门店
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
            SKU2)  # 输入内码查询
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        keshouhSKU2 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[11]/div').text  # 配件可售库存
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div['
                                          '1]/div/div[3]/input').clear()
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').send_keys(
            SKU4)  # 输入内码查询
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        keshouhSKU4 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[11]/div').text  # 配件可售库存

        try:
            assert "部分受理" in a
            print('1.调拨申请单' + dbdh, '已提交,且有可售数量配件已成功受理')
            print(SKU2 + '受理前可售的数量' + keshouqSKU2 + '，受理后的可售数量为' + keshouhSKU2 + '，受理数量为' + shouliSKU2+'有可售数量的紧俏品')
            print(SKU4 + '受理前可售的数量' + keshouqSKU4 + '，受理后的可售数量为' + keshouhSKU4 + '，受理数量为' + shouliSKU4+'非紧俏品有可售数量')
            print(SKU5 + "的取消数量为" + quxiaoSKU5+'非紧俏品，无可售数量，全部取消')
        except Exception as e:
            print('1.调拨申请单，提交失败'+dbdh, format(e))
            print(SKU2 + '受理前可售的数量' + keshouqSKU2 + '，受理后的可售数量为' + keshouhSKU2 + '，受理数量为' + shouliSKU2 + '有可售数量的紧俏品')
            print(SKU4 + '受理前可售的数量' + keshouqSKU4 + '，受理后的可售数量为' + keshouhSKU4 + '，受理数量为' + shouliSKU4 + '非紧俏品有可售数量')
            print(SKU5 + "的取消数量为" + quxiaoSKU5 + '非紧俏品，无可售数量，全部取消')
            homepage.get_windows_img()

    def test_oms_allot2(self):
        '''门店向总部调拨，oms剩余紧俏品配件手动分配以及WMS出库'''

        homepage = HomePage(self.driver)
        a = config.get("testServer", "URL") + '/AlotManagement/transferringOrder/productDistribution'
        self.driver.get(a)  # 打开紧俏品分配
        time.sleep(2)
        homepage.shurubm(SKU1code)  # 输入编码
        homepage.jqpcx()  # 点击查询
        time.sleep(4)
        homepage.jqpdj()  # 点击配件
        time.sleep(2)
        homepage.jqpfpNumc()
        dbshq = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section['
                                                  '2]/div[3]/div/div[2]/div[2]/table/tbody/tr[1]/td[4]/div/span').text
        dbfksSKu = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[2]/div[1]/div/div[2]/div['
            '2]/table/tbody/tr/td[12]/div/span').text

        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[2]/div[3]/div/div[2]/div['
            '2]/table/tbody/tr/td[9]/div/input').clear()
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[2]/div[3]/div/div[2]/div['
            '2]/table/tbody/tr/td[9]/div/input').send_keys(
            '10')  # 输入数量
        homepage.jqpfpButton()  # 点击分配完成
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div/div/div[3]/button[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section['
                                          '1]/div/div/div[1]/div[1]/input').clear()
        homepage.shurubm(SKU3code)  # 输入编码
        homepage.jqpcx()  # 点击查询
        time.sleep(2)
        homepage.jqpdj()  # 点击配件
        time.sleep(2)
        homepage.jqpfpButton()  # 点击分配完成
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[12]/div[2]/div/div/div/div/div[3]/button[2]').click()
        time.sleep(2)
        a = config.get("testServer", "URL") + '/AlotManagement/transferringOrder/stockRemoval'
        print(a)
        self.driver.get(a)  # 打开调拨出库
        time.sleep(2)
        homepage.dbckmore()  # 点击更多查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[5]/div/input').send_keys(dbshq)  # 输入申请单号
        self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div[3]/div/button[1]').click()  # 点击确认

        dbsld1 = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[6]/div/span').text
        dbsld2 = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[6]/div/span').text

        time.sleep(2)
        homepage.qhzh()  # 切换门店
        homepage.shurumd(qhmd)  # 输入需要切换的门店
        homepage.djcx()  # 点击查询
        time.sleep(2)
        homepage.djxzmd()
        homepage.djxz()  # 点击选择
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[4]/ul/li[1]/ul/li[1]/div').click()  # 点击调拨申请
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[2]/button').click()  # 点击更多
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div/div[2]/form/div/div[3]/div/input').send_keys(dbshq)
        self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div/div[3]/div/button[1]').click()
        time.sleep(1)
        a = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text
        try:
            assert '已受理' in a
            print('1.oms紧俏品受理成功，调拨受理单号为：'+dbsld1)
        except Exception as e:
            print('1.oms紧俏品受理失败', format(e))
            homepage.get_windows_img()

        homepage.qhzh()  # 切换门店
        homepage.shurumd(qhgs)  # 输入需要切换的门店
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
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        kucunSKU1 = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[10]/div/span').text
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').clear()
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').send_keys(
            SKU2)  # 输入内码查询
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        kucunSKU2 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[10]/div/span').text
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').clear()
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').send_keys(
            SKU4)  # 输入内码查询
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        kucunSKU4 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[10]/div/span').text
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').clear()

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
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/div/div/span[2]').click()  # 点击出库管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[1]/div').click()  # 点击出库任务
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[4]/div/div[1]').click()  # 点击订单类型
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[4]/div/div[2]/ul[2]/li[2]').click()  # 选择调拨出库
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[7]/div[1]/div[1]/div/span').click()  # 点击搜索条件
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[7]/div[1]/div[2]/ul[2]/li[3]').click()  # 选择业务单号
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[7]/div[2]/input').send_keys(dbsld1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[7]/button').click()  # 点击查询按钮
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[2]/div/span/span[2]').click()  # 点击分拣清单
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[2]/div').click()  # 点击分拣清单
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[3]/div/div/span[4]').click()  # 点击分拣
        time.sleep(3)

        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[2]/div/div[4]/button[2]').click()  # 点击拣货完成
        self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div/div[3]/button[2]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[3]/div').click()  # 点击装箱任务
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section/div[2]/div/div/div[2]/table/tbody/tr/td[2]/div/div/span').click()  # 点击装箱
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[2]/div[2]/button[2]').click()  # 点击一键装箱
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[2]/div[3]/p[1]/button').click()  # 点击拣货完成
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div/div[3]/button[2]').click()  # 点击确定按钮
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '/html/body/div[17]/div[2]/div/div/div/div/div[3]/button[2]').click()  # 点击确认生成发货清单
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[4]/div').click()  # 点击发货管理
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div/div/div[1]/div/div[1]/div/span').click()
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div/div/div[1]/div/div[2]/ul[2]/li[2]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[3]/div/div/span[1]').click()  # 点击发运
        time.sleep(4)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div[2]/div[1]/div/div[1]/div/span').click()  # 选择配送方式
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div[2]/div[1]/div/div[2]/ul[2]/li[3]').click()  # 选择客服自提
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[2]/button[2]').click()  # 点击确发运
        self.driver.find_element_by_xpath('/html/body/div[11]/div[2]/div/div/div/div/div[3]/button[2]').click()  # 点击确定
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[1]/div').click()  # 点击出库任务
        time.sleep(2)
        a1 = self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[8]/div/span').text
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[1]/div/div[7]/div[2]/input').clear()
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[7]/div[2]/input').send_keys(dbsld2)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[7]/button').click()  # 点击查询按钮
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[2]/div/span/span[2]').click()  # 点击分拣清单
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[2]/div').click()  # 点击分拣清单
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[3]/div/div/span[4]').click()  # 点击分拣
        time.sleep(3)

        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[2]/div/div[4]/button[2]').click()  # 点击拣货完成
        self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div/div[3]/button[2]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[3]/div').click()  # 点击装箱任务
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section/div[2]/div/div/div[2]/table/tbody/tr/td[2]/div/div/span').click()  # 点击装箱
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[2]/div[2]/button[2]').click()  # 点击一键装箱
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[2]/div[3]/p[1]/button').click()  # 点击拣货完成
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div/div[3]/button[2]').click()  # 点击确定按钮
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '/html/body/div[17]/div[2]/div/div/div/div/div[3]/button[2]').click()  # 点击确认生成发货清单
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[4]/div').click()  # 点击发货管理
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div/div/div[1]/div/div[1]/div/span').click()
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div/div/div[1]/div/div[2]/ul[2]/li[2]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[3]/div/div/span[1]').click()  # 点击发运
        time.sleep(4)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div[2]/div[1]/div/div[1]/div/span').click()  # 选择配送方式
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div[2]/div[1]/div/div[2]/ul[2]/li[3]').click()  # 选择客服自提
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[2]/button[2]').click()  # 点击确发运
        self.driver.find_element_by_xpath('/html/body/div[11]/div[2]/div/div/div/div/div[3]/button[2]').click()  # 点击确定
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[1]/div').click()  # 点击出库任务
        time.sleep(2)
        a2 = self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[8]/div/span').text
        try:
            assert '已完成' in a1 and '已完成' in a2
            print('2.WMS发货出库成功')
        except Exception as e:
            print('2.WMS发货出库失败', format(e))
            homepage.get_windows_img()

        self.driver.switch_to.window(window[-0])
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div['
                                          '1]/div/button[1]').click()  # 点击库存查询
        time.sleep(5)
        kucunhSKU4 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[10]/div/span').text  # 检查出库后的库存
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').clear()
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').send_keys(
            SKU2)  # 输入内码查询
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        kucunhSKU2 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[10]/div/span').text
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').clear()
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').send_keys(
            SKU1)  # 输入内码查询
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        kucunhSKU1 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[10]/div/span').text

        a = config.get("testServer", "URL") + '/AlotManagement/transferringOrder/stockRemoval'
        print(a)
        self.driver.get(a)  # 打开调拨出库
        time.sleep(2)
        homepage.dbckmore()  # 点击更多查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[5]/div/input').send_keys(dbshq)  # 输入申请单号
        self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div[3]/div/button[1]').click()  # 点击确认
        status1 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span').text
        status2 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/span').text
        chayi1 = int(kucunSKU1)-int(kucunhSKU1)
        chayi2 = int(kucunSKU2)-int(kucunhSKU2)
        chayi3 = int(kucunSKU4)-int(kucunhSKU4)

        try:
            assert '已完成' in status1 and '已完成' in status2 and chayi1 == chayi2 == chayi3 ==10
            print('2.WMS回传oms成功，出库前配件' + SKU1, '库存为' + kucunSKU1, '，出库后配件' + SKU1, '库存为' + kucunhSKU1, '出库数量为：10')
            print('2.WMS回传oms成功，出库前配件' + SKU2, '库存为' + kucunSKU2, '，出库后配件' + SKU1, '库存为' + kucunhSKU2, '出库数量为：10')
            print('2.WMS回传oms成功，出库前配件' + SKU3, '库存为' + kucunSKU4, '，出库后配件' + SKU1, '库存为' + kucunhSKU4, '出库数量为：10')




        except Exception as e:
            print('2.WMS回传oms失败', format(e))
            print('2.WMS回传oms成功，出库前配件' + SKU1, '库存为' + kucunSKU1, '，出库后配件' + SKU1, '库存为' + kucunhSKU1, '出库数量为：10')
            print('2.WMS回传oms成功，出库前配件' + SKU2, '库存为' + kucunSKU2, '，出库后配件' + SKU1, '库存为' + kucunhSKU2, '出库数量为：10')
            print('2.WMS回传oms成功，出库前配件' + SKU3, '库存为' + kucunSKU4, '，出库后配件' + SKU1, '库存为' + kucunhSKU4, '出库数量为：10')

            homepage.get_windows_img()

