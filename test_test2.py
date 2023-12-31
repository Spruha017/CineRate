# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTest():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test(self):
        a = ActionChains(self.driver)
        self.driver.get("http://127.0.0.1:5500/home.html")
        self.driver.set_window_size(1552, 840)
        time.sleep(2)
        self.driver.find_element(By.ID, "searchInput").click()
        self.driver.find_element(By.ID, "searchInput").send_keys("frozen")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(2)

        xpath_genres = "//div[@class='dropdown']/p[text()='Categories']"
        genres_element = self.driver.find_element(By.XPATH, xpath_genres)
        a.move_to_element(genres_element).perform()
        time.sleep(2)
        n = self.driver.find_element(By.LINK_TEXT, "TV Shows")
        a.move_to_element(n).perform()
        time.sleep(2)
        m = self.driver.find_element(By.LINK_TEXT, "Stranger Things")
        a.move_to_element(m).click().perform()
        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, "h1").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "searchInput").click()
        self.driver.find_element(By.ID, "searchInput").send_keys("demon slayer")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
        time.sleep(2)
        element = self.driver.find_element(By.CSS_SELECTOR, "button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
