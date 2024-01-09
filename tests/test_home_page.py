import time

from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_three_arrivals_only(self):
        shop_page = self.go_to_the_shop_page()
        shop_page_url = self.get_url()

        assert ("shop" in shop_page_url)

        home_page = self.go_to_the_home_page()
        arrivals_amount = len(home_page.get_arrivals())

        assert (arrivals_amount == 3)

