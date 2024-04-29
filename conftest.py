import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from datetime import datetime
from pathlib import Path
import json
import allure
from allure_commons.types import AttachmentType
import os
import shutil 


BaseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
swag_base_url = "https://www.saucedemo.com/"
automation_practice_url="https://demo.automationtesting.in/Register.html"
demoqa_url = "https://demoqa.com/"
naveenautomationlabs_url = "https://naveenautomationlabs.com/opencart/"

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

#Allure Report
@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),name="failed_test",attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item,"rep_"+rep.when,rep)
    return rep

def clean_allure_reports(report_dir):
    """
    Clean previous generated Allure reports.

    Args:
        report_dir (str): Path to the directory containing the Allure reports.
    """
    if os.path.exists(report_dir):
        try:
            shutil.rmtree(report_dir)
            print("Previous Allure reports deleted successfully.")
        except Exception as e:
            print(f"Error while deleting previous Allure reports: {e}")
    else:
        print("No previous Allure reports found.")

# Example usage:
report_directory = "allure_reports"
clean_allure_reports(report_directory)


#html report
@pytest.hookimpl(tryfirst = True)
def  pytest_configure(config) :
    today = datetime.now()
    report_dir = Path("htmlreports",today.strftime('%Y%m%d'))
    report_dir.mkdir(parents= True,exist_ok= True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True

def pytest_html_report_title(report):
    report.title = "NaveenAutomationLabs Test Report"


@pytest.fixture
def user_data():
    with open('data/data.json',"r") as file :
        data = json.load(file)
    return data

# @pytest.fixture(scope="module", autouse=True)
# def teardown_module(request):
#     yield
#     # This code will execute after all tests in the module have run
#     # Quit the browser here
#     driver.quit()
