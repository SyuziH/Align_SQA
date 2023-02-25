from selenium import webdriver


def open_browsers():
    driver1 = webdriver.Firefox()
    driver1.get("https://www.demoblaze.com/")

    driver2 = webdriver.Edge()
    driver2.get('https://courses.letskodeit.com/practice')
