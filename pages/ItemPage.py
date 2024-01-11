from locators import Locators


class ItemPage:
    def __init__(self, driver):
        self.driver = driver

    def get_description(self):
        return self.driver.find_element(*Locators.ItemPageLocators.product_description).text

