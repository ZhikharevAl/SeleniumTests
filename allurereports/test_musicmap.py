from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest


class TestMusicMaP:

    def test_title(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.music-map.com/")
        status = self.driver.find_element(By.XPATH, '//*[@id="the_title"]').is_displayed()
        if status:
            assert True
        else:
            assert False
        self.driver.close()
