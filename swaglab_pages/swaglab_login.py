from selenium.webdriver.common.by import By
from actions.selenium_actions import Selenium_Actions

class SwagLabLogin(Selenium_Actions):
   
    username_input=(By.ID,"user-name") 
    password_input=(By.ID,"password")
    login_button=(By.ID,"login-button")
    sort_products_checkbox=(By.CLASS_NAME,"product_sort_container")
    
    def __init__(self,driver):
      super().__init__(driver)

    def login(self,username,password):
        self.webelement_input(self.username_input,username)
        self.webelement_input(self.password_input,password)
        self.webelement_click(self.login_button)

    def sort_products(self):
        self.webelement_select_dropdown(self.sort_products_checkbox,"Price (low to high)")
        