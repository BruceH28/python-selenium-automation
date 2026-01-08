from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#Init driver/ Arrange
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

#Open the url
driver.get('https://www.target.com/')

#Act
driver.find_element(By.ID,'VA_HEALTH_CONSENT_BUTTON').click()
driver.find_element(By.ID,'search').send_keys('beyblade x')
driver.find_element(By.XPATH,"//button[@data-test='@web/Search/SearchButton' and @type='submit']").click()
sleep(5)

#verification/ Assert
expected_text = "beyblade x"
actual_text = driver.find_element(By.XPATH,"//div[@data-test='lp-resultsCount']").text

assert expected_text in actual_text, f'Error, expected {expected_text} not in {actual_text}'

print("Test case passed")
driver.quit()

