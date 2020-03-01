from selenium import webdriver
from selenium.webdriver.common.by import By
from sel import *
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

search = driver.find_element(By.NAME, sel1)
search.send_keys('Dress')
search.send_keys(Keys.RETURN)

assert 'Dress' in driver.find_element(By.XPATH, "//div[contains(@class, 'commercial-unit-desktop-top' )]//h3").text
assert 'Dress' in driver.find_element(By.XPATH, "//div[@class='g']").text


driver.quit()