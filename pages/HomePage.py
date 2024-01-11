from selenium.webdriver.common.by import By

from locators import Locators
from pages.ItemPage import ItemPage
from pages.ShopPage import ShopPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_the_shop_page(self):
        self.driver.find_element(*Locators.HomePage.shop_page).click()
        return ShopPage(self.driver)

    def get_arrivals(self):
        return self.driver.find_elements(*Locators.HomePage.arrivals)

    def open_arrival(self, arrival):
        if arrival == "First":
            arrival = 0
        elif arrival == "Second":
            arrival = 1
        elif arrival == "Third":
            arrival = 2
        self.get_arrivals()[arrival].click()
        return ItemPage(self.driver)

    def select_arrival_by_name(self, arrival_name):
        item = (Locators.HomePage.arrival_by_name % arrival_name)
        self.driver.find_element(By.XPATH, item).click()
        return ItemPage(self.driver)
