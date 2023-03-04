import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures('get_driver')
class TestActions:

    def test_checkbox_buttons(self):
        bmw_checkbox = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="bmwcheck"]')
        benz_checkbox = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="benzcheck"]')
        honda_checkbox = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="hondacheck"]')

        assert not bmw_checkbox.is_selected()
        assert not benz_checkbox.is_selected()
        assert not honda_checkbox.is_selected()

        bmw_checkbox.click()
        assert bmw_checkbox.is_selected()
        assert not benz_checkbox.is_selected()
        assert not honda_checkbox.is_selected()

        benz_checkbox.click()
        assert bmw_checkbox.is_selected()
        assert benz_checkbox.is_selected()
        assert not honda_checkbox.is_selected()

        honda_checkbox.click()
        assert honda_checkbox.is_selected()
        assert bmw_checkbox.is_selected()
        assert benz_checkbox.is_selected()

        bmw_checkbox.click()
        assert not bmw_checkbox.is_selected()
        assert benz_checkbox.is_selected()
        assert honda_checkbox.is_selected()

    def test_radio_buttons(self):
        bmw_radio = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="bmwradio"]')
        benz_radio = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="benzradio"]')
        honda_radio = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="hondaradio"]')

        assert not bmw_radio.is_selected()
        assert not benz_radio.is_selected()
        assert not honda_radio.is_selected()

        bmw_radio.click()
        assert bmw_radio.is_selected()
        assert not benz_radio.is_selected()
        assert not honda_radio.is_selected()

        benz_radio.click()
        assert not bmw_radio.is_selected()
        assert benz_radio.is_selected()
        assert not honda_radio.is_selected()

        honda_radio.click()
        assert honda_radio.is_selected()
        assert not bmw_radio.is_selected()
        assert not benz_radio.is_selected()

    def test_dropdown(self):
        cars = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'select[id="carselect"]')
        cars_select = Select(cars)

        cars_select.select_by_index(0)
        assert cars_select.first_selected_option.text == 'BMW'

        cars_select.select_by_index(1)
        assert cars_select.first_selected_option.text == 'Benz'

        cars_select.select_by_index(2)
        assert cars_select.first_selected_option.text == 'Honda'

    def test_disabled(self):
        disabled_text = "Disabled text"
        disabled_input = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[id="enabled-example-input"]')

        assert disabled_input.is_enabled()
        disabled_input.send_keys(disabled_text)

        disable_button = self.driver.find_element(By.CSS_SELECTOR, 'input[id="disabled-button"]')
        disable_button.click()

        assert not disabled_input.is_enabled()

        enable_button = self.driver.find_element(By.CSS_SELECTOR, 'input[id="enabled-button"]')
        enable_button.click()

        assert disabled_input.is_enabled()

        assert disabled_input.get_attribute('value') == disabled_text

    def test_alert(self):
        input_text_1 = 'Syuzi'
        input_text_2 = 'Anna'

        input_alert = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'input[placeholder="Enter Your Name"')
        input_alert.send_keys(input_text_1)
        self.driver.find_element(By.CSS_SELECTOR, 'input[id="alertbtn"]').click()
        alert_1 = self.driver.switch_to.alert

        assert alert_1.text == f'Hello {input_text_1}, share this practice page and share your knowledge'
        alert_1.accept()

        input_alert.send_keys(input_text_2)
        self.driver.find_element(By.CSS_SELECTOR, 'input[id="confirmbtn"]').click()

        alert_2 = self.driver.switch_to.alert

        assert alert_2.text == f'Hello {input_text_2}, Are you sure you want to confirm?'
        alert_2.dismiss()

    def test_hidden_show_elements(self):
        show_text = self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, 'input[value="Show"]')
        hide_text = self.driver.find_element(By.CSS_SELECTOR, 'input[id="hide-textbox"]')
        hidden_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="show-hide"]')

        text = "apple"
        assert hidden_input.is_displayed()

        hide_text.click()
        assert not hidden_input.is_displayed()

        show_text.click()
        assert hidden_input.is_displayed()

        hidden_input.click()
        hidden_input.send_keys(text)
        hide_text.click()
        show_text.click()
        assert hidden_input.get_attribute('value') == text

    def test_hover(self):
        hover = self.get_wait.wait_for_element(By.CSS_SELECTOR, 'button[id="mousehover"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", hover)

        actions = ActionChains(self.driver)
        actions.move_to_element(hover).perform()
