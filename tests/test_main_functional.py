import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.feed_page import FeedPage


class TestMainFunctionality:
    
    @allure.title('Клик на конструктор')
    def test_click_constructor_button(self, login_page):
        self.driver = login_page
        page = LoginPage(self.driver)
        page = MainPage(self.driver)
        assert page.check_main_page_load()

    @allure.title('Клик на кнопку лента заказов')
    def test_click_feed_button(self, main_page):
        self.driver = main_page
        page = MainPage(self.driver)
        page.check_main_page_load()
        page.click_feed_button()
        page = FeedPage(self.driver)
        assert page.check_for_feed_page_load()

    @allure.title('Клика на ингредиенты')
    def test_click_on_ingredient(self, main_page):
        self.driver = main_page
        page = MainPage(self.driver)
        page.check_main_page_load()
        page.click_on_ingredient_bulka
        assert page.load_window_with_ingredient()


    @allure.title('Заказ для зарегистрированного пользователя')
    def test_logged_in_user_order_creation(self, main_page_logged_in):
        self.driver = main_page_logged_in
        page = MainPage(self.driver)
        page.check_main_page_load()
        page.add_ingredient_to_order()
        page.click_create_order_button()
        assert page.window_with_detail_order()