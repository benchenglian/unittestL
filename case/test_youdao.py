# coding=utf-8
import selenium.webdriver.remote.webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import unittest, time, re


class Youdao(unittest.TestCase):
    def setUp(self):
        self.driver = selenium.webdriver.remote.webdriver.WebDriver(command_executor="http://10.3.246.74:5001/wd/hub",
                                                                    desired_capabilities=DesiredCapabilities.CHROME)
        self.base_url = "http://fanyi.youdao.com/?keyfrom=dict2.top"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_youdao_search(self):
        '''有道搜索'''
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element_by_id("inputOriginal").send_keys("selenium")
        driver.find_element_by_id("transMachine").click()
        time.sleep(2)

    #def tearDown(self):
        #self.driver.quit()
        #self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()