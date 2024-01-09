from selenium.webdriver.support.select import Select

from locators import Locators
from pages.ShopPage import ShopPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_the_shop_page(self):
        self.driver.find_element(*Locators.HomePage.shop_page).click()
        return ShopPage(self.driver)

    def get_arrivals(self):
        return self.driver.find_elements(*Locators.HomePage.arrivals)




