from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.com/")


#By ID
driver.find_element(By.ID,"twotabsearchtextbox")
#By CSS by, ID
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
#By CSS by,tag + ID
driver.find_element(By.CSS_SELECTOR,"input#twotabsearchtextbox")
#By CSS by, class
driver.find_element(By.CSS_SELECTOR,".nav-a.nav-a-2.icp-link-style-2")
driver.find_element(By.CSS_SELECTOR,".nav-a-2.icp-link-style-2")
driver.find_element(By.CSS_SELECTOR,".nav-a-2")
#By CSS by, tag + class
driver.find_element(By.CSS_SELECTOR,"span.nav-cart-icon.nav-sprite")
#By CSS by, tag + ID + class
driver.find_element(By.CSS_SELECTOR,"a#nav-logo-sprites.nav-logo-link")
#By CSS by, attribute
driver.find_element(By.CSS_SELECTOR,"[class='a-icon a-icon-next-rounded']")
driver.find_element(By.CSS_SELECTOR,"[name='field-keywords'][aria-label='Search Amazon']")
#By CSS by, tag + ID + class + attribute
driver.find_element(By.CSS_SELECTOR,"a#nav-logo-sprites.nav-logo-link[lang='en'][aria-label='Amazon']")

driver.find_element(By.CSS_SELECTOR,"[href*='ap_signin_notification_condition_of_use']")