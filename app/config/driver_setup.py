import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def setup():
    options = Options()
    # options.add_argument("--headless=false") # if you want to test your script in local env. comment out this line and line below
    # options.add_argument("--no-sandbox") # here
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()