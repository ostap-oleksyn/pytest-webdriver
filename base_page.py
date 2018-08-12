from typing import List

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    @allure.step("Navigate to {url}")
    def navigate_to(self, url):
        self.driver.get(url)

    def get_element(self, locator: tuple, timeout=5) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator), ' : '.join(locator))

    def get_elements(self, locator: tuple, timeout=5) -> List[WebElement]:
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator), ' : '.join(locator))
