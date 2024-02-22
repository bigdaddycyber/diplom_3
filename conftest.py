import allure
import pytest
from selenium import webdriver
import generate_data
from pages.login_page import LoginPage
from pages.main_page import MainPage



def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', choices=("chrome", "firefox"))

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("browser")


@pytest.fixture
def get_driver(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    return driver


@pytest.fixture
def main_page(get_driver):
    driver = get_driver
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()


@pytest.fixture
def login_page(get_driver):
    driver = get_driver
    driver.get('https://stellarburgers.nomoreparties.site/login')
    yield driver
    driver.quit()


@pytest.fixture
def forgot_password_page(get_driver):
    driver = get_driver
    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
    yield driver
    driver.quit()


@pytest.fixture
def main_page_logged_in(get_driver):
    email, password = generate_data.create_user()
    driver = get_driver
    driver.get('https://stellarburgers.nomoreparties.site/login')
    page = LoginPage(driver)
    page.input_email(email)
    page.input_password(password)
    page.click_login_button()
    yield driver
    driver.quit()


@pytest.fixture
def main_page_log_with_created_order(get_driver):
    token, email, password = generate_data.create_user()
    generate_data.create_order_for_authorized_user(token)
    driver = get_driver
    driver.get('https://stellarburgers.nomoreparties.site/login')
    page = LoginPage(driver)
    page.input_email(email)
    page.input_password(password)
    page.click_login_button()
    yield driver
    driver.quit()


@allure.step('Открытие выбранного браузера на странице Лента заказов')
@pytest.fixture
def feed_page(get_driver):
    driver = get_driver
    driver.get('https://stellarburgers.nomoreparties.site/feed')
    yield driver
    driver.quit()