from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# selectors
AMAZON_LOGO = (By.XPATH, "//i[@aria-label='Amazon']")
EMAIL_FIELD = (By.ID, "ap_email")
CONTINUE_BUTTON = (By.ID, "continue")
NEED_HELP = (By.CSS_SELECTOR, "span.a-expander-prompt")
FORGOT_PASSWORD = (By.ID, "auth-fpp-link-bottom")
OTHER_ISSUES = (By.ID, "ap-other-signin-issues-link")
CREATE_ACCOUNT = (By.ID, "createAccountSubmit")
CONDITIONS = (By.XPATH, "//a[contains(@href, 'condition_of_use)]")
PRIVACY = (By.CSS_SELECTOR, "//a[contains(@href, 'privacy_notice)]")

LINK = "https://www.amazon.com/gp/help/customer/display.html"
INPUT_SEARCH = "input#helpsearch"
GO_BUTTON = "input.a-button-input[type='submit']"
VERIFY_TEXT = "div.cs-help-search-results div:first-child h2 a"


# init driver
driver = webdriver.Chrome()

# open url
driver.get(LINK)

# wait
sleep(3)

# input search data
search = driver.find_element(By.CSS_SELECTOR, INPUT_SEARCH)
search.send_keys('Cancel order')
go = driver.find_element(By.CSS_SELECTOR, GO_BUTTON)
go.click()

# wait
sleep(3)

# verification
assert 'Cancel Items or Orders' in driver.find_element(By.CSS_SELECTOR, VERIFY_TEXT).text
driver.quit()









