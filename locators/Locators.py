from selenium.webdriver.common.by import By


class HomePageLocators:
    alert_window = (By.CSS_SELECTOR, ".fc-cta-consent")
    shop_page = (By.XPATH, "//a[normalize-space()='Shop']")
    home_page_icon = (By.XPATH, "//img[@title='Automation Practice Site']")
    arrivals = (By.XPATH, "(//ul[@class='products'])")
    arrival_by_name = "//img[@title='%s']"


class ItemPageLocators:
    product_description = (By.CSS_SELECTOR, "div[id='tab-description'] p")
    product_name = (By.CSS_SELECTOR, ".product_title.entry-title")
    product_reviews = (By.CSS_SELECTOR, "a[href='#tab-reviews']")
    product_name_in_reviews = (By.CSS_SELECTOR, "#reply-title")


