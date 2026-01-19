from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By





# init driver

driver = webdriver.Chrome()
driver.maximize_window()


# open the url
driver.get('https://www.amazon.com/')

sleep(3)
# locators
driver.find_element(By.ID,'twotabsearchtextbox')

#By XPATH
driver.find_element(By.XPATH,"//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@role='searchbox']")

#By XPATH, any tag
driver.find_element(By.XPATH,"//*[@placeholder='Search Amazon']")

#By XPATH, combination of attributes
driver.find_element(By.XPATH, "//a[@aria-label='Amazon' and @lang='en']")
#By XPATH, combo any tag
driver.find_element(By.XPATH, "//*[@aria-label='Amazon' and @lang='en']")

#By XPATH, text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
#By XPATH, text combo
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

#By XPATH, partial match
driver.find_element(By.XPATH, "//a[contains(@href, @ref_='nav_cs_bestsellers')]")

#By XPATH, parent => child nodes
driver.find_element(By.XPATH, "//div[@id='navbar']//a[text()='Best Sellers']")
