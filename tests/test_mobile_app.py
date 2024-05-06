import pytest
# from pages.sidechefloginpage import MobilePage
from pages.bigovenpages.bigoven_loginpage import BigOvenLoginPage
from tests.conftest import mobile_data, appium_driver_setup
from pages.bigovenpages.new_recipe import New_Recipe_Page
from pages.bigovenpages.all_navigation_elements import All_Navigation_Elements
# class TestSideChefMobileApp : 

#     # @pytest.mark.run()
#     def test_login_functionality(self,appium_driver_setup) :
#         driver = appium_driver_setup
#         driver.implicitly_wait(15);
#         mobilepage = MobilePage(driver)
#         mobilepage.click_login_link()
#         # mobilepage.after_login()
#         print ("Test Login Functionality")

#     def test_after_login(self,appium_driver_setup) :
#         driver = appium_driver_setup
#         driver.implicitly_wait(15);
#         mobilepage = MobilePage(driver)
#         mobilepage.click_login_link()
#         driver.implicitly_wait(2);
#         mobilepage.after_login()
#         print ("Test After Login Functionality")
    
class TestBigOvenMobileApp : 
    @pytest.mark.skip(reason="Skipping")
    def test_login_bigoven(self,appium_driver_setup,mobile_data) :
        driver = appium_driver_setup
        driver.implicitly_wait(5);
        login_page = BigOvenLoginPage(driver);
        login_page.login_bigoven_app(mobile_data['username'] , mobile_data['password']);
        login_page.logout_bigoven_app();
    
    @pytest.mark.skip(reason="Skipping")
    def test_search_item(self,appium_driver_setup,mobile_data) :
        driver = appium_driver_setup
        driver.implicitly_wait(5);
        login_page = BigOvenLoginPage(driver);
        login_page.login_bigoven_app(mobile_data['username'] , mobile_data['password']);
        search_page = BigOvenLoginPage(driver);
        search_page.search_item(mobile_data['searchdata']);
        login_page.logout_bigoven_app();

    @pytest.mark.skip(reason="Skipping")
    def test_invalid_login(self,appium_driver_setup,mobile_data) :
        driver = appium_driver_setup
        driver.implicitly_wait(5);
        login_page = BigOvenLoginPage(driver);
        login_page.invalid_login(mobile_data['invalid_username'] , mobile_data['invalid_password']);
    
        assert "The email or password you entered is incorrect" in driver.page_source, "The email or password you entered is incorrect"

    @pytest.mark.skip(reason="Skipping")
    def test_add_recipie_functionality(self,appium_driver_setup,mobile_data) :
        driver = appium_driver_setup
        login_page = BigOvenLoginPage(driver);
        new_recipe_page=New_Recipe_Page(driver);
        driver.implicitly_wait(5);
        login_page.login_bigoven_app(mobile_data['username'] , mobile_data['password']);  
        driver.implicitly_wait(10);
        new_recipe_page.add_new_recipe(mobile_data['title'],mobile_data['ingredients'],mobile_data['instructions']);
        login_page.logout_bigoven_app();

    def test_click_navbar_elements(self,appium_driver_setup,mobile_data) :
        driver = appium_driver_setup
        login_page = BigOvenLoginPage(driver);
        elements = All_Navigation_Elements(driver);
        login_page.login_bigoven_app(mobile_data['username'] , mobile_data['password']);
        elements.click_all_elements();
        login_page.logout_bigoven_app();
    
       
        