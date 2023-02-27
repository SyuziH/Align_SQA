from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumPython.wait.wait import Wait

driver = webdriver.Chrome()


class Tests:

    def test_correctly_load(self):
        global driver
        driver.get("https://www.demoblaze.com/")

        get_wait = Wait(driver)
        phones_button = get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "a[onclick=\"byCat('phone')\"]")
        phones_button.click()
        phones_list = driver.find_elements(By.CSS_SELECTOR, "div.row")
        assert len(phones_list) != 0, "Phones page is empty"

        laptop_button = get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "a[onclick=\"byCat('notebook')\"]")
        laptop_button.click()
        laptop_list = driver.find_elements(By.CSS_SELECTOR, "div.col-lg-9")
        assert len(laptop_list) != 0, "Laptop page is empty"

        monitor_button = get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, "a[onclick=\"byCat('monitor')\"]")
        monitor_button.click()
        monitor_list = driver.find_elements(By.CSS_SELECTOR, "div#tbodyid")
        assert len(monitor_list) != 0, "Monitor page is empty"
