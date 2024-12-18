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

# find element . by ID
driver.find_element(By.ID,"twotabsearchtextbox")
driver.find_element(By.ID,"nav-search-submit-button")

# Find element, by XPATH
driver.find_element(By.XPATH,"//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH,"//input[@role='searchbox']")

# Homework elements
driver.find_element(By.XPATH,"//i[@role='img']")
driver.find_element(By.XPATH,"//input[@type='email']")
driver.find_element(By.ID,"continue")
driver.find_element(By.XPATH,
driver.find_element(By.XPATH,
driver.find_element(By.XPATH,
driver.find_element(By.XPATH,
driver.find_element(By.XPATH,
driver.find_element(By.XPATH,
driver.find_element(By.XPATH,