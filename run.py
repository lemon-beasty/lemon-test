from commen import method
from  data import data
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
url = data.data.get("url")
username = data.data.get("username")
password = data.data.get("password")
key = data.data.get("key")

method.open_url(driver,url)
method.login_fun(driver,username,password)
method.serch_fun(driver,url,username,password,key)
