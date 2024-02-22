import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage



class TestProfile:
    @allure.title('Клик по кнопке лк на главной')
    def test_click_button_on_main_page(self, get_driver):
        page = MainPage(get_driver)
        page.click_button_lk()
        page = ProfilePage(get_driver)
        assert page.check_profile_page()

    @allure.title('Клик по кнопке история заказов')
    def test_click_orders_history_button(self, get_driver):
        page = MainPage(get_driver)
        page.click_button_lk()
        page = ProfilePage(get_driver)
        page.load_lk()
        page.click_orders_history_button()
        assert page.load_order_history()

    @allure.title(' Выход в ЛК')
    def test_click_logout_button(self, get_driver):
        page = MainPage(get_driver)
        page.click_button_lk()
        page = ProfilePage(get_driver)
        page.load_lk()
        page.click_logout_button()
        page = LoginPage(get_driver)
        assert page.load_login_page()