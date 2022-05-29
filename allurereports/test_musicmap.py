import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


@allure.severity(allure.severity_level.NORMAL)
class TestMusicMaP:

    @allure.severity(allure.severity_level.MINOR)
    def test_title(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.music-map.com/")
        status = self.driver.find_element(By.XPATH, '//*[@id="the_title"]').is_displayed()
        if status:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_search(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.music-map.com/")
        self.driver.find_element(By.ID, 'f').send_keys("-1")
        self.driver.find_element(By.XPATH, '//*[@id="search_form"]/button').click()
        act_title = self.driver.title

        if act_title == "Music like Red - Similar Bands and Artists":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_authentication(self):
        pytest.skip('skipping test')
