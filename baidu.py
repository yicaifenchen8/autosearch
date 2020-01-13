from selenium import webdriver
import time

def find(n):
    driver.implicitly_wait(20)
    return driver.find_element_by_xpath(n)

driver = webdriver.Chrome()
driver.maximize_window()  #浏览器全屏显示
driver.get("https://www.baidu.com/")

find('//*[@id="kw"]').send_keys('破冰行动')
find('//*[@id="su"]').click()
find('//*[@id="1"]/div[3]/h3/a').click()
find('//*[@id="block-BB"]/div/div[1]/div/h1/a[1]').click()
