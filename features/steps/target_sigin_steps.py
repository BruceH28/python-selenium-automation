from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from target_search_script import expected_text


@when("Click on Account icon")
def click_sign_in(context):
    context.driver.find_element(By.ID,'account-sign-in').click()
    sleep(3)

@when("Click on Sign in button")
def click_sign_in_button(context):
    context.driver.find_element(By.CSS_SELECTOR,'[data-test="accountNav-signIn"]').click()
    sleep(3)


@then("Verify 'Sign in or create account' is shown")
def verify_sign_in_or_create_account(context):
    actual_text = context.driver.find_element(By.XPATH, '//h1[contains(text(),"Sign in or create account")]').text
    expected_text = 'Sign in or create account'
    assert actual_text == expected_text, f'Error, expected {expected_text} not in {actual_text}'

