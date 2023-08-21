import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launcing Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launcing Firefox Browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("launcing Edge Browser")

    else:
        print("Headless Mode")
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()

    driver.implicitly_wait(4)
        # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    return driver


def pytest_metadata(metadata):
    metadata["Environment"] = "Test"
    metadata["Project Name"] = "OrangeHRM"
    metadata["Module Name"] = "Employee"
    metadata["Tester"] = "Credence"
    # remove
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)


@pytest.fixture(params=[
    ("Admin","admin123", "Pass"),
    ("Admin1","admin123","Fail"),
    ("Admin","admin1231", "Fail"),
    ("Admin1","admin1231", "Fail")])

def getDataforlogin(request):
    return request.param
