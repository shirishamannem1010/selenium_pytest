from conftest import naveenautomationlabs_url
from practice_pages.loginpage import LoginPage
import pytest

@pytest.mark.usefixtures("browser_setup","log_on_failure")
class TestPractice:
    def setup_class(self):
        self.driver.get(naveenautomationlabs_url)
        self.loginpage = LoginPage(self.driver)

    def test_login(self,user_data):
        self.loginpage.click_myaccount()
        # self.loginpage.naveenautomationlabs_login(user_data['email_id'],user_data['password'])
        self.loginpage.naveenautomationlabs_login(user_data['naveenautomationlabs']['email_id'], user_data['naveenautomationlabs']['password'])
        
    def test_select_product_tocart(self):
       print("-------------Test select Product for cart-----------------")
       self.loginpage.search_product("iphone")
       self.loginpage.select_products_cart()
       print(" printing title of the page : ", self.driver.title)
       self.driver.quit()
    # def test_cart_list(self):
    #     self.loginpage.cart_list_items()
    #     self.driver.quit()
