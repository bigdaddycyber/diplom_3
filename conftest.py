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
def driver(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    yield driver
    if driver is not None:
        driver.quit()


@pytest.fixture
def main_page(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver


@pytest.fixture
def login_page(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')
    yield driver


@pytest.fixture
def forgot_password_page(driver):
    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
    yield driver


@pytest.fixture
def main_page_logged_in(driver):
    email, password = generate_data.create_user()
    driver.get('https://stellarburgers.nomoreparties.site/login')
    page = LoginPage(driver)
    page.input_email(email)
    page.input_password(password)
    page.click_login_button()
    yield driver


@pytest.fixture
def main_page_log_with_created_order(driver):
    token, email, password = generate_data.create_user()
    generate_data.create_order_for_authorized_user(token)
    driver = driver
    driver.get('https://stellarburgers.nomoreparties.site/login')
    page = LoginPage(driver)
    page.input_email(email)
    page.input_password(password)
    page.click_login_button()
    yield driver


@allure.step('Открытие выбранного браузера на странице Лента заказов')
@pytest.fixture
def feed_page(driver):
    driver.get('https://stellarburgers.nomoreparties.site/feed')
    yield driver