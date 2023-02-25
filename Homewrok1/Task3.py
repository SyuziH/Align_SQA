from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def locate_with_css_selectors():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")

    category1_slc = "a#itemc"
    category2_slc = "div.item"

    try:
        category1 = driver.find_element(By.CSS_SELECTOR, category1_slc)
        print("Element is located: " + category1.text)
    except NoSuchElementException:
        print("No such Element: " + category1_slc)

    try:
        category2 = driver.find_element(By.CSS_SELECTOR, category2_slc)
        print("Element is located: " + category2.text)
    except NoSuchElementException:
        print("No such Element: " + category2_slc)

    driver.quit()
