# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.jp_homepage import HomePage
import configparser
import os.path

SKU1 = '02000034'  # 非紧俏品
qhgs = '测试公司（总部）'
qhmd = '东方店'
dbsqnum = 1  # 调拨申请数量
chuku1 = 2  # 第一次出库数量

config = configparser.ConfigParser()
file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
config.read(file_path)


class ZdaoM(unittest.TestCase):
    """总部向门店调拨以及总部wms入库回传"""

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_oms_allot1(self):
        """总部向门店调拨"""

        homepage = HomePage(self.driver)
        homepage.username('dfd')
        homepage.password('123456')
        homepage.send_submit_btn()
        time.sleep(2)
        homepage.qhzh()  # 切换门店
        homepage.shurumd(qhgs)  # 输入需要切换的门店
        homepage.djcx()  # 点击查询
        time.sleep(2)
        homepage.djxzmd()
        homepage.djxz()  # 点击选择
        time.sleep(5)
        print('门店向总部调拨，流程开始')
        homepage.dbMananger()  # 点击调拨管理
        homepage.dborder()  # 点击调拨单
        time.sleep(1)
        homepage.dbapply()  # 点击调拨申请
        time.sleep(3)
        homepage.dbadd()  # 点击新增
        homepage.dbdiaochuf()  # 点击选择调出方
        time.sleep(2)
        homepage.dbshurudcf(qhmd)  # 输入调出方
        homepage.dbchaxuan()  # 点击查询
        time.sleep(1)
        homepage.dbxuanzedcf()  # 选择调出方
        homepage.dbxz()  # 点击选择
        time.sleep(1)
        homepage.dbnewsdd()  # 点击新增配件按钮
        time.sleep(1)
        homepage.dbshuruneima(SKU1)  # 输入内码
        homepage.dbchaxuanpeij()  # 点击查询
        time.sleep(7)
        dbfksSKu = self.driver.find_element_by_xpath(
            '/html/body/div[19]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[10]/div/span').\
            text  # 取调出方受理前的库存
        homepage.doublec()  # 双击配件
        homepage.dbshurushul(dbsqnum)  # 输入数量1
        homepage.dbsure()  # 点击确定
        time.sleep(1)
        homepage.dbclose()  # 关闭添加配件弹框
        time.sleep(1)
        homepage.dbbaocun()  # 点击保存按钮
        time.sleep(2)
        homepage.dbaddress()  # 点击选择收货地址
        time.sleep(1)
        homepage.dbxuanzaddress()  # 点击选择配送方式
        homepage.dbzipei()  # 选择自配
        homepage.dbbaocunsure()  # 点击保存
        time.sleep(2)
        homepage.dbsub()  # 点击提交
        homepage.dbsurequed()  # 点击确定
        time.sleep(4)
        dbdh = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div['
                                                 '1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div['
                                                 '2]/table/tbody/tr[1]/td[6]/div/span').text
        a = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div['
                                              '1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div['
                                              '2]/table/tbody/tr[1]/td[2]/div/span').text

        try:
            assert "待受理" in a
            print('1.总部调拨申请单' + dbdh, '已提交')
        except Exception as e:
            print('1.总部调拨申请单，提交失败', format(e))
            homepage.get_windows_img()
        homepage.qhzh()  # 切换门店
        homepage.shurumd(qhmd)  # 输入需要切换的门店
        homepage.djcx()  # 点击查询
        time.sleep(2)
        homepage.djxzmd()
        homepage.djxz()  # 点击选择
        time.sleep(5)
        homepage.dbsqsl()  # 点击调拨申请受理
        time.sleep(2)
        homepage.dbsqdhsearch(dbdh)  # 输入申请单号
        homepage.dbsqdhchaxun()  # 点击查询
        time.sleep(2)
        homepage.dbsqslbutton()  # 点击受理
        time.sleep(1)
        homepage.dbsqslsure()  # 点击确定
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/div/div').click()  # 点击库存管理
        self.driver.switch_to_default_content()  # 到最外层
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').send_keys(
            SKU1)  # 输入内码查询
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/label/span/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        dbslhkc = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[11]/div').text  # 配件可售库存
        zkucunq = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[10]/div/span').text
        zhanyong = int(dbfksSKu) - int(dbslhkc)
        try:
            assert zhanyong == 1
            print("2.门店受理成功，受理前配件" + SKU1 + "的可售库存为" + dbfksSKu, ",受理后配件" + SKU1 + "的可售库存为" + dbslhkc, '占用库存为:1')
        except Exception as e:
            print('2.门店受理失败！！！' + SKU1 + "的可售库存为" + dbfksSKu, ",受理后配件" + SKU1 + "的可售库存为" + dbslhkc, '占用库存为:1',
                  format(e))
            homepage.get_windows_img()

        homepage.dbck()  # 点击调拨出库
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[2]/button').click()  # 点击更多查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[45]/div[2]/div/div/div[2]/form/div/div[5]/div/input').send_keys(dbdh)
        self.driver.find_element_by_xpath('/html/body/div[45]/div[2]/div/div/div[3]/div/button[1]').click()  # 点击确定
        time.sleep(2)
        dbchuStatus = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div['
                                                        '1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div['
                                                        '2]/table/tbody/tr/td[2]/div/span').text
        dbsld = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div['
                                                  '1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div['
                                                  '2]/table/tbody/tr/td[6]/div/span').text
        print(dbsld+'，'+dbchuStatus)

        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[3]/div/span').click()  # 点击要出库的调拨出库单

        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[5]/button').click()  # 点击提交
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[90]/div[2]/div/div/div/div/div[3]/button[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[6]/button').click()  # 点击出库
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[90]/div[2]/div/div/div/div/div[3]/button[2]').click()
        time.sleep(2)
        status = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span').text
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        zkucunh = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[10]/div/span').text
        jskucun = int(zkucunq) - int(zkucunh)
        try:
            assert jskucun == 1 and '已完成' in status
            print("3.门店出库成功，出库前配件" + SKU1 + "的库存为" + zkucunq, ",出库后配件" + SKU1 + "的可售库存为" + zkucunh, '出库数量为:1')
        except Exception as e:
            print('3.门店出库失败！！！' + SKU1 + "的库存为" + zkucunq, ",出库后配件" + SKU1 + "的可售库存为" + zkucunh, '出库数量为:1',
                  format(e))
            homepage.get_windows_img()

        homepage.qhzh()  # 切换门店
        homepage.shurumd(qhgs)  # 输入需要切换的门店
        homepage.djcx()  # 点击查询
        time.sleep(2)
        homepage.djxzmd()
        homepage.djxz()  # 点击选择
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').send_keys(
            SKU1)  # 输入内码查询
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        dbslhkc = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[11]/div').text  # 配件可售库存
        thrukuq = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[10]/div/span').text  # 配件库存
        homepage.dbMananger()  # 点击调拨管理
        homepage.dborder()  # 点击调拨单
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[4]/ul/li[1]/ul/li[4]/div').click()  # 点击调拨入库
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[3]/button').click()  # 点击新增
        time.sleep(1)
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
        dcthrkd = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[6]/div/span').text
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
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[4]/div/div[2]/ul[2]/li[2]').click()  # 选择调拨退货
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
                    '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[2]/button').click()  # 点击更多查询
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[20]/div[2]/div/div/div[2]/form/div/div[4]/div/input').send_keys(dcthrkd)
                self.driver.find_element_by_xpath('/html/body/div[20]/div[2]/div/div/div[3]/div/button[1]').click()  # 点击确定
                time.sleep(2)
                a = self.driver.find_element_by_xpath(
                    '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text
                self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
                time.sleep(2)
                self.driver.find_element_by_xpath(
                    '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
                time.sleep(5)
                thrukuh = self.driver.find_element_by_xpath(
                    '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
                    '2]/table/tbody/tr/td[10]/div/span').text  # 获取门店库存
                chayi = int(thrukuh) - int(thrukuq)
                try:
                    assert chayi == 1 and '已入库' in a
                    print('4.总部入库成功，入库前配件' + SKU1, '的库存为' + thrukuq, '，入库后配件' + SKU1, '的库存为' + thrukuh, '入库数量为：1')
                except Exception as e:
                    print('4.总部入库失败，入库前配件' + SKU1, '的库存为' + thrukuq, '，入库后配件' + SKU1, '的库存为' + thrukuh, '入库数量为：1',
                          format(e))
                break
            else:
                a = adanhao
        else:
            print('wms回传异常')

    def test_oms_allot2(self):
        """总部调入退回，wms出库"""
        homepage = HomePage(self.driver)
        thrukuq = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[10]/div/span').text  # 获取门店库存
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

        self.driver.find_element_by_xpath('//input[@class="el-input__inner"]').send_keys(
            qhmd)  # 输入调出方
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
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div['
            '1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text
        drthsqd = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div['
            '1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[6]/div/span').text
        try:
            assert "待受理" in a
            print('1.总部调入退回申请单' + drthsqd, '已提交')
        except Exception as e:
            print('1.总部调入退回申请单' + drthsqd, '已提交', format(e))
            homepage.get_windows_img()
        homepage.qhzh()  # 切换门店
        homepage.shurumd(qhmd)  # 输入需要切换的门店
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
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[2]/div[1]/div/div[2]/div['
            '2]/table/tbody/tr/td[2]/div/button[1]').click()  # 点击受理
        self.driver.find_element_by_xpath('/html/body/div[19]/div[2]/div/div/div[3]/button[2]').click()  # 点击确定
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        homepage.qhzh()  # 切换门店
        homepage.shurumd(qhgs)  # 输入需要切换的门店
        homepage.djcx()  # 点击查询
        time.sleep(2)
        homepage.djxzmd()
        homepage.djxz()  # 点击选择
        time.sleep(5)

        window = self.driver.window_handles
        self.driver.switch_to.window(window[-1])
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/div').click()  # 点击出库管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[7]/div').click()  # 点击其他出库
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[1]/div/div[4]/div/div[1]/div/span').click()  # 点击订单类型
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[1]/div/div[4]/div/div[2]/ul[2]/li[3]').click()  # 订单类型选择调入退回
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/div[1]/div[1]/div/span').click()  # 选择查询条件
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/div[1]/div[2]/ul[2]/li[3]').click()  # 选择业务单号
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/div[2]/input').send_keys(drthsqd)  # 输入业务单号
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[1]/div/div[6]/button[1]').click()  # 点击查询
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[2]/div/a').click()  # 点击出库单号
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[2]/button').click()  # 点击确认出库
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div/div[3]/button[2]').click()  # 点击确定
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[6]/ul/li[3]/div').click()  # 点击接口同步日志
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div/button').click()  # 点击查询按钮
        time.sleep(2)

        a = self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[3]/div/span').text  # 获取wms接口日志第一条的业务单号

        while a not in drthsqd:
            time.sleep(5)
            self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div/button').click()
            time.sleep(1)
            adanhao = self.driver.find_element_by_xpath(
                '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[3]/div/span').text
            status = self.driver.find_element_by_xpath(
                '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[5]/div/span').text
            print(adanhao)

            if adanhao in drthsqd and '成功' in status:
                self.driver.switch_to.window(window[-0])
                time.sleep(5)
                self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[4]/ul/li[2]/ul/li[1]/div').click()  #
                time.sleep(2)
                self.driver.find_element_by_xpath(
                    '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[2]/button').click()  # 点击更多查询
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[4]/div/input').send_keys(drthsqd)
                self.driver.find_element_by_xpath('/html/body/div[9]/div[2]/div/div/div[3]/div/button[1]').click()  # 点击确定
                time.sleep(2)
                a = self.driver.find_element_by_xpath(
                    '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/div/span').text

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
                thrukuh = self.driver.find_element_by_xpath(
                    '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
                    '2]/table/tbody/tr/td[10]/div/span').text  # 获取门店库存
                chayi = int(thrukuq) - int(thrukuh)
                try:
                    assert chayi == 1 and '已完成' in a
                    print('2.总部出库成功，出库前配件' + SKU1, '的库存为' + thrukuq, '，出库后配件' + SKU1, '的库存为' + thrukuh, '出库数量为：1')
                except Exception as e:
                    print('2.总部出库失败，出库前配件' + SKU1, '的库存为' + thrukuq, '，出库后配件' + SKU1, '的库存为' + thrukuh, '出库数量为：1',
                          format(e))
                break
            else:
                a = adanhao
        else:
            print('wms回传异常')

        homepage.qhzh()  # 切换门店
        homepage.shurumd(qhmd)  # 输入需要切换的门店
        homepage.djcx()  # 点击查询
        time.sleep(2)
        homepage.djxzmd()
        homepage.djxz()  # 点击选择
        time.sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input').send_keys(
            SKU1)  # 输入内码查询
        self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        thrukuq = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[10]/div/span').text  # 获取门店库存
        homepage.dbMananger()  # 点击调拨管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[4]/ul/li[2]/div/div').click()  # 点击调拨退货
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[4]/ul/li[2]/ul/li[2]/div').click()  # 点击调出退回入库
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/div/span').click()  # 选择入库单据
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[1]/div/div/div[3]/button').click()  # 点击入库
        self.driver.find_element_by_xpath('/html/body/div[22]/div[2]/div/div/div[3]/button[2]').click()  # 点击确定
        time.sleep(4)
        self.driver.refresh()
        time.sleep(4)
        a = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span').text





