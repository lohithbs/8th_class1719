from selenium import webdriver
driver=webdriver.Chrome()
driver.get('file:///G:/selinium/qwebtable.html')
driver.maximize_window()
driver.implicitly_wait(10)
ele=driver.find_elements_by_xpath('//*[@id="emp"]/thead/tr/th[1]')
for i in range(len('td+1')):
    print(i)