from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.mobile_actions import Mobile_Appium_Actions
import time
class MobilePage(Mobile_Appium_Actions):
        skip_button=(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.TextView")
        login_link=(By.XPATH,"(//android.widget.TextView[@class='android.widget.TextView'])[4]")
        email_field=(By.XPATH,"(//android.widget.EditText[@class='android.widget.EditText'])[1]")
        password_field=(By.XPATH,"(//android.widget.EditText[@class='android.widget.EditText'])[2]")
        start_cooking_button=(By.XPATH,"(//android.view.ViewGroup[@class='android.view.ViewGroup'])[29]")
       
        skip_after_login=(By.XPATH,"(//android.widget.TextView[@class='android.widget.TextView'])[1]")
        gotit_button=(By.XPATH,"(//android.widget.TextView[@class='android.widget.TextView'])[10]")
       
        def __init__(self,driver):
            super().__init__(driver)
        def click_login_link(self):
            time.sleep(10)
            # self.click_webelement(self.skip_button)
            time.sleep(10)
            self.click_webelement(self.login_link)
            time.sleep(10)
            self.input_webelement(self.email_field,"demo@gmail.com")
            self.input_webelement(self.password_field,"Demo@123")
            self.click_webelement(self.start_cooking_button)

            # time.sleep(15)
            # self.click_webelement(self.skip_after_login)
            # time.sleep(10)
            # self.click_webelement(self.gotit_button) 
            # time.sleep(3)    

        def after_login(self):
            time.sleep(10)
            self.click_webelement(self.skip_after_login)
            time.sleep(5)
            self.click_webelement(self.gotit_button) 
            time.sleep(3)          