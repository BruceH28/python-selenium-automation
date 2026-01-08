from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#Init driver/ Arrange
driver = webdriver.Chrome()
driver.maximize_window()


#Open the url
driver.get('https://www.target.com/')
sleep(3)

#Allows page to be clickable in chrome with consent warning present as an overlay
driver.find_element(By.ID,'VA_HEALTH_CONSENT_BUTTON').click()
sleep(3)
driver.find_element(By.ID,'account-sign-in').click()
sleep(3)
driver.find_element(By.XPATH,'//button[@data-test="accountNav-signIn"]').click()
sleep(3)
driver.find_element(By.XPATH, '//h1[contains(text(),"create account")]')
sleep(3)
driver.find_element(By.ID,'login')

driver.quit()