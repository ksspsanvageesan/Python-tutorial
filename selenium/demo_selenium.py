from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
#driver.back()
#driver.forward()
#driver.refresh()


#find element by id
element = driver.find_element(By.ID, "content")
element = driver.find_element(By.XPATH,"//*[@id='content']/ul/li[1]/a")