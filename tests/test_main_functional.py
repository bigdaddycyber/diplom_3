import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.feed_page import FeedPage


class TestMainFunctionality:
    
    @allure.title('Клик на конструктор')
    def test_click_constructor_button(self, driver):
        page = MainPage(driver)
        assert page.check_main_page_load()

    @allure.title('Клик на кнопку лента заказов')
    def test_click_feed_button(self, driver):
        page = MainPage(driver)
        page.check_main_page_load()
        page.click_feed_button()
        page = FeedPage(driver)
        assert page.check_for_feed_page_load()

    @allure.title('Клика на ингредиенты')
    def test_click_on_ingredient(self, driver):
        page = MainPage(driver)
        page.check_main_page_load()
        page.click_on_ingredient_bulka()
        assert page.load_window_with_ingredient()


    @allure.title('Заказ для зарегистрированного пользователя')
    def test_logged_in_user_order_creation(self, driver):
        page = MainPage(driver)
        page.check_main_page_load()
        page.add_ingredient_to_order()
        page.click_create_order_button()
        assert page.window_with_detail_order()