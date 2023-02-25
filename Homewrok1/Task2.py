from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def locate_with_xpaths():
    driver = webdriver.Chrome()

    driver.get("https://www.demoblaze.com/")

    header1_xpath = "//a[@id='login2']"
    header2_xpath = "//a[@class='login4']"

    try:
        header1 = driver.find_element(By.XPATH, header1_xpath)
        print("Element is located: " + header1.text)
    except NoSuchElementException:
        print("No Such Element: " + header1_xpath)

    try:
        header2 = driver.find_element(By.XPATH, header2_xpath)
        print("Element is located: " + header2.text)
    except NoSuchElementException:
        print("No Such Element: " + header2_xpath)

    driver.quit()
