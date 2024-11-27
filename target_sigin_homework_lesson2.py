from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.target.com/')
sleep(3)
driver.find_element(By.ID,"account-sign-in").click()
sleep(3)
driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()
sleep(3)
driver.find_element(By.XPATH,"//span[contains(text(), 'Sign into your Target account')]")

#verfiy
driver.find_element(By.ID,'login')

print("Test Passed")