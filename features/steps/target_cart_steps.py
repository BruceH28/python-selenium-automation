from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("Click on Cart icon")
def click_car_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,'.sc-3d85a90e-1.fkOzcq').click()
    sleep(3)

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR,'.styles_ndsHeading__phw6r.styles_fontSize1__OL7f3').text
    expected_text = "Your cart is empty"
    assert actual_text ==  expected_text, f'Error, expected {expected_text} not in {actual_text}'

#