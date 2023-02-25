from selenium import webdriver
from selenium.webdriver.common.by import By


def max_price_item():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/")
    driver.implicitly_wait(12)
    elems = driver.find_elements(By.CSS_SELECTOR, 'div.card-block')

    info = []
    prices = []
    for elem in elems:
        info.append(elem.text.split('\n'))
        prices.append(elem.text.split('\n')[1])

    max_val = sorted(prices)[-1]

    for i in range(0, len(info)):
        if info[i][1] == max_val:
            print(info[i][0], max_val)
