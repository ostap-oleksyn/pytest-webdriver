import allure
from selenium.webdriver.common.by import By

from base_page import BasePage
from results_page import ResultsPage


class SearchPage(BasePage):
    search_field = (By.ID, "lst-ib")

    @allure.step
    def open(self):
        super().navigate_to("https://google.com")
        return self

    @allure.step("search for {text}")
    def search_for(self, text):
        super().get_element(self.search_field).send_keys(text)
        super().get_element(self.search_field).submit()
        return ResultsPage(self.driver)
