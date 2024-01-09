from webbrowser import Chrome

import pytest

from locators import Locators
from pages.HomePage import HomePage
from pages.ShopPage import ShopPage


@pytest.mark.usefixtures("setup")
class BaseClass:
    driver: Chrome

    def go_to_the_shop_page(self):
        self.driver.find_element(*Locators.HomePage.shop_page).click()
        return ShopPage(self.driver)

    def go_to_the_home_page(self):
        self.driver.find_element(*Locators.HomePage.home_page_icon).click()
        return HomePage(self.driver)

    def get_url(self):
        return self.driver.current_url

    def navigate_to_the_previous_page(self):
        self.driver.back()
