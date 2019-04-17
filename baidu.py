# coding=utf-8
import selenium.webdriver.remote.webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import urllib2

driver=selenium.webdriver.remote.webdriver.WebDriver(command_executor="127.0.0.1:4444//wd/hub",desired_capabilities=DesiredCapabilities.CHROME)          #获取浏览器的对象（此处的driver可以定义为任意字符，只是个对象）
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium")
     #get方法发送网址
driver.find_element_by_id("su").click()
print(driver.title)
driver.quit()
