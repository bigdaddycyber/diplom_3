from locators import *
from pages.base_page import BasePage
import allure

class RecoveryPasswordPage(BasePage):
    
    @allure.step('Страница восстановления пароля')
    def check_password_recover_page(self):
        return self.check_element_present(RecoveryPasswordPageLocators.TEXT_PASSWORD_RECOVERY)


    @allure.step('Клик по вводe email')
    def click_email_input(self):
        self.click_on_element(RecoveryPasswordPageLocators.CLICK_EMAIL_INPUT)


    @allure.step('Ввод email')
    def input_email(self, email):
        self.input_in_field(RecoveryPasswordPageLocators.CLICK_EMAIL_INPUT, email)


    @allure.step('Клик по Восстановить пароль')
    def click_recover_button(self):
        self.click_on_element(RecoveryPasswordPageLocators.CLICK_BUTTON_RECOVERY)


    @allure.step('Ожидание закрытия формы восстановления')
    def check_password_header_gone(self):
        return self.wait_for_invisibility_of_element_located(RecoveryPasswordPageLocators.TEXT_PASSWORD_RECOVERY[1])

