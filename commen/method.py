# # 打开浏览器函数
# import time
# def open_url(driver,url):
#     from selenium import webdriver
#     import time
#     driver.get(url)         #打开网站
#     driver.implicitly_wait(10)
#     driver.maximize_window()
# # 登录函数
# def login_fun(driver,username,password):
#
#     driver.find_element_by_id("username").send_keys(username)
#     driver.find_element_by_id("password").send_keys(password)
#     driver.find_element_by_xpath('//input[@id="rememberUserCode"]/following-sibling::ins').click()
#     driver.find_element_by_id("btnSubmit").click()
#
# # 搜索函数
# def serch_fun(driver,url,username,password,key):
#     from selenium import webdriver
#     import time
#     # open_url(driver,url)
#     # login_fun(driver,username,password)
#     driver.find_element_by_xpath('//span[text()="日间管理"]').click()
#     time.sleep(2)
#     driver.find_element_by_id("filter").send_keys(key)
#     driver.find_element_by_id("filter")
#
#
#
# def serch_fun(driver,url,username,password,key):
#     # open_url(driver,url)
#     # login_fun(driver,username,password)
#     driver.find_element_by_xpath('//span[text()="零售出库"]').click()
#     time.sleep(2)
#     id_li = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")
#     id_frame = id_li+"-frame"
#     driver.switch_to.frame(id_frame)
#     time.sleep(2)
#     driver.find_element_by_id("searchNumber").send_keys(key)
#     driver.find_element_by_xpath('//span[text()="查询"]').click()
#     time.sleep(1)
#     num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]//div').text


import time
from selenium import webdriver
def open_url(driver,url):
    from selenium import webdriver
    import time
    driver.get(url)         #打开网站
    driver.implicitly_wait(10)
    driver.maximize_window()
# # 登录函数
def login_fun(driver,username):
    driver.find_element_by_id("username").send_keys(username)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="submit"]').click()

# # 搜索函数
def serch_fun(driver,key):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    # open_url(driver,key)
    # login_fun(driver,username)
    driver.find_element_by_xpath('//span[text()="日间管理"]').click()
    # driver.find_element_by_xpath('//*[@id="filter"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//input[@id="filter"]').send_keys(key)
    driver.find_element_by_xpath('//input[@id="filter"]').send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="patientlist_table"]/tbody/tr/td[15]/a').click()
    id = driver.find_element_by_xpath('//*[@id="patient_detail"]/div[1]/div[1]/font[1]').text()
    return id
url = "http://172.17.0.128:8198/"
driver = webdriver.Chrome()
open_url(driver,url)
username="00"
key = "270"
num_id = "1217"
login_fun(driver,username="00")
id = serch_fun(driver,key)
if id == num_id:
    print("这个患者ID为{}".format(id))
else:
    print("这条用例不通过")