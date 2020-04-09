from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")


@given('Open Gamestop page')
def open_gamestop(context):
    context.driver.get('https://www.gamestop.com/')

@when('Search for Sta')
def search_field_input(context):
    search = context.driver.find_element(By.CSS_SELECTOR, "input[name='q']")
    search.send_keys('Sta')
    sleep(3)

@then('Auto-suggestion appears')
def verify_auto_suggestion(context):
    auto_suggestion = context.driver.find_element(By.CSS_SELECTOR, "div.suggestions")
    assert auto_suggestion.is_displayed()
    sleep(3)

@when('Search for Star Wars')
def verify_auto_suggestion_content(context):
    search = context.driver.find_element(By.CSS_SELECTOR, "input[name='q']")
    search.send_keys('Sta')

@then('Results for Star Wars')
def search_product(context):
    search_field = context.driver.find_element(*SEARCH_INPUT)
    search_field.clear()
    search_field.send_keys('dress')
    context.driver.find_element(*SEARCH_ICON).click()