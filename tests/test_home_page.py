import time

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
