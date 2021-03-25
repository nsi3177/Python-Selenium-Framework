from selenium.webdriver.common.by import By

from PageObjects.Shoppage import Shop
from Shared.utilities import Utility


class Home:
    brand = (By.XPATH, '//nav//a[@class="navbar-brand"]')
    btn_shop = (By.XPATH, '//a[@href="/angularpractice/shop"]')

    def __init__(self, driver):
        self.driver = driver
        self.utilities_object = Utility(self.driver)

    def get_elements_from_home_page(self):
        home_page_elements = {}
        home_page_elements['brand_name'] = Home.brand
        home_page_elements['btn_shop'] = Home.btn_shop
        return home_page_elements

    def click_Shop_btn(self):

        self.utilities_object.click_element_if_displayed(Home.btn_shop)
        shop_object = Shop(self.driver)
        return shop_object