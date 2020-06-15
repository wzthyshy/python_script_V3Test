from selenium import webdriver
from time import  sleep

class Login():
    def user_login(self,driver):
        driver.find_element_by_id("loginname").clear()
        driver.find_element_by_id("loginname").send_keys("汤直营")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("0")
        driver.find_element_by_id("code").clear()
        driver.find_element_by_id("code").send_keys("0000")



