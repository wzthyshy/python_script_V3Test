from time import sleep, strftime

import sys
from selenium import webdriver
import unittest


# 定义类继承unittest
class WebTourTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://192.168.13.250:8008/FHMYSQL2")

    def testLogin(self):
        # 定位登陆页面信息并实例化
        uername = self.driver.find_element_by_id("loginname")
        pwd = self.driver.find_element_by_id("password")
        code = self.driver.find_element_by_id("code")
        submit = self.driver.find_element_by_id("to-recover")
        # 赋值
        uername.send_keys("汤直营")
        pwd.send_keys("0")
        code.send_keys("0000")
        submit.click()
        self.driver.implicitly_wait(20)
        # 获取登陆后的信息
        text = self.driver.find_element_by_id("user_info").text
        try:
            self.assertIn("汤直营", text)
        except AssertionError:
            # 设置时间戳
            nowtime = strftime("%Y_%m_%d_%H_%M_%S")
            # 设置断言信息；使用 sys.exc_info()获取断言信息
            # sys.exc_info()
            self.driver.get_screenshot_as_file("../Image/%s-%s.jpg" % nowtime, sys.exc_info()[1])
        # 点击退出
        self.driver.find_element_by_css_selector(".icon-caret-down").click()
        self.driver.find_element_by_css_selector(".icon-off").click()

    def tearDown(self):
        sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main
