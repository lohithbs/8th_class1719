from selenium import webdriver
driver=webdriver.Chrome()
driver.get('file:///G:/selinium/qwebtable.html')
driver.maximize_window()
driver.implicitly_wait(10)
ele=driver.find_elements_by_xpath('//*[@id="emp"]/thead/tr/th')
print(ele)
for i in ele:
    print(i.text)
