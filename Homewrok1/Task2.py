from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def locate_with_xpaths():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")

    x_paths = {}
    x_paths['Home'] = "//span[@class='sr-only']"
    x_paths['Contact'] = "//a[@data-target='#exampleModal']"
    x_paths['About us'] = "//a[@data-target='#videoModal']"
    x_paths['Cart'] = "//a[@id='cartur']"
    x_paths['Log in'] = "//a[@id='login2']"
    x_paths['Sign up'] = "//a[@id='signin2']"

    for key, value in x_paths.items():
        try:
            driver.find_element(By.XPATH, value)
            print(f'Element is located: {key}')
        except NoSuchElementException:
            print(f'No Such Element: {key}')

    driver.quit()
