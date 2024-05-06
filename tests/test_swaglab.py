import pytest
from swaglab_pages.swaglab_login import SwagLabLogin
from tests.conftest import swag_base_url

@pytest.mark.usefixtures("browser_setup","log_on_failure")
class TestSwagLab:
    def setup_class(self):
        print("-------------Setup class-----------------")
        self.driver.get(swag_base_url)  # Use the defined variable
        self.swaglablogin = SwagLabLogin(self.driver)
    
        print("-------------Setup class-----------------")
    def test_login(self,user_data) :
        print("-------------Test Login-----------------")
        self.swaglablogin.login(user_data['swaglabs']['swag_username'],user_data['swaglabs']['swag_password'])
        # assert True == self.loginpage.empname_is_displayed()
        # self.loginpage.logout()

    def test_sort_products(self,user_data):
        print("-------------Test Sort Products-----------------")
        self.swaglablogin.sort_products()
        self.swaglablogin.enter_details_for_checkout(user_data['swaglabs']['first_name'],user_data['swaglabs']['last_name'],user_data['swaglabs']['postal_code'])
        
    def test_logout(self):
        print("-------------Test Logout-----------------")
        self.swaglablogin.logout()
        assert swag_base_url == self.driver.current_url
        print("-------------Logout Successfully-----------------")
        
   

    def test_invalid_login(self,user_data) :
        print("-------------Test Login with invalid credentials-----------------")

        self.swaglablogin.invalid_login(user_data['swaglabs']['swag_username'],user_data['swaglabs']['incorrect_password'])
        assert swag_base_url == self.driver.current_url
        self.driver.quit()