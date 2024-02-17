import generate_data
import allure
from pages.login_page import LoginPage
from pages.recovery_password_page import RecoveryPasswordPage



class TestPasswordRecovery:
    @allure.title('Клик по ссылке восстановить пароль')
    def test_click_on_password_recovery_link(self, login_page):
        self.driver = login_page
        page = LoginPage(self.driver)
        page.click_recovery_password()
        page = RecoveryPasswordPage(self.driver)
        assert page.check_password_recover_page()


    @allure.title('Cтраницу сброса пароля после ввода email')
    def test_input_email_and_click_recover_button(self, forgot_password_page):
        email = generate_data.create_user()
        self.driver = forgot_password_page
        page = RecoveryPasswordPage(self.driver)
        page.input_email(email)
        page.click_recover_button()
        page = RecoveryPasswordPage(self.driver)
        page.check_password_recover_page()
        assert page.check_password_recover_page()
        