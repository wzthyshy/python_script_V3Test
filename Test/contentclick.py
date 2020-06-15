from time import sleep

from selenium .webdriver.common.action_chains import ActionChains
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://18h236a233.imwork.net:13257/FHMYSQL2/")

# driver.find_element_by_css_selector("#loginname").clear()
# driver.find_element_by_css_selector("#loginname").send_keys("汤直营")
#
# driver.find_element_by_css_selector("#password").clear()
# driver.find_element_by_css_selector("#password").send_keys("0")
driver.find_element_by_css_selector("#saveid").click()
# driver.add_cookies({"name":"username","value":"%E6%B1%A4%E7%9B%B4%E8%90%A5"})
# driver.add_cookie({"name":"password","value":"0"})
driver.add_cookie({"name":"JSESSIONID","value":"25C495C0BC1A0C5747A92ACFC9E3BCC8"})
sleep(5)
driver.refresh()





