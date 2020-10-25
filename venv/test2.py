from selenium import webdriver
import time
import csv
import os

dr = webdriver.Chrome()
dr.maximize_window()
dr.get("https://tswms.g-parts.cn")
dr.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div/div/form/div[1]/div/div/input").send_keys('zhangwei')
dr.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div/div/form/div[2]/div/div/input").send_keys('123456')
dr.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div/div/form/div[4]/div/button").click()
time.sleep(2)
dr.find_element("//*[@id='leftInner']/ul/li[3]/div/div").click()
time.sleep(2)
dr.find_element("//*[@id='leftInner']/ul/li[3]/ul/li[3]/div/span[2]").click()
time.sleep(2)
dr.find_element("//*[@id='right-content']/div/section/div[1]/div/div[1]/div/div[1]/div/i").click()
time.sleep(1)





dr.implicitly_wait(10)

