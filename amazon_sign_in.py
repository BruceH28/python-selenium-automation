from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#Init driver/ Arrange
driver = webdriver.Chrome()
driver.maximize_window()

#Open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F%26tag%3Damazusnavi-20%26ref%3Dnav_signin%26adgrpid%3D185319704606%26hvpone%3D%26hvptwo%3D%26hvadid%3D779770532387%26hvpos%3D%26hvnetw%3Dg%26hvrand%3D5730689460791936674%26hvqmt%3De%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9015231%26hvtargid%3Dkwd-360364908397%26hydadcr%3D28884_14649101_1546077%26mcid%3Dadfdaf019ea13ff5af2dd6b5b801add6%26hvocijid%3D5730689460791936674--%26hvexpln%3D0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

#Act
#Amazon logo
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
sleep(3)
#Email field
driver.find_element(By.ID,"ap_email_login")
sleep(3)
#Continue button
driver.find_element(By.XPATH,'//input[@class="a-button-input"]')
#Conditions of use link
driver.find_element(By.XPATH,'//a[contains(@href,"_condition_of_use"]')
#Privacy Notice link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
#Need help link
driver.find_element(By.XPATH, "//a[@class='a-size-base a-link-normal']")
#Forgot your password link isn't present on page as suggested requires further navigation
driver.get("https://www.amazon.com/gp/help/customer/account-issues/ref=unified_claim_collection?ie=UTF8")
driver.find_element(By.ID, "cu-select-firstNode").click()
driver.find_element(By.XPATH, '//option[@value="2"]')
#Other issues with Sign-In link isn't present on page as suggested requires further navigation
driver.get("https://www.amazon.com/gp/help/customer/account-issues/ref=unified_claim_collection?ie=UTF8")
driver.find_element(By.ID, "cu-select-firstNode")
#Create your Amazon account button no longer has seperate field new users must enter email and submit
driver.find_element(By.ID, 'ap_email_login').submit()

#Assert

driver.quit()