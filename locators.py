from selenium.webdriver.common.by import By



class MainPageLocators:
    BUTTON_LK = [By.XPATH, '//p[ text()="Личный Кабинет" ]']
    CLICK_BUTTON_CREATE_ORDER = [By.XPATH, '//button[ text()="Оформить заказ" ]']
    LOGO_CENTRE = [By.XPATH, '//div[ contains(@class, "header__logo") ]/a']
    CLICK_BUTTON_FEED = [By.XPATH, '//*[ text()="Лента Заказов" ]']
    BURGER_CONSTRUCTOR = [By.XPATH, '//ul[ contains(@class, "BurgerConstructor") ]/parent::section']
    ORDER_CONFIRMATION = [By.XPATH, '//p[ text()="идентификатор заказа" ]']
    ORDER_ID = [By.XPATH, '//p[ text()="идентификатор заказа"']



class IngredientsLocators:
    BULKA = [By.XPATH, '//*[ text()="Флюоресцентная булка R2-D3"']
    INGREDIENT_DETAIL = [By.XPATH, '//h2[ text()="Детали ингредиента" ]']
    CLOSE_INGREDIENT_DETAILS_MODAL_WINDOW_X_BUTTON = [By.XPATH, '//h2[ text()="Детали ингредиента" ]/parent::div/parent::div//button[ contains(@class, "Modal_modal__close") ]']
    BUN_1_COUNTER = [By.XPATH, '//*[ text()="Флюоресцентная булка R2-D3" ]/parent::a//p[ contains(@class, "counter") ]']
    
    
    
class LoginPageLocators:
    INPUT_EMAIL = [By.XPATH, '//input[ contains(@type, "text") ]'] 
    INPUT_PASSWORD = [By.XPATH, '//input[ contains(@type, "password") ]']
    BUTTON_REGISTRATION = '//a[ text() = "Зарегистрироваться" ]'
    LOGIN_BUTTON = [By.XPATH, '//button[ text() = "Войти" ]']
    CONSTRUCTOR_BUTTON = [By.XPATH, '//*[ text()="Конструктор" ]']
    RECOVERY_PASSWORD = [By.XPATH, '//a[ @href="/forgot-password" ]']
    
    
    
class RecoveryPasswordPageLocators:
    TEXT_PASSWORD_RECOVERY = [By.XPATH, "//h2[text()='Восстановление пароля')]"]
    CLICK_EMAIL_INPUT = [By.XPATH, '//div[@class, "input_type_text"]']
    CLICK_BUTTON_RECOVERY = [By.XPATH, '//button [text()="Восстановить"]']
    
    
    
class ProfilePageLocators:
    LOGO_PROFIL = [By.XPATH, "//a[ text()='Профиль' ]"]
    BUTTON_HISTORY_ORDER = [By.XPATH, "//a[ text()='История заказов' ]"]
    NAME_FIELD = [By.XPATH,'//label[ text()="Имя"]']
    LOGIN_FIELD = [By.XPATH,'//label[ text()="Логин"]']
    BUTTON_LOGOUT = [By.XPATH, "//button[ text()='Выход' ]"]
    LIST_ORDER = [By.XPATH, '//li[ contains(@class, "OrderHistory_listItem") ]']
    ORDER_ID = [By.XPATH, '//ul[ contains(@class, "OrderHistory_profileList") ]']
    
    
    
class ResetPasswordPageLocators:
    ENTER_CODE_FROM_EMAIL= [By.XPATH, "//label[@class, 'Введите код из письма' ]"]
    SHOW_PASSWORD_ICON = [By.XPATH, '//div[ contains(@class, "input__icon") ]']
    PASSWORD_INPUT_FIELD = [By.XPATH, "//label[ text()='Пароль' ]/parent::div"]      



class FeedPageLocators:
    FEED_ORDERS = [By.XPATH, '//h1[ text()="Лента заказов" ]']
    LOGO_BUTTON = [By.XPATH, '//div[ contains(@class, "header__logo") ]/a']
    TOTAL_ORDERS = [By.XPATH, '//p[ text()[contains (., "Выполнено за все время:")]']
    TODAY_ORDERS = [By.XPATH, '//p[ text()[contains (., "Выполнено за сегодня:")]']
    FIRST_ORDER_FROM_FEED = [By.XPATH, '//ul[ contains(@class, "OrderFeed_list") ]/li']
    WINDOW_FIRST_ORDER = [By.XPATH, '//div[ contains(@class, "Modal_modal__container_Wo2l") ]']