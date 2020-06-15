from selenium import webdriver
import config
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome()
driver.get(config.website_url)
wait = WebDriverWait(
    driver, 9, ignored_exceptions=StaleElementReferenceException)
# time.sleep(5)

try:
    WebDriverWait(driver, 9).until(
        EC.presence_of_element_located((By.XPATH, config.email_input)))
except TimeoutException:
    print("Loading took too much time!!!!")
    exit()


driver.find_element_by_xpath(config.email_input).send_keys(config.email)
driver.find_element_by_xpath(config.submit_button).click()

wait.until(EC.presence_of_element_located((By.XPATH, config.submit_button)))
driver.find_element_by_xpath(config.password_input).send_keys(config.password)
wait.until(EC.presence_of_element_located((By.XPATH, config.submit_button)))
time.sleep(2)
driver.find_element_by_xpath(config.submit_button).click()

time.sleep(5)
