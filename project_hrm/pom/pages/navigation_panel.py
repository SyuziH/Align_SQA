from selenium.webdriver.common.by import By
from seleniumPython.Align_SQA.project_hrm.pom.base.base_page import BasePage


class NavigationPanel(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    ROOT_ELEMENT = (By.CSS_SELECTOR, 'nav[aria-label="Sidepanel"]')
    NAVIGATION_ITEMS = (By.CSS_SELECTOR, 'ul[class=oxd-main-menu] > li')
    PAGE_IS_VISIBLE_RECRUITMENT = (By.CSS_SELECTOR, 'li[class = "oxd-topbar-body-nav-tab --visited"]')



    def get_navigation_items(self):
        self.get_wait().wait_for_page()
        navigation_elements = self.get_wait().wait_for_list_size_change(self.NAVIGATION_ITEMS, size=11)
        navigation_item_names = ['Admin', 'PIM', 'LEAVE', 'TIME', 'Recruitment', 'My_Info', 'Performance', 'Dashboard',
                                 'Directory', 'Maintenance', 'Buzz']
        return dict(zip(navigation_item_names, navigation_elements))

    def go_to(self, page):
        element = self.get_navigation_items().get(page)
        self.get_wait().wait_for_element_to_be_clickable(element)
        self.click(element)


    def find_navigated_page(self, locator):
        return self.get_wait().wait_for_element(locator)