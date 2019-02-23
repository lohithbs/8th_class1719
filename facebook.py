from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(10)
element=driver.find_elements_by_xpath("//input[@type='email' or @type='password' or @name='firstname' or @name='lastname']")
for data in element:
    data.send_keys('qspiders')
pass
