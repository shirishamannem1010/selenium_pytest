from actions.mobile_actions import Mobile_Appium_Actions
from appium.webdriver.common.appiumby import AppiumBy

class BigOvenLoginPage(Mobile_Appium_Actions):
    signin_button = (AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']");
    email_input = (AppiumBy.XPATH,"//android.widget.EditText[@resource-id='com.bigoven.android:id/email']");
    password_input = (AppiumBy.XPATH,"//android.widget.EditText[@resource-id='com.bigoven.android:id/password']");
    moreoptions_button = (AppiumBy.XPATH , "//android.widget.ImageView[@content-desc='More options']");
    settings_button = (AppiumBy.XPATH , "//android.widget.TextView[@text = 'Settings']");
    signout_button = (AppiumBy.XPATH , "//android.widget.TextView[@text='Sign Out']");
    confrim_signout_button = (AppiumBy.XPATH , "//android.widget.Button[@resource-id='android:id/button1']");

    search_button = (AppiumBy.XPATH , "//android.widget.Button[@content-desc='Search All Recipes']");
    search_input = (AppiumBy.XPATH , "//android.widget.AutoCompleteTextView[@resource-id='com.bigoven.android:id/searchBarText']");
    back_button = (AppiumBy.XPATH , "//android.widget.ImageButton[@content-desc='Navigate up']");



    def  __init__ (self, driver):
        super().__init__(driver);

    def  login_bigoven_app(self ,email,password) :
        self.click_webelement(self.signin_button);
        self.input_webelement(self.email_input,email);
        self.input_webelement(self.password_input,password);
        self.click_webelement(self.signin_button);
        

    def  logout_bigoven_app( self ) :
        self.click_webelement(self.moreoptions_button);
        self.click_webelement(self.settings_button);
        self.click_webelement(self.signout_button);
        self.click_webelement(self.confrim_signout_button);


    def search_item(self , search_text) :
        self.click_webelement(self.search_button);
        self.click_webelement(self.search_input);
        self.input_webelement(self.search_input,search_text);
        self.driver.execute_script('mobile: performEditorAction', {'action': 'search'})
        self.click_webelement(self.back_button);

    def invalid_login(self ,email,password) :
        self.click_webelement(self.signin_button);
        self.input_webelement(self.email_input,email);
        self.input_webelement(self.password_input,password);
        self.click_webelement(self.signin_button);