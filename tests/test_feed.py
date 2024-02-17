from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage
import allure


class TestFeed:

    @allure.title('Заказы из истории заказов в ленте заказов')
    def test_orders_from_user_profile_history(self, main_page_logged_in_with_created_order):
        self.driver = main_page_logged_in_with_created_order
        page = MainPage(self.driver)
        page.click_button_lk()
        page = ProfilePage(self.driver)
        page.click_orders_history_button()
        page.load_order_history()
        order_id_in_history = page.get_user_order_id_from_history()
        page.click_on_feed_button()
        page = FeedPage(self.driver)
        page.check_for_feed_page_load(order_id_in_history)

    @allure.title('Увеличение числа заказов')
    def test_total_orders_counters_increase_after_creating_order(self, main_page_logged_in):
        self.driver = main_page_logged_in
        page = MainPage(self.driver)
        page.check_main_page_load()
        page.click_feed_button()
        page = FeedPage(self.driver)
        page.check_for_feed_page_load()
        total_counter_0 = page.get_total_orders_counter_value()
        page.click_on_label_button()
        page = MainPage(self.driver)
        page.check_main_page_load()
        page.add_ingredient_to_order()
        page.click_create_order_button()
        page.click_feed_button()
        page = FeedPage(self.driver)
        page.check_for_feed_page_load()
        total_counter_1 = page.get_total_orders_counter_value()
        assert total_counter_1 > total_counter_0


    @allure.title('Отображение заказа в ленте заказов')
    def test_created_order_id_displayed_in_progress(self, main_page_logged_in):
        self.driver = main_page_logged_in
        page = MainPage(self.driver)
        page.check_main_page_load()
        page.add_ingredient_to_order()
        page.click_create_order_button()
        order_id = page.get_new_order_id()
        page.click_feed_button()
        page = FeedPage(self.driver)
        page.check_for_feed_page_load()
        assert page.check_for_feed_page_load(order_id)