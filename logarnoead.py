from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.colaboraread.com.br/login/auth")

login = driver.find_element_by_id("username")
login.clear()
login.send_keys("ead22604732")
#login.send_keys(Keys.RETURN) ---retorna as teclas inputadas

password = driver.find_element_by_id("password")
password.clear()
password.send_keys("shutdown")
#password.send_keys(Keys.RETURN) ---retorna as teclas inputadas


lembra=driver.find_element_by_id('remember_me')
lembra.click()

entra=driver.find_element_by_class_name('btn-primary')
entra.click()

span=driver.find_element_by_class_name('btn-default')
span.click()

curso=driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div[1]/div/div/div/div/div/div/div[1]/div/div[3]/form/div[2]/button')
curso.click()