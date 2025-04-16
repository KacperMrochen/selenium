import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
# import os 

# exclude_debug = os.getenv("SELENIUM_EXCLUDE_DEBUG", "false").lower()

class BasePage:

    def __init__(self, driver):
        self.driver = driver
    
    def wait_for_new_window_and_switch(self, old_windows, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.new_window_is_opened(old_windows)
        )
        new_window = [w for w in self.driver.window_handles if w not in old_windows][0]
        self.driver.switch_to.window(new_window)

    def wait_for_title(self, title_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.title_contains(title_part)
        )

    def verify_title_contains(self, expected_text, timeout=10):
        self.wait_for_title(expected_text, timeout)
        return expected_text in self.driver.title