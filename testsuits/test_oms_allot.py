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
dbsqnum = 5  # 调拨申请数量
chuku1 = 2  # 第一次出库数量

config = configparser.ConfigParser()
file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
config.read(file_path)

class MdaoZ(unittest.TestCase):
    '''门店向总部调拨，非紧俏品'''

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)





    def test_oms_allot1(self):
        '''门店向总部调拨，wms部分发货'''

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
        homepage.dbshuruneima(SKU1)  # 输入内码
        homepage.dbchaxuanpeij()  # 点击查询
        time.sleep(5)
        dbfksSKu = self.driver.find_element_by_xpath(
            '/html/body/div[19]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[10]/div/span').text  # 取调出方受理前的库存
        homepage.doublec()  # 双击配件
        homepage.dbshurushul(dbsqnum)  # 输入数量5
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
            assert "已受理" in a
            print('1.调拨申请单' + dbdh, '已提交')
        except Exception as e:
            print('1.调拨申请单，提交失败', format(e))
            homepage.get_windows_img()

        homepage.qhzh()  # 切换门店
        homepage.shurumd(qhgs)  # 输入需要切换的门店
        homepage.djcx()  # 点击查询
        time.sleep(2)
        homepage.djxzmd()
        homepage.djxz()  # 点击选择
        time.sleep(5)
        a = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[1]/div/div/div[3]/div/a[2]').text
        try:
            assert qhgs in a
            print('2.切换总部，查看调拨申请是否受理成功')
        except Exception as e:
            print('2.调切换总部失败', format(e))
            homepage.get_windows_img()

        homepage.dbck()  # 点击调拨出库
        time.sleep(2)
        homepage.dbckmore()  # 点击更多查询
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[34]/div[2]/div/div/div[2]/form/div/div[5]/div/input').send_keys(dbdh) # 输入申请单号
        self.driver.find_element_by_xpath('/html/body/div[34]/div[2]/div/div/div[3]/div/button[1]').click()  # 点击确认
        dbchuStatus = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div['
                                                        '1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div['
                                                        '2]/table/tbody/tr/td[2]/div/span').text
        dbsld = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div['
                                                  '1]/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div['
                                                  '2]/table/tbody/tr/td[6]/div/span').text

        try:
            assert '待出库' in dbchuStatus
            print("3.已成功自动受理，调拨受理单号为" + dbsld)
        except Exception as e:
            print('3.自动受理失败！！！', format(e))
            homepage.get_windows_img()
        time.sleep(5)
        ##############################################################################
        # 检查受理后的库存
        ##############################################################################
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
        dbslhkc = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[11]/div').text  # 配件可售库存
        zkucunq = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[10]/div/span').text
        zhanyong = int(dbfksSKu) - int(dbslhkc)
        try:
            assert zhanyong == 5
            print("4.受理前配件" + SKU1 + "的可售库存为" + dbfksSKu, ",受理后配件" + SKU1 + "的可售库存为" + dbslhkc, '占用库存为:5')
        except Exception as e:
            print('4.库存占用失败！！！', format(e))
            homepage.get_windows_img()
        a = config.get("testWms", "wms")
        js = "window.open(" + '"' + a + '"' + ")"  # 打开wms
        self.driver.execute_script(js)
        window = self.driver.window_handles
        self.driver.switch_to.window(window[-1])
        time.sleep(3)
        a = homepage.get_page_title()

        try:
            assert '极配WMS系统' in a
            print('5.成功进入wms系统，wms出库中，请等待。。。。。')
        except Exception as e:
            print('5.进入wms系统失败', format(e))
            homepage.get_windows_img()
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
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section/div[2]/div/div/div[2]/ul[2]/li[2]').click()  # 设置默认仓
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/div/div/span[2]').click()  # 点击出库管理
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[1]/div').click()  # 点击出库任务
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[4]/div/div[1]').click()  # 点击订单类型
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[4]/div/div[2]/ul[2]/li[2]').click()  # 选择调拨出库
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[7]/div[1]/div[1]/div/span').click()  # 点击搜索条件
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[7]/div[1]/div[2]/ul[2]/li[3]').click()  # 选择业务单号
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[7]/div[2]/input').send_keys(dbsld)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[7]/button').click()  # 点击查询按钮
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[2]/div/span/span[2]').click()  # 点击分拣清单
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[2]/div').click()  # 点击分拣清单
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr[1]/td[3]/div/div/span[4]').click()  # 点击分拣
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div[3]/div/div[2]/table/tbody/tr/td[9]/div/div/div[2]/input').clear()
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div[3]/div/div[2]/table/tbody/tr/td[9]/div/div/div[2]/input').send_keys(
            chuku1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div[3]/div/div[2]/table/tbody/tr/td[2]/div/div/span').click()  # 点击保存
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[2]/div/div[4]/button[2]').click()  # 点击拣货完成

        self.driver.find_element_by_xpath(
            '/html/body/div[10]/div[2]/div/div/div[2]/div/form/div/div/div/textarea').send_keys('少拣3个')
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
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div/div/div[1]/div/div[1]/div/span').click()
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div/div/div[1]/div/div[2]/ul[2]/li[2]').click()
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
        a = self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[8]/div/span').text
        try:
            assert '已完成' in a
            print('6.WMS发货出库成功')
        except Exception as e:
            print('6.WMS发货出库失败', format(e))
            homepage.get_windows_img()
        time.sleep(5)
        self.driver.switch_to.window(window[-0])
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div['
                                          '1]/div/button[1]').click()  # 点击库存查询
        time.sleep(5)
        zkucunh = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[10]/div/span').text  # 检查出库后的库存
        kucun = int(zkucunq) - int(zkucunh)
        homepage.dbck()  # 点击调拨出库
        time.sleep(2)
        a = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div['
            '1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span').text

        try:
            assert kucun == 2 and '部分出库' in a
            print('7.WMS回传oms成功，出库前配件' + SKU1, '库存为' + zkucunq, '，出库后配件' + SKU1, '库存为' + zkucunh, '出库数量为：2')
        except Exception as e:
            print('7.WMS回传oms失败，出库前配件' + SKU1, '库存为' + zkucunq, '，出库后配件' + SKU1, '库存为' + zkucunh, '出库数量为：2', format(e))
            homepage.get_windows_img()

    def test_oms_allot2(self):
        '''门店向总部调拨，wms再次出库'''
        homepage = HomePage(self.driver)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div['
                                          '1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        kucun1 = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[10]/div/span').text  # 检查再次出库前的库存
        window = self.driver.window_handles
        self.driver.switch_to.window(window[-1])
        time.sleep(3)
        chukudanhao = self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[3]/div/a').text  # 获取出库单号
        yewudanhao  = self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[13]/div/span').text  # 获取业务单号
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[6]/div').click()  # 点击出库差异
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div/div/div[4]/div[2]/input').send_keys(chukudanhao)  # 输入出库单号查询
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div/div/div[4]/button').click()  # 点击查询
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[2]/div/span/span[2]').click()  # 再次出库
        self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div/div/div/div[3]/button[2]').click()  # 点击确定
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)

        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[1]/div').click()  # 点击出库任务
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[1]/div').click()  # 点击出库任务
        time.sleep(1)

        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[4]/div/div[1]').click()  # 点击订单类型
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[4]/div/div[2]/ul[2]/li[2]').click()  # 选择调拨出库
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[7]/div[1]/div[1]/div/span').click()  # 点击搜索条件
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[7]/div[1]/div[2]/ul[2]/li[3]').click()  # 选择业务单号
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[1]/div/div[7]/div[2]/input').send_keys(yewudanhao)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[1]/div[1]/div/div[7]/button').click()  # 点击查询
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
            '//*[@id="right-content"]/div/section[2]/div[3]/div/div[2]/table/tbody/tr/td[9]/div/div/div[2]/input').clear()
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div[3]/div/div[2]/table/tbody/tr/td[9]/div/div/div[2]/input').send_keys(
            chuku1)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div[3]/div/div[2]/table/tbody/tr/td[2]/div/div/span').click()  # 点击保存
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div[2]/div/div[4]/button[2]').click()  # 点击拣货完成
        self.driver.find_element_by_xpath(
            '/html/body/div[10]/div[2]/div/div/div[2]/div/form/div/div/div/textarea').send_keys('少拣1个')
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
        a = self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[8]/div/span').text
        try:
            assert '已完成' in a
            print('1.WMS再次发货，出库成功')
        except Exception as e:
            print('1.WMS再次发货，出库失败', format(e))
            homepage.get_windows_img()
        time.sleep(5)
        self.driver.switch_to.window(window[-0])
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div['
                                          '1]/div/button[1]').click()  # 点击库存查询
        time.sleep(5)
        zkucunh = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div['
            '2]/table/tbody/tr/td[10]/div/span').text  # 检查出库后的库存
        kucun = int(kucun1) - int(zkucunh)
        homepage.dbck()  # 点击调拨出库
        time.sleep(2)
        a = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div['
            '1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span').text

        try:
            assert kucun == 2 and '部分出库' in a
            print('2.WMS回传oms成功，出库前配件' + SKU1, '库存为' + kucun1, '，出库后配件' + SKU1, '库存为' + zkucunh, '出库数量为：2')
        except Exception as e:
            print('2.WMS回传oms失败，出库前配件' + SKU1, '库存为' + kucun1, '，出库后配件' + SKU1, '库存为' + zkucunh, '出库数量为：2', format(e))
            homepage.get_windows_img()

    def test_oms_allot3(self):
        '''门店向总部调拨，wms确认差异'''
        homepage = HomePage(self.driver)
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div').click()  # 点击库存查询
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div['
                                          '1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        keshouNum = self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[11]/div').text
        window = self.driver.window_handles
        self.driver.switch_to.window(window[-1])
        time.sleep(3)
        chukudanhao = self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[3]/div/a').text  # 获取出库单号
        self.driver.find_element_by_xpath('//*[@id="leftInner"]/ul/li[3]/ul/li[6]/div').click()  # 点击出库差异
        time.sleep(1)

        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div/div/div[4]/div[2]/input').send_keys(chukudanhao)  # 输入出库单号查询
        self.driver.find_element_by_xpath(
            '//*[@id="right-content"]/div/section[1]/div/div/div[4]/button').click()  # 点击查询
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="right-content"]/div/section[2]/div/div/div[2]/table/tbody/tr/td[2]/div/span/span[1]').click()
        time.sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/div/div/div/div[3]/button[2]').click()
        time.sleep(2)
        self.driver.switch_to.window(window[-0])
        self.driver.find_element_by_xpath('//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div['
                                          '1]/div/button[1]').click()  # 点击查询
        time.sleep(5)
        cyhkeshouNum = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[11]/div').text

        homepage.dbck()  # 点击调拨出库
        time.sleep(2)
        a = self.driver.find_element_by_xpath(
            '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div['
            '1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span').text
        try:
            assert '已完成' in a
            print('1.wms确认差异成功')
        except Exception as e:
            print('1.wms确认差异失败', format(e))
            homepage.get_windows_img()
        chayi = int(cyhkeshouNum) - int(keshouNum)
        try:
            assert chayi == 1 and '已完成' in a
            print('2.WMS回传oms成功，确认差异前配件' + SKU1, '的可售库存为' + keshouNum, '，确认差异后配件' + SKU1, '可售库存为' + cyhkeshouNum, '差异数量为：1')
        except Exception as e:
            print('2.WMS回传oms失败，确认差异前配件' + SKU1, '的可售库存为' + keshouNum, '，确认差异后配件' + SKU1, '可售库存为' + cyhkeshouNum, '差异数量为：1', format(e))
            homepage.get_windows_img()








if __name__ == '__main__':
    unittest.main()
