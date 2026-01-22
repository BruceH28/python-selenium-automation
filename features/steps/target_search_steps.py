from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@when('Click VA HEALTH CONSENT button')
def click_consent(context):
    context.driver.find_element(By.ID,'VA_HEALTH_CONSENT_BUTTON').click()
    sleep(3)

@when('Search for beyblade x')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('beyblade x')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton' and @type='submit']").click()
    sleep(5)

@then('Verify search worked')
def verify_search_result(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    assert 'beyblade x' in actual_text, f'Error, expected "beyblade x" not in actual {actual_text}'
