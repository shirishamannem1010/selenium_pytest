
# import pytest
# from pages.login import LoginPage
# from conftest import BaseUrl
# from pages.leaves import LeavePage
# @pytest.mark.usefixtures("browser_setup","log_on_failure")
# class TestOrangeHrm:
#     def setup_class(self):
#         print("-------------Setup class-----------------")
#         self.driver.get(BaseUrl)
#         self.loginpage = LoginPage(self.driver)
#         print("-------------Setup class-----------------")
        

#     def test_login(self,user_data) :
#         print("-------------Test Login-----------------")
#         self.loginpage.login(user_data['Username'],user_data['Password'])
#         # assert True == self.loginpage.empname_is_displayed()
#         self.loginpage.logout()

#     def test_apply_leaves(self,user_data):
#         print("-------------Test Apply Leave-----------------")
#         self.leavepage = LeavePage(self.driver)
#         self.loginpage = LoginPage(self.driver)
#         self.loginpage.login(user_data['Username'],user_data['Password'])

#         self.leavepage.navigate_to_leave()
#         self.leavepage.select_date_from_calendar()
#         # self.leavepage.select_dates()
#         self.driver.quit()
        
    