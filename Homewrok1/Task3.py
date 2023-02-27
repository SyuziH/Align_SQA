from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def locate_with_css_selectors():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")

    categories = {}
    categories['Phones'] = "a[onclick=\"byCat('phone')\"]"
    categories['Laptops'] = "a[onclick=\"byCat('notebook')\"]"
    categories['Monitors'] = "a[onclick=\"byCat('monitor')\"]"

    for key, value in categories.items():
        try:
            driver.find_element(By.CSS_SELECTOR, value)
            print(f'Element is located: {key}')
        except NoSuchElementException:
            print(f'No Such Element: {key}')

    driver.quit()
