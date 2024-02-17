from locators import *
#from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure


class ProfilePage(BasePage):
    
    
    @allure.step('Проверка лого gрофиля')
    def check_profile_page(self):
        return self.check_element_present(ProfilePageLocators.LOGO_PROFIL)


    @allure.step('Загрузка ЛК')
    def load_lk(self):
        return self.wait_for_element_located(ProfilePageLocators.LOGO_PROFIL)


    @allure.step('Клик по кнопке История заказов')
    def click_orders_history_button(self):
        self.click_on_element(ProfilePageLocators.BUTTON_HISTORY_ORDER)
        
    @allure.step('Клик по кнопке Лента заказов')
    def click_on_feed_button(self):
        self.click_on_element(MainPageLocators.CLICK_BUTTON_FEED)


    @allure.step('Загрузки истории заказов')
    def load_order_history(self):
        return self.wait_for_element_located(ProfilePageLocators.LIST_ORDER)


    @allure.step('Получить заказ из истории заказов')
    def get_user_order_id_from_history(self):
        return self.return_text_in_element(ProfilePageLocators.ORDER_ID)


    @allure.step('Клик по кнопке Выход')
    def click_logout_button(self):
        self.click_on_element(ProfilePageLocators.BUTTON_LOGOUT)
