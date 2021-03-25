class Utility:
    def __init__(self, driver):
        self.driver = driver

    def click_element_if_displayed(self, element):
        if self.driver.find_element(*element):
            self.driver.find_element(*element).click()
        else:
            print("Element not found")

    def click_element(self, element):
        self.driver.find_element(*element).click()

    def verify_element_displayed(self, element):
        if self.driver.find_element(*element):
            return True
        else:
            return False

    def find_elements_if_displayed(self, element):
        if self.driver.find_elements(*element):
            return self.driver.find_elements(*element)
        else:
            print("No element like "+element+" found on the page")

    def store_text_if_displayed(self, element):
        if self.verify_element_displayed(element):
            return self.driver.find_element(*element).text
        else:
            print("Element "+element+" not found on the page")
