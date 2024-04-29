from selenium.webdriver.common.by import By
from actions.selenium_actions import Selenium_Actions

class LeavePage(Selenium_Actions):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    _leave_menu = (By.XPATH, "//span[text()='Leave']")
    
    from_date=(By.XPATH,"(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")
    select_date30=(By.XPATH,"(//div[@class='oxd-calendar-date'])[30]")
    # Interactions
    def navigate_to_leave(self):
        self.webelement_click(self._leave_menu)
    
    def select_date_from_calendar(self):
        calendar_icon = self.driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")
        print("---------------calendar_icon----------------")
        calendar_icon.click()
        print("---------------calendar_icon 222222222222----------------")
        
        day_xpath = "(//div[@class='oxd-calendar-date'])[30]"
        day_element = self.driver.find_element(By.XPATH, day_xpath)
        
        
        day_element.click()
    # def select_dates(self):
    #     self.from_date.click()
    #     self.select_date30.click()


       