from selenium.webdriver.common.by import By
from actions.selenium_actions import Selenium_Actions

class SwagLabLogin(Selenium_Actions):
   
    username_input=(By.ID,"user-name") 
    password_input=(By.ID,"password")
    login_button=(By.ID,"login-button")
    sort_products_checkbox=(By.XPATH,"//select[@class='product_sort_container']")
    addtocart_bolt_tshirt=(By.XPATH,"(//button[@class='btn btn_primary btn_small btn_inventory '])[2]")
    sauce_bike_light=(By.XPATH,"(//div[@class='inventory_item_name '])[2]")
    bike_light_to_cart=(By.ID,"add-to-cart")
    cart_icon=(By.XPATH,"//a[@class='shopping_cart_link']")
    checkout_button=(By.XPATH,"//button[text()='Checkout']")
    first_name=(By.ID,"first-name")
    last_name=(By.ID,"last-name")
    postal_code=(By.ID,"postal-code")
    continue_button=(By.ID,"continue")

    menu_bar=(By.XPATH,"//button[@id='react-burger-menu-btn']")
    logout_button=(By.ID,"logout_sidebar_link")
  
    def __init__(self,driver):
      super().__init__(driver)

    def login(self,username,password):
        self.webelement_input(self.username_input,username)
        self.webelement_input(self.password_input,password)
        self.webelement_click(self.login_button)

    def sort_products(self):
        self.webelement_select_dropdown(self.sort_products_checkbox,"Price (low to high)")
        # self.webelement_click(self.addtocart_bolt_tshirt)
        self.webelement_click(self.sauce_bike_light)
        self.webelement_click(self.bike_light_to_cart)
        self.webelement_click(self.cart_icon)
        assert self.webelement_is_isenabled(self.checkout_button)
        self.webelement_click(self.checkout_button)

    def enter_details_for_checkout(self,first_name,last_name,zip_code):
        self.webelement_input(self.first_name,first_name)
        self.webelement_input(self.last_name,last_name)
        self.webelement_input(self.postal_code,zip_code)
        assert self.webelement_get_attribute(self.first_name,"value") == first_name
        assert self.webelement_is_isenabled(self.continue_button)
        self.webelement_click(self.continue_button)
        

    def logout(self):
        self.webelement_click(self.menu_bar)
        self.webelement_click(self.logout_button)

    def invalid_login(self,username,password):
        self.webelement_input(self.username_input,username)
        self.webelement_input(self.password_input,password)
        self.webelement_click(self.login_button)
        print("-------------Invalid Login-------------")   
    



        