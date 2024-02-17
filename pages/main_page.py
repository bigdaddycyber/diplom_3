from locators import *
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    

    @allure.step('Главная страница')
    def check_main_page_load(self):
        return self.check_element_present(MainPageLocators.LOGO_CENTRE)
    
    @allure.step('Клик по кнопке лента заказов')
    def click_feed_button(self):
        self.click_on_element(MainPageLocators.CLICK_BUTTON_FEED) 


    @allure.step('Клик по кнопке Личный кабинет')
    def click_button_lk(self):
        self.click_on_element(MainPageLocators.BUTTON_LK)
        

    @allure.step('Клик по кнопке Лента заказов')
    def click_button_feed(self):
        self.click_on_element(MainPageLocators.CLICK_BUTTON_FEED)
    

    @allure.step('Клик на кнопке Создать заказ')
    def click_create_order_button(self):
        self.click_on_element(MainPageLocators.CLICK_BUTTON_CREATE_ORDER)
        
    
    @allure.step('Клик на ингредиенте булка')
    def click_on_ingredient_bulka(self):
        self.click_on_element(IngredientsLocators.BULKA)
    
    
    @allure.step('Загрузка окна с описанием игредиента')
    def load_window_with_ingredient(self):
        return self.wait_for_element_located(IngredientsLocators.INGREDIENT_DETAIL)
    
    
    @allure.step('Добавить ингредиент булка 1 шт')
    def add_ingredient_to_order(self):
        self.drag_and_drop_element(IngredientsLocators.BULKA, MainPageLocators.BURGER_CONSTRUCTOR)


    @allure.step('Окно с деталями заказа')
    def window_with_detail_order(self):
        return self.wait_for_element_located(MainPageLocators.ORDER_CONFIRMATION)
    

    @allure.step('Получение номера созданного заказа')
    def get_new_order_id(self):
        return self.return_text_in_element(MainPageLocators.ORDER_ID)