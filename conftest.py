import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    #    driver = webdriver.Chrome(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless ")
    # or
    options.headless = True
    options.add_argument('--ignore-certificate-errors-spki-list')

    driver = webdriver.Chrome(
        options=options,
        service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()
