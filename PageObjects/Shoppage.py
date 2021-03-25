from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import Checkout
from Shared.utilities import Utility


class Shop:

    shoppage_objects_dict = {}
    btn_checkout = (By.XPATH, '//div[@id="navbarResponsive"]//a')

    def __init__(self, driver):
        self.driver = driver
        self.utilities_object = Utility(self.driver)

    def add_item_to_cart(self, item_to_be_searched):
        count = 1
        shop_card = (By.XPATH, '//app-card'+'[{}]'.format(count)+'//h4[@class="card-title"]//a')
        try:
            while self.utilities_object.verify_element_displayed(shop_card):
                shop_card = (By.XPATH, '//app-card'+'[{}]'.format(count)+'//h4[@class="card-title"]//a')
                element_title = self.utilities_object.store_text_if_displayed(shop_card)
                if element_title == item_to_be_searched:
                    xpath_btn_add_to_cart = '//app-card'+'[{}]'.format(count)+'//div[@class="card-footer"]//button'
                    btn_add_to_cart = (By.XPATH, xpath_btn_add_to_cart)
                    self.utilities_object.click_element(btn_add_to_cart)
                    break
                count = count+1
        except WebDriverException:
            print("The element does not exist on this page")

    def checkout(self):
        Shop.shoppage_objects_dict['btn_checkout'] = self.driver.find_element(*Shop.btn_checkout)
        Shop.shoppage_objects_dict['btn_checkout'].click()
        checkout_object = Checkout(self.driver)
        return checkout_object
