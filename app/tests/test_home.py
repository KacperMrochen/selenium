import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..utils.logger import Logger
from ..utils.props import ReadConfig
from ..pages.HomePage import HomePage
from ..pages.HomePage import BasePage

class TestHomePage:
    home_page_url = ReadConfig.get_base_url()
    logger = Logger.log_gen()

    def test_title_text(self, setup):
        self.driver = setup
        self.driver.get(self.home_page_url)

        home_page = HomePage(driver=self.driver)
        
        assert home_page.verify_title_contains("DEMOQA")

    def test_link(self, setup):
        self.driver = setup
        self.driver.get(self.home_page_url)

        home_page = HomePage(self.driver)
        home_page.click_banner()

        assert home_page.verify_title_contains("Tools QA - Selenium Training")