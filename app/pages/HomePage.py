from selenium.webdriver.common.by import By
from .BasePage import BasePage

class HomePage(BasePage):
    banner_xpath = '//img[@class="banner-image"]'
    card_class_xpath = '//div[contains(@class, "card mt-4")]'

    def __init__(self, driver):
        self.driver = driver

    def get_cards(self):
        self.driver.find_elements(By.XPATH, self.card_class_xpath)

    def click_banner(self):
        old_windows = self.driver.window_handles
        self.driver.find_element(By.XPATH, self.banner_xpath).click()
        self.wait_for_new_window_and_switch(old_windows)