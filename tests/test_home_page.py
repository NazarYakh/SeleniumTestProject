import time

from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_three_arrivals_only(self):
        shop_page = self.go_to_the_shop_page()
        shop_page_url = self.get_url()

        assert ("shop1" in shop_page_url, "Url should contain shop-word")
        print(shop_page_url)

