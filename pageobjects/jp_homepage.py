from framework.base_page import BasePage


class HomePage(BasePage):
    '''登录页'''
    input_box_un = 'xpath=>//*[@id="app"]/div/div[2]/div/div/div/form/div[2]/div/div/input'  # 用户名

    def username(self, text):  # 输入用户名
        self.type(self.input_box_un, text)


    input_box_pw = 'xpath=>//*[@id="app"]/div/div[2]/div/div/div/form/div[3]/div/div/input'  # 密码

    def password(self, text):  # 输入密码
        self.type(self.input_box_pw, text)

    login_submit_btn1 = 'xpath=>/html/body/div[1]/div/div[2]/div/div/div/form/div[5]/div'  # 登录提交

    def send_submit_btn(self):  # 提交按钮
        self.click(self.login_submit_btn1)

    '''基础设置'''
    qhzh1 = 'xpath=>//*[@id="routes"]/div[2]/div[1]/div/div/div[3]/div/a[2]'  # 点击门店切换

    def qhzh(self):
        self.click(self.qhzh1)

    shurumd1 = 'xpath=>/html/body/div[6]/div[2]/div/div/div/header/div/input'  # 输入切换的门店

    def shurumd(self, text):
        self.type(self.shurumd1, text)

    djcx1 = 'xpath=>/html/body/div[6]/div[2]/div/div/div/header/button[1]'  # 点击查询

    def djcx(self):
        self.click(self.djcx1)

    djxzmd1 = 'xpath=>/html/body/div[6]/div[2]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[1]/div/span'  # 选择门店

    def djxzmd(self):
        self.click(self.djxzmd1)

    djxz1 = 'xpath=>/html/body/div[6]/div[2]/div/div/div/header/button[2]'  # 点击选择

    def djxz(self):
        self.click(self.djxz1)

    '''采购管理'''
    purchaseManagement1 = 'xpath=>//*[@id="leftInner"]/ul/li[2]/div/div'  # 采购管理

    def purchaseManagement(self):  # 采购管理
        self.click(self.purchaseManagement1)

    '''采购管理-滚动计划'''
    purchasePlan1 = "xpath=>/html/body/div[1]/div/div[1]/div[1]/div/div[4]/ul/li[2]/ul/li[1]/div/span[2]"  # 滚动计划单

    def purchasePlan(self):  # 滚动计划单
        self.click(self.purchasePlan1)


    ppadd1 = "xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[3]/button"  # 新增

    def ppadd(self):  # 新增
        self.click(self.ppadd1)

    xzgysButton1 = "xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[3]/di" \
                   "v/div[2]/form/div[1]/div/div/div[2]"  # 选择供应商

    def xzgysButton(self):
        self.click(self.xzgysButton1)

    gysSearch1 = "xpath=>/html/body/div[21]/div[2]/div/div/div[2]/div[1]/div[1]/input"  # 输入供应商名称

    def gysSearch(self, text):  # 条件输入
        self.type(self.gysSearch1, text)

    searchButton1 = "xpath=>/html/body/div[21]/div[2]/div/div/div[2]/div[1]/button[1]"  # 点击 查询按钮

    def searchButton(self):
        self.click(self.searchButton1)

    doubleBill1 = "xpath=>/html/body/div[21]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody"  # 双击供应商

    def doubleBill(self):
        self.doubleclick(self.doubleBill1)

    addsku1 = "xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[3]/div/div[3]/div/div[1]/button"  # 新增配件

    def addsku(self):
        self.click(self.addsku1)

    skusearch1 = "xpath=>/html/body/div[11]/div[2]/div/div/div[2]/div[1]/div[2]/div/input"  # 输入配件

    def skusearch(self, text):
        self.type(self.skusearch1, text)

    skuchaxun1 = "xpath=>/html/body/div[11]/div[2]/div/div/div[2]/div[1]/button[1]"  # 选择查询

    def skuchaxun(self):
        self.click(self.skuchaxun1)

    doublesku1 = "xpath=>/html/body/div[11]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/table/tbody"  # 双击配件

    def doublesku(self):
        self.doubleclick(self.doublesku1)

    caigouNum1 = "xpath=>/html/body/div[19]/div[2]/div/div/div[2]/form/div[4]/div[1]/div/div/div/input"  # 输入采购数量

    def caigouNum(self, text):
        self.type(self.caigouNum1, text)

    caigouPrice1 = "xpath=>/html/body/div[19]/div[2]/div/div/div[2]/form/div[5]/div[1]/div/div/div/input"  # 输入采购单价

    def caigouPrice(self, text):
        self.type(self.caigouPrice1, text)

    caigouSure1 = "xpath=>/html/body/div[19]/div[2]/div/div/div[3]/div/button[1]"  # 点击确定

    def caigouSure(self):
        self.click(self.caigouSure1)

    gddaoru1 = '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[3]/div/div[3]/div/div[2]/div/div[1]/button'  # 点击导入

    def gddaoru(self):
        self.click(self.gddaoru1)

    gddaoruneima1 = '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[3]/div/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/button'  # 点击导入内码

    def gddaoruneima(self):
        self.click(self.gddaoruneima1)

    skuclose1 = "xpath=>/html/body/div[11]/div[2]/div/div/div[2]/div[1]/button[3]"  # 关掉配件选择弹框

    def skuclose(self):
        self.click(self.skuclose1)

    orderplan1 = "xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[4]/button"  # 保存滚动计划单

    def orderplan(self):
        self.click(self.orderplan1)



    orderplansub1 = "xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[5]/button"  # 提交滚动计划单

    def orderplansub(self):
        self.click(self.orderplansub1)

    gdmore1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[2]/button'  # 点击更多

    def gdmore(self):
        self.click(self.gdmore1)

    gdmoreshuru1 = 'xpath=>/html/body/div[24]/div[2]/div/div/div[2]/form/div[3]/div/div/input'  # 输入滚动计划单

    def gdmoreshuru(self, text):
        self.type(self.gdmoreshuru1, text)

    gdmoresure = 'xpath=>/html/body/div[24]/div[2]/div/div/div[3]/div/button[1]'  # 点击确定

    def gdmoresur(self):
        self.click(self.gdmoresure)

    '''采购管理-计划采购订单'''
    planCaigouPlan1 = "xpath=>/html/body/div[1]/div/div[1]/div[1]/div/div[4]/ul/li[2]/ul/li[2]/div/span[2]"  # 点击计划采购订单

    def planCaigouPlan(self):
        self.click(self.planCaigouPlan1)

    pcadd1 = "xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[4]/button"  # 点击新增按钮

    def pcadd(self):
        self.click(self.pcadd1)

    pcxzgys1 = "xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[3]/div/" \
               "div[2]/form/div[1]/div/div/div[2]/button"  # 打开新增供应商弹框

    def pcxzgys(self):
        self.click(self.pcxzgys1)

    pcxzgymc1 = "xpath=>/html/body/div[49]/div[2]/div/div/div[2]/div[1]/div/input"  # 输入供应商名称

    def pcxzgymc(self, text):
        self.type(self.pcxzgymc1, text)

    pcxzgyscx1 = "xpath=>/html/body/div[49]/div[2]/div/div/div[2]/div[1]/button[1]"  # 搜索按钮

    def pcxzgyscx(self):
        self.click(self.pcxzgyscx1)

    doublegys1 = "xpath=>/html/body/div[49]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody"  # 计划采购订单，双击供应商

    def doublegys(self):
        self.doubleclick(self.doublegys1)

    pcuxgdjh1 = "xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[3]/div/div[3]/div/div[1]/button"  # 点击选择滚动计划

    def pcuxgdjh(self):
        self.click(self.pcuxgdjh1)

    jhorder1 = 'xpath=>/html/body/div[52]/div[2]/div/div/div[2]/div[1]/div[1]/div[4]/div/input'  # 输入计划采购订单

    def jhorder(self, text):
        self.type(self.jhorder1, text)

    jhsearchbutton1 = 'xpath=>/html/body/div[52]/div[2]/div/div/div[2]/div[1]/div[1]/div[5]/button'  # 点击查询按钮

    def jhsearchbutton(self):
        self.click(self.jhsearchbutton1)

    pcxzgdjh1 = "xpath=>/html/body/div[52]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]/div/span"  # 选择具体的滚动计划单

    def pcxzgdjh(self):
        self.click(self.pcxzgdjh1)

    pcxz1 = "xpath=>/html/body/div[52]/div[2]/div/div/div[2]/div[1]/div[1]/div[6]/button"  # 点击选择按钮

    def pcxz(self):
        self.click(self.pcxz1)

    pcsave1 = "xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[5]/button"  # 点击保存

    def pcsave(self):
        self.click(self.pcsave1)

    pcsub1 = "xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[6]/button"  # 点击提交

    def pcsub(self):
        self.click(self.pcsub1)

    pcsre1 = "xpath=>/html/body/div[62]/div[2]/div/div/div/div/div[3]/button[2]"  # 点击确定

    def pcsre(self):
        self.click(self.pcsre1)

    '''临时采购订单'''
    lsCaigouOrder1 = 'xpath=>//*[@id="leftInner"]/ul/li[2]/ul/li[4]/div/span[2]'  # 点击临时采购订单

    def lsCaigouOrder(self):
        self.click(self.lsCaigouOrder1)

    lsadd1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[4]/button'  # 点击新增按钮

    def lsadd(self):
        self.click(self.lsadd1)

    lsxzgys1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[3]/div/div[2]' \
               '/form/div[1]/div/div/div[2]/button'  # 选择供应商按钮

    def lsxzgys(self):
        self.click(self.lsxzgys1)

    lsgys1 = "xpath=>/html/body/div[27]/div[2]/div/div/div[2]/div[1]/div/input"  # 输入供应商名称

    def lsgys(self, text):
        self.type(self.lsgys1, text)

    lsgysSearch1 = "xpath=>/html/body/div[27]/div[2]/div/div/div[2]/div[1]/button[1]"  # 搜索按钮

    def lsgysSearch(self):
        self.click(self.lsgysSearch1)

    lsgysxz1 = "xpath=>/html/body/div[27]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody/tr"  # 双击选择供应商

    def lsgysxz(self):
        self.doubleclick(self.lsgysxz1)

    lssddSku1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[3]/div/div[3]' \
                '/div/div[1]/button'  # 选择配件弹框

    def lssddSku(self):
        self.click(self.lssddSku1)

    lsskuSeaech1 = "xpath=>/html/body/div[40]/div[2]/div/div/div[2]/div[1]/div[2]/div/input"  # 输入配件

    def lsskuSeaech(self, text):
        self.type(self.lsskuSeaech1, text)

    lsskusearchButton1 = "xpath=>/html/body/div[40]/div[2]/div/div/div[2]/div[1]/button[1]"  # 点击查询

    def lsskusearchButton(self):
        self.click(self.lsskusearchButton1)

    lsxzsku1 = "xpath=>/html/body/div[40]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[2]/div/label/span/input"  # 双击选择配件

    def lsxzsku(self):
        self.doubleclick(self.lsxzsku1)

    lsskuNum1 = "xpath=>/html/body/div[48]/div[2]/div/div/div[2]/form/div[4]/div[1]/div/div/div/input"  # 输入数量

    def lsskuNum(self, text):
        self.type(self.lsskuNum1, text)

    lsskuPrice1 = "xpath=>/html/body/div[48]/div[2]/div/div/div[2]/form/div[5]/div[1]/div/div/div/input"  # 输入单价

    def lsskuPrice(self, text):
        self.type(self.lsskuPrice1, text)

    lssure1 = "xpath=>/html/body/div[48]/div[2]/div/div/div[3]/div/button[1]"  # 点击确定按钮

    def lssure(self):
        self.click(self.lssure1)

    lsclose1 = "xpath=>/html/body/div[40]/div[2]/div/div/div[2]/div[1]/button[3]"  # 点击关闭添加配件弹框

    def lsclose(self):
        self.click(self.lsclose1)

    lsSave1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[5]/button'  # 点击保存按钮

    def lsSave(self):
        self.click(self.lsSave1)

    lsSub1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[6]/button'  # 点击提交按钮

    def lsSub(self):
        self.click(self.lsSub1)

    lsSubSure1 = 'xpath=>/html/body/div[52]/div[2]/div/div/div/div/div[3]/button[2]'  # 点击确定

    def lsSubSure(self):
        self.click(self.lsSubSure1)

    lsdjStatus1 = '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[1]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/div/span'  # 获取单据状态

    def lsdjStatus(self):
        self.wenben(self.lsdjStatus1)

    '''外采订单'''
    wcCaigouOrder1 = 'xpath=>//*[@id="leftInner"]/ul/li[2]/ul/li[5]'  # 点击外采订单

    def wcCaigouOrder(self):
        self.click(self.wcCaigouOrder1)

    wcadd1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[4]/button'  # 点击新增按钮

    def wcadd(self):
        self.click(self.wcadd1)

    wcxzgys1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[3]/div/div[2]/form/div[1]/div/div/div[2]/button/span/i'  # 选择供应商按钮

    def wcxzgys(self):
        self.click(self.wcxzgys1)

    wcgys1 = "xpath=>/html/body/div[94]/div[2]/div/div/div[2]/div[1]/div[1]/input"  # 输入供应商名称

    def wcgys(self, text):
        self.type(self.wcgys1, text)

    wcgysSearch1 = "xpath=>/html/body/div[94]/div[2]/div/div/div[2]/div[1]/button[1]"  # 搜索按钮

    def wcgysSearch(self):
        self.click(self.wcgysSearch1)

    wcgysxz1 = "xpath=>/html/body/div[94]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/table/tbody"  # 双击选择供应商

    def wcgysxz(self):
        self.doubleclick(self.wcgysxz1)

    wcsddSku1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[2]/div/div/div/div/div[3]/div/div[3]/div/div[1]/button'  # 选择配件弹框

    def wcsddSku(self):
        self.click(self.wcsddSku1)

    wcskuSeaech1 = "xpath=>/html/body/div[108]/div[2]/div/div/div[2]/div[1]/div/input"  # 输入配件

    def wcskuSeaech(self, text):
        self.type(self.wcskuSeaech1, text)

    wcskusearchButton1 = "xpath=>/html/body/div[108]/div[2]/div/div/div[2]/div[1]/button[1]"  # 点击查询

    def wcskusearchButton(self):
        self.click(self.wcskusearchButton1)

    wcxzsku1 = "xpath=>/html/body/div[108]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/table/tbody"  # 双击选择配件

    def wcxzsku(self):
        self.doubleclick(self.wcxzsku1)

    wcskuNum1 = "xpath=>/html/body/div[116]/div[2]/div/div/div[2]/form/div[4]/div[1]/div/div/div/input"  # 输入数量

    def wcskuNum(self, text):
        self.type(self.wcskuNum1, text)

    wcskuPrice1 = "xpath=>/html/body/div[116]/div[2]/div/div/div[2]/form/div[5]/div[1]/div/div/div/input"  # 输入单价

    def wcskuPrice(self, text):
        self.type(self.wcskuPrice1, text)

    wcsure1 = "xpath=>/html/body/div[116]/div[2]/div/div/div[3]/div/button[1]"  # 点击确定按钮

    def wcsure(self):
        self.click(self.wcsure1)

    wcclose1 = "xpath=>/html/body/div[108]/div[2]/div/div/div[2]/div[1]/button[3]"  # 点击关闭添加配件弹框

    def wcclose(self):
        self.click(self.wcclose1)

    wcSave1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[5]/button'  # 点击保存按钮

    def wcSave(self):
        self.click(self.wcSave1)

    wcSub1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[6]/button'  # 点击提交按钮

    def wcSub(self):
        self.click(self.wcSub1)

    wcSubSure1 = 'xpath=>/html/body/div[140]/div[2]/div/div/div/div/div[3]/button[2]'  # 点击确定

    def wcSubSure(self):
        self.click(self.wcSubSure1)

    '''调拨申请'''
    dbMananger1 = 'xpath=>//*[@id="leftInner"]/ul/li[4]/div'  # 点击调拨管理

    def dbMananger(self):
        self.click(self.dbMananger1)

    dborder1 = 'xpath=>//*[@id="leftInner"]/ul/li[4]/ul/li[1]/div/div'  # 点击调拨单

    def dborder(self):
        self.click(self.dborder1)

    dbapply1 = 'xpath=>//*[@id="leftInner"]/ul/li[4]/ul/li[1]/ul/li[1]/div'  # 点击调拨申请

    def dbapply(self):
        self.click(self.dbapply1)

    dbadd1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[3]/button'  # 点击新增

    def dbadd(self):
        self.click(self.dbadd1)

    dbdiaochuf1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[' \
                  '3]/div/div[2]/form/div[1]/div/div/div[2]/button'  # 点击选择调出方

    def dbdiaochuf(self):
        self.click(self.dbdiaochuf1)

    dbshurudcf1 = 'xpath=>/html/body/div[32]/div[2]/div/div/div[2]/div[1]/div/input'  # 输入调出方

    def dbshurudcf(self, text):
        self.type(self.dbshurudcf1, text)

    dbchaxuan1 = 'xpath=>/html/body/div[32]/div[2]/div/div/div[2]/div[1]/button[1]'  # 点击查询

    def dbchaxuan(self):
        self.click(self.dbchaxuan1)

    dbxuanzedcf1 = 'xpath=>/html/body/div[32]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[3]'  # 选择调出方

    def dbxuanzedcf(self):
        self.click(self.dbxuanzedcf1)

    dbxz1 = 'xpath=>/html/body/div[32]/div[2]/div/div/div[2]/div[1]/button[2]'  # 点击选择

    def dbxz(self):
        self.click(self.dbxz1)

    dbnewsdd1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[' \
                '3]/div/div[3]/div/div[1]/button'  # 点击新增配件按钮

    def dbnewsdd(self):
        self.click(self.dbnewsdd1)

    dbshuruneima1 = 'xpath=>/html/body/div[19]/div[2]/div/div/div[2]/div[1]/div[2]/div/input'  # 输入内码

    def dbshuruneima(self, text):
        self.type(self.dbshuruneima1, text)

    dbchaxuanpeij1 = 'xpath=>/html/body/div[19]/div[2]/div/div/div[2]/div[1]/button[1]'  # 点击查询

    def dbchaxuanpeij(self):
        self.click(self.dbchaxuanpeij1)

    doublec1 = "xpath=>/html/body/div[19]/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/table/tbody/tr/td[2]/div/label/span/input"  # 双击配件

    def doublec(self):
        self.doubleclick(self.doublec1)

    dbshurushul1 = 'xpath=>/html/body/div[26]/div[2]/div/div/div[2]/form/div[4]/div[1]/div/div/div/input'  # 输入数量5'

    def dbshurushul(self, text):
        self.type(self.dbshurushul1, text)

    dbsure1 = 'xpath=>/html/body/div[26]/div[2]/div/div/div[3]/div/button[1]'  # 点击确定

    def dbsure(self):
        self.click(self.dbsure1)

    dbclose1 = 'xpath=>/html/body/div[19]/div[2]/div/div/a/i'  # 关闭添加配件弹框

    def dbclose(self):
        self.click(self.dbclose1)

    dbbaocun1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[4]/button'  # 点击保存按钮

    def dbbaocun(self):
        self.click(self.dbbaocun1)

    dbaddress1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[2]/div/div/div/div/div[3]/div/div[3]/div/div[5]/button'  # 点击选择收货地址

    def dbaddress(self):
        self.click(self.dbaddress1)

    dbxuanzaddress1 = 'xpath=>/html/body/div[31]/div[2]/div/div/div[2]/div/div[2]/div[2]/form/div[6]/div/div/div[1]/div/span'  # 点击选择配送方式

    def dbxuanzaddress(self):
        self.click(self.dbxuanzaddress1)

    dbzipei1 = 'xpath=>/html/body/div[31]/div[2]/div/div/div[2]/div/div[2]/div[2]/form/div[6]/div/div/div[2]/ul[2]/li[1]'  # 选择自配

    def dbzipei(self):
        self.click(self.dbzipei1)

    dbbaocunsure1 = 'xpath=>/html/body/div[31]/div[2]/div/div/div[2]/div/div[1]/form/button[2]'  # 点击保存

    def dbbaocunsure(self):
        self.click(self.dbbaocunsure1)

    dbsub1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[5]/button'  # 点击提交

    def dbsub(self):
        self.click(self.dbsub1)

    dbsurequed1 = 'xpath=>/html/body/div[36]/div[2]/div/div/div/div/div[3]/button[2]'  # 点击确定

    def dbsurequed(self):
        self.click(self.dbsurequed1)

    '''调拨申请受理'''
    dbsqsl1 = 'xpath=>//*[@id="leftInner"]/ul/li[4]/ul/li[1]/ul/li[2]/div'  # 调拨申请受理

    def dbsqsl(self):
        self.click(self.dbsqsl1)

    dbsqdhsearch1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[1]/div/div/div[4]/div[2]/input'  # 输入调拨申请单号

    def dbsqdhsearch(self, text):
        self.type(self.dbsqdhsearch1, text)

    dbsqdhchaxun1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[1]/div/div/div[4]/button'  # 点击查询按钮

    def dbsqdhchaxun(self):
        self.click(self.dbsqdhchaxun1)

    dbsqslbutton1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[2]/div/div[1]/div/div/div[2]/div[2]/table/tbody/tr/td[2]/div/div/button[1]'  # 点击受理

    def dbsqslbutton(self):
        self.click(self.dbsqslbutton1)

    dbsqslsure1 = 'xpath=>/html/body/div[59]/div[2]/div/div/div/div/div[3]/button[2]'  # 点击确认

    def dbsqslsure(self):
        self.click(self.dbsqslsure1)

    '''调拨出库'''

    dbck1 = 'xpath=>//*[@id="leftInner"]/ul/li[4]/ul/li[1]/ul/li[3]'  # 点击调拨出库菜单

    def dbck(self):
        self.click(self.dbck1)

    dbckmore1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[2]/button'  # 更多查询

    def dbckmore(self):
        self.click(self.dbckmore1)

    dbckmapply1 = 'xpath=>/html/body/div[34]/div[2]/div/div/div[2]/form/div/div[5]/div/input'  # 输入申请单号

    def dbckmapply(self, text):
        self.type(self.dbckmapply1, text)

    dbckmsure1 = 'xpath=>/html/body/div[34]/div[2]/div/div/div[3]/div/button[1]'  # 点击确认
    dbckmsure1 = 'xpath=>/html/body/div[34]/div[2]/div/div/div[3]/div/button[1]'  # 点击确认

    def dbckmsure(self):
        self.click(self.dbckmsure1)

    dbckutijiao1 = '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[5]/button'  # 点击提交

    dbckutjsuren1 = '/html/body/div[90]/div[2]/div/div/div/div/div[3]/button[2]'  # 点击确认

    dbchuchuku1 = '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/main/div[1]/section[1]/div/div/div[6]/button'  # 点击出库

    dbchuchukusure1 = '/html/body/div[90]/div[2]/div/div/div/div/div[3]/button[2]'  # 点击确认

    '''调入退回申请'''

    doubledcf1 = 'xpath=>//*[contains(text(),"启用")]'

    def doubledcfe(self):
        self.doubleclick(self.doubledcf1)

    doubledcf2 = 'xpath=>//*[contains(text(),"启用")]'

    def doubledcf(self):
        self.doubleclick(self.doubledcf2)

    '''库存管理'''
    kcgl1 = '//*[@id="leftInner"]/ul/li[5]/div/div'  # 库存管理

    def kcgl(self):
        self.click(self.kcgl1)

    kccx1 = '//*[@id="leftInner"]/ul/li[5]/ul/li[1]/div'  # 库存查询

    def kccx(self):
        self.click(self.kccx1)

    kccxnmcx1 = '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/div[3]/input'  # 输入内码查询

    def kccxnmcx(self, text):
        self.type(self.kccxnmcx1, text)

    kccxcx1 = '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section/div[2]/div[1]/div/button[1]'  # 点击查询

    def kccxcx(self):
        self.click(self.kccxcx1)

    '''库存管理-采购入库'''
    cgru1 = 'xpath=//*[@id="leftInner"]/ul/li[5]/ul/li[2]/div'  # 点击采购入库菜单

    def cgru(self):
        self.click(self.cgru1)

    cgrkadd1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/section[1]/div/div/div[4]/button'  # 点击新增

    def cgrkadd(self):
        self.click(self.cgrkadd1)

    cgruxzcgdd1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div[1]/button[5]'  # 点击选择采购订单

    def cgruxzcgdd(self):
        self.click(self.cgruxzcgdd1)

    cgruxzjtcgdd1 = 'xpath=>/html/body/div[136]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[' \
                    '1]/td[1]/div/span'  # 选择入库的采购订单

    def cgruxzjtcgdd(self):
        self.click(self.cgruxzjtcgdd1)

    cgruxz1 = 'xpath=>/html/body/div[136]/div[2]/div/div/div[2]/div[1]/div[1]/div[7]/button'  # 点击选择按钮

    def cgruxz(self):
        self.click(self.cgruxz1)

    cgruru1 = 'xpath=>/*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div[1]/button[4]'  # 点击入库按钮

    def cgruru(self):
        self.click(self.cgruru1)

    '''紧俏品分配'''

    xtsz1 = 'xpath=>//*[@id="leftInner"]/ul/li[9]/div/div'  # 点击系统设置

    def xtsz(self):
        self.click(self.xtsz1)

    jcsj1 = 'xpath=>//*[@id="leftInner"]/ul/li[9]/ul/li[1]/div/div'  # 点击基础数据

    def jcsj(self):
        self.click(self.jcsj1)

    jqpfp1 = 'xpath=>//*[@id="leftInner"]/ul/li[9]/ul/li[1]/ul/li[5]/div'  # 点击紧俏品分配

    def jqpfp(self):
        self.click(self.jqpfp1)

    shurubm1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[1]/div/div/div[1]/div[1]/input'  # 输入编码

    def shurubm(self, text):
        self.type(self.shurubm1, text)

    jqpcx1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[1]/div/div/div[3]/button'  # 点击查询

    def jqpcx(self):
        self.click(self.jqpcx1)

    jqpdj1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[2]/div[1]/div/div[2]/div[2]/table/tbody/tr'  # 选择配件

    def jqpdj(self):
        self.click(self.jqpdj1)

    jqpfpNumc1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[2]/div[3]/div/div[2]/div[2]/table/tbody/tr/td[9]/div/span'  # 输入数量

    def jqpfpNumc(self):
        self.click(self.jqpfpNumc1)

    jqpfpNum1 = '//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[2]/div[3]/div/div[2]/div[2]/table/tbody/tr/td[9]/div/input'  # 输入数量

    def jqpfpNum(self, text):
        self.type(self.jqpfpNum1, text)

    jqpfpButton1 = 'xpath=>//*[@id="routes"]/div[2]/div[2]/div/div[2]/div/div/div/section[2]/div[3]/div/div[2]/div[2]/table/tbody/tr/td[2]/div/button[2]'  # 点击分配完成

    def jqpfpButton(self):
        self.click(self.jqpfpButton1)

    jqpsuren1 = '/html/body/div[12]/div[2]/div/div/div/div/div[3]/button[2]'  # 点击确定

    def jqpsuren(self):
        self.click(self.jqpsuren1)
