from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType
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
        self.driver.find_element(By.ID, 'f').send_keys("-1")
        self.driver.find_element(By.XPATH, '//*[@id="search_form"]/button').click()
        act_title = self.driver.find_element(By.XPATH, '//*[@id="s0"]')

        if act_title == self.driver.find_element(By.XPATH, '//*[@id="s0"]'):
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_search", attachment_type=AttachmentType.png)
            self.driver.close()
            assert False





