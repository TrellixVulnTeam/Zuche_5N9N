from time import sleep


def pickup():
    # 选择时间
    driver.find_element_by_name("hCityId").send_keys("LAX")

    sleep(2)
    driver.find_element_by_class_name("airport").click()
    # driver.find_element_by_name("hRCityId").send_keys("LAX")
    # driver.find_element_by_css_selector("/html/body/div[9]/div/div[2]/a").click()
    driver.find_element_by_class_name("searchBtn").click()
    sleep(10)
