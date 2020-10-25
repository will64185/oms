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
dr.find_element_by_xpath("//*[@id='leftInner']/ul/li[3]/div/i").click()
time.sleep(2)
dr.find_element_by_xpath("//*[@id='leftInner']/ul/li[3]/ul/li[4]/div/span[2]").click()
time.sleep(2)
dr.find_element_by_xpath("//*[@id='right-content']/div/section[1]/div/div/div[4]/div[1]/div[1]/div/i").click()
time.sleep(2)
dr.find_element_by_xpath("//*[@id='right-content']/div/section[1]/div/div/div[4]/div[1]/div[2]/ul[2]/li[2]").click()
time.sleep(2)
dr.find_element_by_xpath("//*[@id='right-content']/div/section[1]/div/div/div[4]/div[2]/input").send_keys("PKDD-20190212610000000003")
time.sleep(2)
dr.find_element_by_xpath("//*[@id='right-content']/div/section[1]/div/div/div[4]/button[1]").click()
time.sleep(2)
dr.find_element_by_xpath("//*[@id='right-content']/div/section[2]/div/div/div[2]/table/tbody/tr/td[1]/div/div/i").click()
time.sleep(2)
a = dr.find_element_by_xpath("//*[@id='right-content']/div/section[2]/div/div/div[2]/table/tbody/tr[2]/td/div/div/div/div[2]/table/tbody/tr/td/div/span").text
print(a)