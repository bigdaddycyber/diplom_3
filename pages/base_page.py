from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def click_on_element(self, element):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(element)).click()

    def get_element_attribute(self, element, attr):
        return self.driver.find_element(*element).get_attribute(attr)

    def get_element_value_of_css_property(self, element, css_prop):
        return self.driver.find_element(*element).value_of_css_property(css_prop)

    def input_in_field(self, element, keys):
        self.driver.find_element(*element).send_keys(keys)

    def check_element_present(self, element):
        try:
            self.driver.find_element(*element)
        except NoSuchElementException:
            return False
        return True

    def wait_for_element_located(self, element):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, element)))
        return True

    def wait_for_element_to_be_clickable(self, element):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, element)))
        return True

    def wait_for_invisibility_of_element_located(self, element):
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element_located((By.XPATH, element)))
        return True

    def drag_and_drop_element(self, drag_element, drop_element):
        drag_element = self.driver.find_element(*drag_element)
        drop_element = self.driver.find_element(*drop_element)
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_element, drop_element)
        action.perform()

    def return_text_in_element(self, element):
        return self.driver.find_element(*element).text

    def wait_for_text_in_element(self, element, order_id):
        WebDriverWait(self.driver, 5).until(expected_conditions.text_to_be_present_in_element((By.XPATH, element), order_id))
        return True
