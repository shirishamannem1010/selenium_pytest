from selenium.webdriver.common.by import By
from actions.selenium_actions import Selenium_Actions
class LoginPage(Selenium_Actions):
    def __init__(self, driver):
        self.driver = driver
        
        self.myaccount=(By.XPATH,"//span[text()='My Account']")
        self.login=(By.XPATH,"(//a[text()='Login'])[1]")
        self.email_field=(By.ID,"input-email")
        self.password_field=(By.ID,"input-password")
        self.loginBtn=(By.XPATH,"//input[@class='btn btn-primary']")

        self.search_input=(By.XPATH,"//input[@class='form-control input-lg']")
        self.search_btn=(By.XPATH,"//button[@class='btn btn-default btn-lg']")

        self.select_product=(By.XPATH,"(//img[@class='img-responsive'])[2]")
        self.product_quantity=(By.ID,"input-quantity")
        self.add_to_cart=(By.XPATH,"//button[text()='Add to Cart']")

        self.cartBtn=(By.XPATH,"//span[@id='cart-total']")
        self.view_cart=(By.XPATH,"(//i[@class='fa fa-shopping-cart'])[3]")
        self.use_code=(By.XPATH,"(//a[@class='accordion-toggle collapsed'])[1]")

        self.estimate_shipping=(By.XPATH,"(//a[@class='accordion-toggle collapsed'])[2]")
        self.select_country=(By.XPATH,"(//select[@class='form-control'])[1]")
        self.select_state=(By.XPATH,"(//select[@class='form-control'])[2]")
    def click_myaccount(self):
        self.webelement_click(self.myaccount)
        self.webelement_click(self.login)
    def naveenautomationlabs_login(self,email,password):
        self.webelement_send_keys(self.email_field,email)
        self.webelement_send_keys(self.password_field,password)
        self.webelement_click(self.loginBtn) 
    def search_product(self,product):
        self.webelement_send_keys(self.search_input,product)
        self.webelement_click(self.search_btn)    
        print("-------------Product searched-------------")
    def select_products_cart(self):
        self.webelement_click(self.select_product)
        self.webelement_cleartext(self.product_quantity)
        # assert self.webelement_is_empty(self.product_quantity)
        print("-------------Product quantity is cleared-------------")
        self.webelement_send_keys(self.product_quantity,"2")
        assert self.webelement_get_attribute(self.product_quantity,"value") == "2"
        print("-------------Product selected-------------")

        self.webelement_is_isenabled(self.add_to_cart)
        self.webelement_click(self.add_to_cart)
        print("-------------Product added to cart-------------")
        
    def cart_list_items(self):
        self.webelement_click(self.cartBtn)
        self.webelement_click(self.view_cart)
        print("-------------Cart items displayed-------------")
        # self.webelement_click(self.use_code)
        # self.webelement_send_keys(self.use_code,"ABC123")
        print("-------------Code entered-------------")
        # assert self.webelement_get_attribute(self.use_code,"value") == "ABC123"
       
        # self.webelement_click(self.estimate_shipping)
        # self.webelement_select_dropdown(self.select_country,"India")
        # assert self.webelement_get_attribute(self.select_country,"value") == "99"
        # print("-------------Country selected-------------")
        # self.webelement_select_dropdown(self.select_state,"Telangana")
        # assert self.webelement_get_attribute(self.select_state,"value") == "4231"
        
      
    