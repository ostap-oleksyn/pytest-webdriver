import allure
from selenium.webdriver.common.by import By

from base_page import BasePage
from images_page import ImagesPage


class ResultsPage(BasePage):
    result_link = (By.CSS_SELECTOR, "h3 a")
    images_tab_link = (By.XPATH, "(.//div[@id='hdtb-msb-vis']//a)[1]")

    @allure.step
    def open_result_link(self, position):
        super().get_elements(self.result_link)[position - 1].click()

    def get_result_link_text(self, position) -> str:
        return super().get_elements(self.result_link)[position - 1].text

    @allure.step
    def switch_to_images_page(self):
        super().get_element(self.images_tab_link).click()
        return ImagesPage(self.driver)
