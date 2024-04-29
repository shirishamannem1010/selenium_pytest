
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class Selenium_Actions:
    def __init__(self, driver):
        self.driver = driver

    def webelement_click(self, locator):
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(locator)).click()

    def webelement_send_keys(self, locator, text):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator)).send_keys(text)

    def webelement_get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

    def webelement_input(self, locator, text):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locator)).send_keys(text)
    
    def webelement_select_dropdown(self, locator, text):
        select = Select(WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator)))
        select.select_by_visible_text(text)

    def webelement_displayed(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).is_displayed()
    def webelement_scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def webelement_cleartext(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()
    def webelement_get_attribute(self, locator, attribute):
        return WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locator)).get_attribute(attribute)
    def webelement_is_empty(self, locator):
        return WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locator)).is_empty()
    def webelement_is_isenabled(self, locator):
        return WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locator)).is_enabled()
