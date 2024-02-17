from locators import *
from pages.base_page import BasePage
from data import ResetPasswordPageTestData
import allure


class ResetPasswordPage(BasePage):
    @allure.step('Cтраница сброса пароля')
    def wait_for_reset_password_page_loaded(self):
        return self.wait_for_element_located(ResetPasswordPageLocators.ENTER_CODE_FROM_EMAIL)

    #@allure.step('Проверка, что страница сброса пароля загружена')
    def check_reset_page_laoded(self):
        return self.check_element_present(ResetPasswordPageLocators.ENTER_CODE_FROM_EMAIL)

    #@allure.step('Ждать пока закончится анимация загрузки Modal_overlay')
    def wait_for_overlay_disappear(self):
        self.wait_for_invisibility_of_element_located(ResetPasswordPageLocators.MODAL_OVERLAY)

    #@allure.step('Клик на иконке Показать пароль')
    def click_show_password_button(self):
        self.click_on_element(ResetPasswordPageLocators.SHOW_PASSWORD_ICON)

    @allure.step('Проверка, что поле ввода пароля активно')
    def check_password_input_field_active(self):
        border = ResetPasswordPageTestData.active_field_border in self.get_element_value_of_css_property(
            ResetPasswordPageLocators.PASSWORD_INPUT_FIELD, 'border')
        active_field = ResetPasswordPageTestData.active_field_class in self.get_element_attribute(
            ResetPasswordPageLocators.PASSWORD_INPUT_FIELD, 'class')
        return border and active_field