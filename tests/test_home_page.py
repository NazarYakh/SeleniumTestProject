from pages.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_three_arrivals_only(self):
        shop_page = self.go_to_the_shop_page()
        shop_page_url = self.get_url()

        assert "shop" in shop_page_url, "Url should contain shop-word"

        home_page = self.go_to_the_home_page()
        arrivals_amount = len(home_page.get_arrivals())

        assert arrivals_amount == 3, "Arrivals amount should be equal to 3"

    def test_images_should_navigate(self):
        home_page_url = self.get_url()
        shop_page = self.go_to_the_shop_page()
        shop_page_url = self.get_url()

        assert "shop" in shop_page_url, "Url should contain shop-word"

        home_page = self.go_to_the_home_page()
        arrivals_amount = len(home_page.get_arrivals())

        assert arrivals_amount == 3, "Arrivals amount should be equal to 3"

        home_page.open_arrival("First")
        first_arrival_url = self.get_url()
        assert first_arrival_url != home_page_url, "Url`s should be different"

        self.navigate_to_the_previous_page()

        home_page.open_arrival("Second")
        second_arrival_url = self.get_url()
        assert second_arrival_url != home_page_url, "Url`s should be different"

        self.go_to_the_home_page()

        current_url = self.get_url()

        assert current_url == home_page_url, "Seems like you are not on the home page"

    def test_description_match(self):
        part_of_description = 'HTML practically so that we can understand the markup of a web page'

        home_page = HomePage(self.driver)

        '''You can choose product by name ex. "'Thinking in HTML'"'''
        item_page = home_page.select_arrival_by_name('Thinking in HTML')

        product_description = item_page.get_description()

        assert part_of_description in product_description, \
            "Part of description were are looking for should be in Product description"

    def test_arrival_reviews(self):
        home_page = HomePage(self.driver)

        '''You can choose product by name ex. "Selenium Ruby"'''
        item_page = home_page.select_arrival_by_name('Selenium Ruby')

        product_name = item_page.get_product_name()
        item_page.go_to_reviews()
        product_name_in_reviews = item_page.get_product_name_from_reviews()

        assert product_name in product_name_in_reviews, "Product name should present be in Reviews tab"

