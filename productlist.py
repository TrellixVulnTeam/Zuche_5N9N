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