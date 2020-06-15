from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import Keys
import unittest
import HTMLTestRunner
class WebTourTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://192.168.13.250:8008/FHMYSQL2")
    def testLogin(self):
        uername=self.driver.find_element_by_id("loginname")
        pwd=self.driver.find_element_by_id("password")
        code=self.driver.find_element_by_id("code")
        submit=self.driver.find_element_by_id("to-recover")
        uername.send_keys("汤直营")
        pwd.send_keys("0")
        code.send_keys("0000")
        submit.click()
        time.sleep(5)
    def tearDown(self):
        self.driver.quit()
def fp():
    test=unittest.TestCase()
    test.addTest(WebTourTest('testLogin'))
    file_result=open('C:\\test.html','wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=file_result,title=u'WebTour测试报告',description=u'用例执行情况')
    runner.run(test)
    file_result.close()
if __name__ == '__main__':
    fp()



