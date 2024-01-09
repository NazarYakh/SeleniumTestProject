from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from locators import Locators


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    def choose_delivery_location(self, country):
        self.driver.find_element(*Locators.ConfirmPage.delivery_location).send_keys(country)

    def wait_for_country_presence(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def select_country_from_dropdown(self, country):
        self.driver.find_element(By.LINK_TEXT, country).click()

    def select_term_and_conditions_checkbox(self):
        self.driver.find_element(*Locators.ConfirmPage.term_and_conditions_checkbox).click()

    def submit_order(self):
        self.driver.find_element(*Locators.ConfirmPage.purchase_button).click()

    def get_order_message(self):
        return self.driver.find_element(*Locators.ConfirmPage.order_message).text


