# coding=utf-8

import selenium.webdriver.remote.webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import unittest, time, re


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = selenium.webdriver.remote.webdriver.WebDriver(command_executor="http://127.0.0.1:5001/wd/hub",desired_capabilities=DesiredCapabilities.CHROME)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    # 百度搜索用例
    def test_baidu_search(self):
        '''百度搜索'''

        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    # 百度设置用例
    def test_baidu_set(self):
        '''百度设置'''
        driver = self.driver

        # 进入搜索设置页
        driver.get(self.base_url + "/gaoji/preferences.html")

        # 设置每页搜索结果为50 条
        m = driver.find_element_by_name("NR")  # 返回列表
        print(m)
        m.find_element_by_xpath("//option[@value='50']").click()
        time.sleep(2)

        # 保存设置的信息
        driver.find_element_by_xpath("//input[@value='保存设置']").click()

    #def tearDown(self):
        #self.driver.quit()
        #self.assertEqual([], self.verificationErrors)  # 断言错误列表是否为空


if __name__ == "__main__":
    unittest.main()