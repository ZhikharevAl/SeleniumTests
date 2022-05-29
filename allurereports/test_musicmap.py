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

    def test_search(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.music-map.com/")
        self.driver.find_element(By.ID, 'f').send_keys("Red")
        self.driver.find_element(By.XPATH, '//*[@id="search_form"]/button').click()
        act_title = self.driver.find_element(By.XPATH, '//*[@id="the_title"]')

        if act_title == self.driver.find_element(By.XPATH, '//*[@id="the_title"]'):
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False
