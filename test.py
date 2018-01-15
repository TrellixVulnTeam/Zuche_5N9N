#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from selenium import webdriver
from time import sleep


def test():
    '''
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("http://car.ctrip.com/")
    driver.maximize_window()
    sleep(10)

    # login
    driver.find_element_by_class_name("cui_links_login").click()
    driver.find_element_by_name("txtUserName").send_keys("17621380822")
    driver.find_element_by_name("txtPwd").send_keys("Legend.1234")
    driver.find_element_by_name("btnSubmit").click()
    sleep(2)
'''
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://accounts.ctrip.com/member/login.aspx?BackUrl=http%3A%2F%2Fcar.ctrip.com%2F&responsemethod=get")
    driver.maximize_window()
    sleep(10)

    # login
    driver.find_element_by_name("txtUserName").send_keys("17621380822")
    driver.find_element_by_name("txtPwd").send_keys("Legend.1234")
    driver.find_element_by_name("btnSubmit").click()
    sleep(10)




    # 选择时间
    driver.find_element_by_name("hCityId").send_keys("LAX")

    sleep(2)
    driver.find_element_by_class_name("airport").click()
    # driver.find_element_by_name("hRCityId").send_keys("LAX")
    # driver.find_element_by_css_selector("/html/body/div[9]/div/div[2]/a").click()
    driver.find_element_by_class_name("searchBtn").click()
    sleep(10)

    # 当前句柄转到新页面
    driver.switch_to_window(driver.window_handles[1])

    # 循环获取供应
    vendors = driver.find_elements_by_class_name("supplier_item")

    for vendor in vendors:
        if vendor.text == "Sixt":
            vendor.click()
            break
    sleep(5)

    # 选择车型
    vehicles = driver.find_elements_by_xpath('//*[@id="productlist_filter"]/div/ul[1]/li/div[2]/p[1]/span[1]')
    details = driver.find_elements_by_xpath('//*[@id="productlist_filter"]/div/ul[2]/li/div/div[2]/div[3]')
    count = 0
    for vehicle in vehicles:
        if vehicle.text == "丰田 Yaris":
            details[count].click()
            sleep(2)
            break
        count += 1
    sleep(2)



    # 模拟点击“查看详细”按钮
    driver.find_element_by_css_selector("#productlist_filter .j_detail_spe").click()
    sleep(5)
    '''
    '''
    # 选择现付
    pays = driver.find_elements_by_xpath('//*[@id="j_mainview"]/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div[2]'
                                         '/ul/li')
    for pay in pays:
        if pay.text == "门店付全额":
            print(pay.text)
            pay.click()
            sleep(2)
            break
    sleep(2)

    driver.switch_to_window(driver.window_handles[2])  # 当前句柄转到新页面
    driver.find_element_by_css_selector("#j_mainview .btn").click()  # 模拟点击“下一步，填写订单”按钮
    sleep(1)

    # 填写表单
    driver.find_element_by_css_selector("#lastName").clear()
    driver.find_element_by_css_selector("#lastName").send_keys("ctrip")
    driver.find_element_by_css_selector("#firstName").clear()
    driver.find_element_by_css_selector("#firstName").send_keys("test")
    driver.find_element_by_css_selector("#mobile").clear()
    driver.find_element_by_css_selector("#mobile").send_keys("17621380822")
    driver.find_element_by_css_selector("#email").clear()
    driver.find_element_by_css_selector("#email").send_keys("jt_sun@Ctrip.com")

    driver.find_element_by_name("age").click()
    sleep(2)
    ages = driver.find_elements_by_css_selector(".ui-dropdown-item")

    for age in ages:
        if age.text == "25-65 周岁":
            age.click()
            break
    sleep(5)

    payment = driver.find_element_by_id("submit-order")
    driver.execute_script("arguments[0].scrollIntoView();", payment)

    sleep(5)
    payment.click()

test()
