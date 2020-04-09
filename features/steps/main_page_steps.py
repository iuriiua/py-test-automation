from selenium.webdriver.common.by import By
from behave import given, when, then

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when('Click Amazon Orders link')
def click_orders_link(context):
    context.driver.find_element(*ORDERS_LINK).click()

@when('Search for {product}')
def search_product(context, product):
    search_field = context.driver.find_element(*SEARCH_INPUT)
    search_field.clear()
    search_field.send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()
