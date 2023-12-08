# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTest():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test(self):
        self.driver.get("http://127.0.0.1:5500/home.html")
        self.driver.set_window_size(1552, 840)
        self.driver.find_element(By.ID, "searchInput").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "searchInput").send_keys("frozen")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(1)

        self.driver.find_element(By.LINK_TEXT, "Stranger Things").click()

        self.driver.find_element(By.CSS_SELECTOR, "h1").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "searchInput").click()
        self.driver.find_element(By.ID, "searchInput").send_keys("demon slayer")
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(2)
        element = self.driver.find_element(By.CSS_SELECTOR, "button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
