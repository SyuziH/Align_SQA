from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()


def explicitly_wait():
    """tells Selenium WebDriver to wait for a certain condition to be met before proceeding with the script. Unlike
    implicit waits, explicit waits are applied to specific elements of the webpage and can have custom conditions.
    As an argument you need to pass:

    driver -> instance of driver
    timeout -> how many seconds do wait
    poll_frequency -> sleep interval between calls : default 0.5
    ignored_exceptions -> exception classes ignored during calls : default NoSuchElementException


    """
    wait = WebDriverWait(driver, timeout=10, poll_frequency=0.3)

    # Wait for element to be clickable
    wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "selector")))

    # Wait for element to be visible
    wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "selector")))

    # Wait for element to be present
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "selector")))

