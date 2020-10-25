# coding = utf-8
import HTMLTestReportCN
import os
import unittest
import time
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib

# =============发送邮件===================================


def sendReport(file_new, filename):
    f = open(new_report, 'rb')
    mail_body = f.read()
    msg = MIMEMultipart()
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = '13052085563@163.com'  # 发件地址
    msg['To'] = '641851519@qq.com'  # 收件人地址，多人以分号分隔
    text = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(text)
    time.sleep(2)
    att = MIMEApplication(open(filename, 'rb').read())
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(att)
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.set_debuglevel(1)
    smtp.login('13052085563@163.com', 'VYRVOQMUBPXOIYKL')  # 登录邮箱的账户和密码
    smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())
    smtp.quit()
    print('邮件发送成功')


# ====================查找测试报告目录，找到最新生成的测试报告文件========
def newReport(testReport):
    lists = os.listdir(testReport)  # 返回测试报告所在目录下的所有文件列表
    lists2 = sorted(lists)  # 获得按升序排序后的测试报告列表
    file_new = os.path.join(testReport, lists2[-1])  # 获取最后一个即最新的测试报告地址
    print(file_new)
    return file_new

def newReport1(testReport):
    lists = os.listdir(testReport)  # 返回测试报告所在目录下的所有文件列表
    lists2 = sorted(lists)  # 获得按升序排序后的测试报告列表
    filename = os.path.join(testReport, lists2[-1])  # 获取最后一个即最新的测试报告地址
    print(filename)
    return filename



if __name__ == '__main__':

    # 设置报告文件保存路径
    report_path  = os.path.dirname(os.path.abspath('.')) + '/test_report/'
    # 获取系统当前时间
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    # 设置报告名称格式
    HtmlFile = report_path + now + "HTMLtemplate.html"
    fp = open(HtmlFile, "wb")
    suite = unittest.TestLoader().discover("testsuits")
    # 执行用例

    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title="极配OMS回归测试报告", description="用例测试情况")
    runner.run(suite)
    fp.close()  # 这边曾错写成fp.close，导致发送邮件时正文怎么都发不出来

    new_report = newReport(report_path)  # 获取最新报告文件
    filename1 = newReport1(report_path)
    sendReport(new_report, filename1)  # 发送最新的测试报告