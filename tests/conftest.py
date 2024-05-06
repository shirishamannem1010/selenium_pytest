# import pytest
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from datetime import datetime
# from pathlib import Path
# import json
# import allure
# from allure_commons.types import AttachmentType
# import os
# import shutil 

# from appium import webdriver
# # from appium.webdriver.appium_service import AppiumService
# import configparser
# from typing import Dict, Any
# from appium.webdriver.appium_service import AppiumService
# from appium.options.common import AppiumOptions
# from selenium.webdriver.chrome.options import ChromeOptions

# swag_base_url = "https://www.saucedemo.com/"
# current_dir = os.path.dirname(os.path.abspath(__file__))
# config_path = os.path.join(current_dir,'..','', 'config.ini')
# @pytest.fixture(scope= "session")
# def browser_setup() :
#     global driver;
#     # service = Service(ChromeDriverManager().install());
#     # service = webdriver.Chrome();
#     chrome_options = webdriver.ChromeOptions();
#     chrome_options.add_experimental_option("detach",True);
#     # driver = webdriver.Chrome(service= service,options= chrome_options);
#     driver = webdriver.Chrome(options= chrome_options);
#     driver.maximize_window();
#     config = read_config();
#     baseUrl = config["base_url"]
#     driver.get(baseUrl);
#     yield driver;
#     driver.quit();

# #Allure Report
# @pytest.fixture()
# def log_on_failure(request):
#     yield
#     item = request.node
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(),name="failed_test",attachment_type=AttachmentType.PNG)

# @pytest.hookimpl(hookwrapper=True,tryfirst=True)
# def pytest_runtest_makereport(item,call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item,"rep_"+rep.when,rep)
#     return rep

# def clean_allure_reports(report_dir):
#     """
#     Clean previous generated Allure reports.

#     Args:
#         report_dir (str): Path to the directory containing the Allure reports.
#     """
#     if os.path.exists(report_dir):
#         try:
#             shutil.rmtree(report_dir)
#             print("Previous Allure reports deleted successfully.")
#         except Exception as e:
#             print(f"Error while deleting previous Allure reports: {e}")
#     else:
#         print("No previous Allure reports found.")

# # Example usage:
# report_directory = "allure_reports"
# clean_allure_reports(report_directory)


# #html report
# @pytest.hookimpl(tryfirst = True)
# def  pytest_configure(config) :
#     today = datetime.now()
#     report_dir = Path("htmlreports",today.strftime('%Y%m%d'))
#     report_dir.mkdir(parents= True,exist_ok= True)
#     pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
#     config.option.htmlpath = pytest_html
#     config.option.self_contained_html = True

# def pytest_html_report_title(report):
#     report.title = "NaveenAutomationLabs Test Report"


# @pytest.fixture
# def user_data():
#     with open('data/data.json',"r") as file :
#         data = json.load(file)
#     return data

# @pytest.fixture(scope="module", autouse=True)
# def teardown_module(request):
#     yield
#     # This code will execute after all tests in the module have run
#     # Quit the browser here
#     driver.quit()

# #  Mobile Automation Configurations
# def read_mobile_config() :
#     config = configparser.ConfigParser()
#     config.read(config_path)
#     if 'Mobile' in config:
#         mobile_config = config['Mobile']
#         return mobile_config
#     else:
#         raise Exception("Mobile section not found in config.ini")

# def read_config(ui_path=config_path, section='UI'):
#     parser = configparser.ConfigParser();
#     parser.read(ui_path, encoding='utf-8');
#     if parser.has_section(section):
#         config = dict(parser.items(section));
#     else:
#         raise ValueError(f"Section '{section}' not found in the config file.");
#     return config;
# #this fixture will provide the driver for the mobile application
# @pytest.fixture(scope= "session")
# def appium_driver_setup(request) :
#     mobile_config  = read_mobile_config()
#     # appium_server = AppiumService()
#     appium_server = AppiumService();
#     appium_server.start()

#     cap : Dict[str, Any] = {
#         "platformName": mobile_config["platformName"],
#         "appium:deviceName": mobile_config["deviceName"],
#         "appium:automationName": mobile_config["automationName"],
#         "appium:appPackage": mobile_config["appPackage"],
#         "appium:appActivity": mobile_config["appActivity"],
#         "appium:platformVersion": mobile_config["platformVersion"]
#     }
#     driver = webdriver.Remote(mobile_config["appium_server_url"], options=ChromeOptions().add_experimental_option('w3c', False).add_experimental_option('excludeSwitches', ['enable-logging']).add_experimental_option('useAutomationExtension', False).add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'}))
#     yield driver
#     driver.quit()
#     appium_server.stop()

# #this fixture will provide the data from the json file for the mobile application
# @pytest.fixture()
# def mobile_json_data() :
#     with open("./data/mobileapp.json","r") as file :
#         data = json.load(file)
#     return data;


import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from datetime import datetime
from pathlib import Path
import json
import allure
import configparser
import os
import requests
from allure_commons.types import AttachmentType
from typing import Any, Dict
from appium.webdriver.appium_service import AppiumService
from appium.options.common import AppiumOptions


current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir,'..','', 'config.ini')
swag_base_url = "https://www.saucedemo.com/"
#this fixture will provide the driver for the web application
@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    global driver
    # service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    # Pass the Service instance to webdriver.Chrome()
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    request.cls.driver.maximize_window()

#this fixture will take the screenshot of the failed test cases
@pytest.fixture(autouse= True)
def log_on_failure(request):
    yield
    item = request.node
    if hasattr(item, "rep_call") and hasattr(item.rep_call, "failed") and item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=allure.attachment_type.PNG)

#this fixture will provide the html report for the test cases
@pytest.hookimpl(hookwrapper= True , tryfirst= True)
def pytest_runtest_makereport(item,call) :
    outcome = yield;
    rep = outcome.get_result();
    setattr(item,"rep_"+rep.when,rep)
    return rep

#this fixture will provide the html report for the test cases
@pytest.hookimpl(tryfirst= True)
def  pytest_configure(config) :
    today = datetime.now();
    report_dir = Path("reports",today.strftime('%Y%m%d'));
    report_dir.mkdir(parents= True,exist_ok= True);
    pytest_html = report_dir / f"report_{today.strftime('%Y%m%d%H%M')}.html" ;
    config.option.htmlpath = pytest_html;
    config.option.self_contained_html = True;

#this fixture will provide the title for the html report
def pytest_html_report_title(report) :
    report.title = "Swaglab Test Report";

@pytest.fixture
def user_data():
    with open('data/data.json',"r") as file :
        data = json.load(file)
    return data

# this function will read the data in UI section in config file
def read_config(ui_path=config_path):
    parser = configparser.ConfigParser();
    parser.read(ui_path, encoding='utf-8');
    if parser.has_section():
        config = dict(parser.items());
    else:
        raise ValueError(f"Section '' not found in the config file.");
    return config;

#this function will provide the data in Mobile section in config file 
def read_mobile_config() :
    config = configparser.ConfigParser();
    config.read(config_path);
    if 'Mobile' in config:
        mobile_config = config['Mobile']
        return mobile_config
    else:
        raise Exception("Mobile section not found in config.ini")

#this fixture will provide the driver for the mobile application
@pytest.fixture(scope= "session")
def appium_driver_setup(request) :
    mobile_config  = read_mobile_config();
    appium_server = AppiumService();
    appium_server.start();

    cap : Dict[str, Any] = {
        "platformName": mobile_config["platformName"],
        "appium:deviceName": mobile_config["deviceName"],
        "appium:automationName": mobile_config["automationName"],
        "appium:appPackage": mobile_config["appPackage"],
        "appium:appActivity": mobile_config["appActivity"],
        "appium:platformVersion": mobile_config["platformVersion"]
    }

    driver = webdriver.Remote(mobile_config["appium_server_url"],options=AppiumOptions().load_capabilities(cap));
    yield driver
    driver.quit();
    appium_server.stop();

#this fixture will provide the data from the json file for the mobile application
@pytest.fixture()
def mobile_data() :
    with open("./data/mobiledata.json","r") as file :
        data = json.load(file)
    return data;
