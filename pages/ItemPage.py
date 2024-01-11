from locators import Locators


class ItemPage:
    def __init__(self, driver):
        self.driver = driver

    def get_description(self):
        return self.driver.find_element(*Locators.ItemPageLocators.product_description).text

    def get_product_name(self):
        return self.driver.find_element(*Locators.ItemPageLocators.product_name).text

    def go_to_reviews(self):
        self.driver.find_element(*Locators.ItemPageLocators.product_reviews).click()

    def get_product_name_from_reviews(self):
        return self.driver.find_element(*Locators.ItemPageLocators.product_name_in_reviews).text

