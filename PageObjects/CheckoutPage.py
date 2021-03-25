from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from Shared.utilities import Utility


class Checkout:

    btn_checkout = (By.XPATH, '//button[@class="btn btn-success"]')
    item_added = (By.XPATH, '//div[@class="media"]//h4[@class="media-heading"]')

    def __init__(self, driver):
        self.driver = driver
        self.utilities_object = Utility(self.driver)

    def checkout(self, items_added):
        count = 1
        item_row = (By.XPATH, '//tbody//tr[{}]'.format(count))
        try:
            while self.utilities_object.verify_element_displayed(item_row):
                # //tbody//tr[1]//h4//a
                media_heading = (By.XPATH, '//tbody//tr[{}]'.format(count)+'//h4//a')
                element_title = self.utilities_object.store_text_if_displayed(media_heading)
                print(element_title)
                assert element_title == items_added[count-1]
                count = count+1
                item_row = (By.XPATH, '//tbody//tr[{}]'.format(count))
        except WebDriverException:
            print("Elements have ended")


