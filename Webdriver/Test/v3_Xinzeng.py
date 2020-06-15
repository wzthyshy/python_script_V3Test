from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep ,ctime
import os
import random
from datetime import date
from datetime import timedelta
#验证码

import datetime
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DC_PATH = BASE_DIR + "districtcode.txt"
# 随机生成客户姓名
def creatName():
    firstnamelist=["A","B","C","D","E","F","G","H","I","J","K","L","M","N",]
    firstname =random.choice(firstnamelist)
    lastname=random.randint(000,1000)
    return firstname+str(lastname)




# 随机生成手机号码
def createPhone():
    prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
    return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))
# 随机生成身份证号
def getdistrictcode():
    with open("D:\Python35\Python_Script\districtcode.txt") as file:
        data = file.read()
        districtlist = data.split('\n')
    for node in districtlist:
  #print node
        if node[10:11] != ' ':
            state = node[10:].strip()
        if node[10:11]==' 'and node[12:13]!=' ':
            city = node[12:].strip()
        if node[10:11] == ' 'and node[12:13]==' ':
            district = node[14:].strip()
            code = node[0:6]
            codelist.append({"state":state,"city":city,"district":district,"code":code})
def gennerator():
    global codelist
    codelist = []
    if not codelist:
        getdistrictcode()
    id = codelist[random.randint(0,len(codelist))]['code'] #地区项
    id = id + str(random.randint(1930,2013)) #年份项
    da  = date.today()+timedelta(days=random.randint(1,366)) #月份和日期项
    id = id + da.strftime('%m%d')
    id = id+ str(random.randint(100,300))#，顺序号简单处理

    i = 0
    i=i+1
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] #权重项
    checkcode ={'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'5','9':'3','10':'2'} #校验码映射
    for i in range(0,len(id)):

       count = count +int(id[i])*weight[i]

    id = id + checkcode[str(count%11)] #算出校验码
    return id
print(gennerator())
print(createPhone())
print(creatName())

driver=webdriver.Firefox()
driver.get("http://192.168.13.250:8008/FHMYSQL2/ ")
driver.maximize_window()
#输入登录密码
driver.find_element_by_id("loginname").send_keys("汤直营")
driver.find_element_by_id("password").send_keys("0")
driver.find_element_by_id("code").send_keys("0000")
#点击登录
driver.find_element_by_id("to-recover").click()
sleep(10)
#
driver.find_element_by_xpath(".//*[@id='main-container']/div[1]/ul/li[4]/a").click()
sleep(3)
driver.switch_to.frame("mainFrame")
driver.switch_to.frame("page_z005")
driver.find_element_by_link_text("征信申请表").click()
sleep(3)
# 进入征信页面
driver.switch_to.default_content()
driver.switch_to.frame("mainFrame")
driver.switch_to.frame("page_a14244")
driver.find_element_by_xpath("html/body/div[2]/div[3]/input").send_keys(creatName())
driver.find_element_by_xpath("html/body/div[2]/div[5]/input").send_keys(gennerator())
driver.find_element_by_xpath("html/body/div[2]/div[20]/input").send_keys(createPhone())
driver.implicitly_wait(5)
try:
    print(ctime())
     # 选择主贷人
    driver.find_element_by_xpath("html/body/div[2]/div[13]/span[1]/img").click()
except NoSuchElementException as msg:
	print(msg)
finally:
	print(ctime())

sleep(3)

driver.switch_to.default_content()
driver.switch_to.frame("_DialogFrame_0")
driver.implicitly_wait(5)
try:
    driver.find_element_by_css_selector("[data-name='主贷人']")
    element = driver.find_element_by_css_selector("[data-name='主贷人']")

except NoSuchElementException as msg:
	print(msg)
# finally:
# 	print(ctime())
# driver.find_element_by_css_selector("[data-name='主贷人']")
# element=driver.find_element_by_css_selector("[data-name='主贷人']")
sleep(3)
ActionChains(driver).double_click(element).perform()
sleep(5)
#进入征信页面
driver.switch_to.default_content()
driver.switch_to.frame("mainFrame")
driver.switch_to.frame("page_a14244")
#选择贷款银行
driver.find_element_by_xpath("html/body/div[2]/div[6]/span[1]/img").click()
driver.switch_to.default_content()
driver.switch_to.frame("_DialogFrame_0")
driver.find_element_by_xpath(".//*[@id='tb1']/tbody/tr[1]/td[1]")
element=driver.find_element_by_xpath(".//*[@id='tb1']/tbody/tr[1]/td[1]")
sleep(3)
ActionChains(driver).double_click(element).perform()
sleep(5)
#进入征信页面zz
driver.switch_to.default_content()
driver.switch_to.frame("mainFrame")
driver.switch_to.frame("page_a14244")
#选择业务员
driver.find_element_by_xpath("html/body/div[2]/div[7]/span[1]/img").click()
driver.switch_to.default_content()
driver.switch_to.frame("_DialogFrame_0")
driver.find_element_by_xpath(".//*[@id='tb1']/tbody/tr[1]/td[1]")
element=driver.find_element_by_xpath(".//*[@id='tb1']/tbody/tr[1]/td[1]")
sleep(3)
ActionChains(driver).double_click(element).perform()
sleep(5)
#进入征信页面
driver.switch_to.default_content()
driver.switch_to.frame("mainFrame")
driver.switch_to.frame("page_a14244")
#选择业务区域
driver.find_element_by_xpath("html/body/div[2]/div[19]/span[1]/img").click()
driver.switch_to.default_content()
driver.switch_to.frame("_DialogFrame_0")
driver.find_element_by_xpath(".//*[@id='tb1']/tbody/tr[1]/td[1]")
element=driver.find_element_by_xpath(".//*[@id='tb1']/tbody/tr[1]/td[1]")
sleep(3)
ActionChains(driver).double_click(element).perform()
sleep(5)
#进入征信页面
driver.switch_to.default_content()
driver.switch_to.frame("mainFrame")
driver.switch_to.frame("page_a14244")
#选择客户风险
driver.find_element_by_xpath("html/body/div[2]/div[31]/span[1]/img").click()
driver.switch_to.default_content()
driver.switch_to.frame("_DialogFrame_0")
driver.find_element_by_xpath(".//*[@id='tb1']/tbody/tr[1]/td[1]")
element=driver.find_element_by_xpath(".//*[@id='tb1']/tbody/tr[1]/td[1]")
sleep(3)
ActionChains(driver).double_click(element).perform()
sleep(5)
#进入征信页面
driver.switch_to.default_content()
driver.switch_to.frame("mainFrame")
driver.switch_to.frame("page_a14244")
#选择合作车商
driver.find_element_by_xpath("html/body/div[2]/div[10]/span[1]/img").click()
driver.switch_to.default_content()
driver.switch_to.frame("_DialogFrame_0")
driver.find_element_by_xpath(".//*[@id='tb1']/tbody/tr[1]")
element=driver.find_element_by_xpath(".//*[@id='tb1']/tbody/tr[1]")
sleep(3)
ActionChains(driver).double_click(element).perform()
sleep(5)
#进入征信页面
driver.switch_to.default_content()
driver.switch_to.frame("mainFrame")
driver.switch_to.frame("page_a14244")
#点击保存
driver.implicitly_wait(5)

driver.find_element_by_link_text("保存").click()
element = driver.find_element_by_link_text("保存").click()


al = driver.switch_to.alert
al.accept()

# #点击提交
# driver.implicitly_wait(5)
#
# driver.find_element_by_link_text("提交").click()
# element = driver.find_element_by_link_text("提交").click()
#
#
# al = driver.switch_to.alert
# al.accept()




