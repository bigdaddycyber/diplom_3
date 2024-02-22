import allure
from locators import *
from pages.base_page import BasePage


class FeedPage(BasePage):
    
    
    @allure.step('Ожидание загрузки страницы Лента заказов')
    def check_for_feed_page_load(self):
        return self.wait_for_element_located(FeedPageLocators.FEED_ORDERS)


    @allure.step('Клик по первому заказу из ленты')
    def click_on_top_order_from_list(self):
        self.click_on_element(FeedPageLocators.FIRST_ORDER_FROM_FEED)


    @allure.step('Ожидание появление модального окна с заказом!')
    def wait_for_order_details_modal_window(self):
        return self.wait_for_element_located(FeedPageLocators.WINDOW_FIRST_ORDER)


    @allure.step('Всего заказов')
    def get_total_orders_counter_value(self):
        return self.return_text_in_element(FeedPageLocators.TOTAL_ORDERS)


    @allure.step('Всего заказов сегодня')
    def get_today_orders_counter_value(self):
        return self.return_text_in_element(FeedPageLocators.TODAY_ORDERS)


    @allure.step('Клик по логотипу по центру')
    def click_on_label_button(self):
        self.click_on_element(FeedPageLocators.LOGO_BUTTON)
