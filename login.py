from selenium import webdriver
from time import sleep

def login()
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://accounts.ctrip.com/member/login.aspx?BackUrl=http%3A%2F%2Fcar.ctrip.com%2F&responsemethod=get")
    driver.maximize_window()
    sleep(10)

    # login
    driver.find_element_by_name("txtUserName").send_keys("17621380822")
    driver.find_element_by_name("txtPwd").send_keys("Legend.1234")
    driver.find_element_by_name("btnSubmit").click()
    sleep(10)
