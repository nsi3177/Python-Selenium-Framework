import pytest
from PageObjects.Homepage import Home
from Shared.utilities import Utility


@pytest.mark.usefixtures("browser_setup")
class TestFirstDemo:

    def test_demo_1(self, browser_setup):
        utilities_object = Utility(self.driver)
        homepage_object = Home(self.driver)
        homepage_object_dict = homepage_object.get_elements_from_home_page()
        brand_name = homepage_object_dict['brand_name']
        txt_brand_name = utilities_object.store_text_if_displayed(brand_name)
        assert txt_brand_name == "ProtoCommerce", "The brand name did not match"
        shoppage_object = homepage_object.click_Shop_btn()
        items_to_add = ["Blackberry", "Samsung Note 8"]
        for item in items_to_add:
            shoppage_object.add_item_to_cart(item)
        checkout_object = shoppage_object.checkout()
        checkout_object.checkout(items_to_add)