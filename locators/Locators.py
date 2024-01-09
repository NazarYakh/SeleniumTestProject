from selenium.webdriver.common.by import By


class HomePage:
    alert_window = (By.CSS_SELECTOR, ".fc-cta-consent")
    shop_page = (By.XPATH, "//a[normalize-space()='Shop']")
    home_page_icon = (By.XPATH, "//img[@title='Automation Practice Site']")

