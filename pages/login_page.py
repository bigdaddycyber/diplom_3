from locators import *
from pages.base_page import BasePage
import allure



class LoginPage(BasePage):
    
    @allure.step('Ввод email')
    def input_email(self, email):
        self.input_in_field(LoginPageLocators.INPUT_EMAIL, email)


    @allure.step('Ввод пароля')
    def input_password(self, password):
        self.input_in_field(LoginPageLocators.INPUT_PASSWORD, password)


    @allure.step('Загрузка страницы авторизации')
    def load_login_page(self):
        return self.wait_for_element_located(LoginPageLocators.LOGIN_BUTTON)
    
    @allure.step('Клик на кнопке Войти')
    def click_login_button(self):
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)
        
    @allure.step('Клик по восстановить пароль')
    def click_recovery_password(self):
        self.click_on_element(LoginPageLocators.RECOVERY_PASSWORD)


