from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#Init driver/ Arrange
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

#Open the url
driver.get('https://stackoverflow.com/users/signup')
sleep(10)


#Create your account
driver.find_element(By.XPATH,'//h1[text()="Create your account"]')
sleep(2)

#terms of service
driver.find_element(By.CSS_SELECTOR,'[name="tos"]')
sleep(2)

#Privacy policy
driver.find_element(By.CSS_SELECTOR,'[name="privacy"]')
sleep(2)

#Email text field
driver.find_element(By.CSS_SELECTOR,'#email')
sleep(2)

#Show/hide password
driver.find_element(By.CSS_SELECTOR,'.js-show-password[aria-hidden="true"]')
sleep(2)

#Password text field
driver.find_element(By.CSS_SELECTOR,'#password')
sleep(2)

#Sign up button
driver.find_element(By.CSS_SELECTOR,'#submit-button')
sleep(2)

#Sign up with google
driver.find_element(By.CSS_SELECTOR,'div#openid-buttons > button[data-provider="google"]')
sleep(2)

#Sign up with github
driver.find_element(By.CSS_SELECTOR,'div#openid-buttons > button[data-provider="github"]')
sleep(2)

driver.quit()