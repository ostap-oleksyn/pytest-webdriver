from selenium.webdriver.common.by import By

from base_page import BasePage


class ImagesPage(BasePage):
    image = (By.CSS_SELECTOR, "#rg img")
