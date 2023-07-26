
import pytest
from pages.rostelekom import MainPage
from pages.elements import WebElement
import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('VALID_EMAIL')
valid_password = os.getenv('VALID_PASSWORD')
valid_name = os.getenv('VALID_NAME')
valid_lastname = os.getenv('VALID_LASTNAME')
valid_phone = os.getenv('VALID_PHONE')
invalid_password = os.getenv('INVALID_PASS')
invalid_email = os.getenv('INVALID_EMAIL')
invalid_name = os.getenv('INVALID_NAME')
invalid_lastname = os.getenv('INVALID_LASTNAME')
invalid_phone = os.getenv('INVALID_PHONE')
new_valid_email = os.getenv('VALID_EMAIL_NEW')
valid_ls = os.getenv('VALID_LS')
new_valid_phone = os.getenv('VALID_PHONE_NEW')
invalid_login = os.getenv('INVALID_LOGIN')


def test_check_main_page(web_browser):
    """ Make sure main page have all forms. """

    page = MainPage(web_browser)
    # Check page sides
    assert page.left_side.find() and page.right_side.find(), "Форма разделена неверно на два блока."
    # Auth title check
    assert "Авторизация" in page.auth_title.get_text(), "Слово 'Авторизация' не найдено на странице."
    # Password field check
    assert page.password_field.find(), "Поле ввода пароля не найдено."
    # Phone field in right side check
    assert "Телефон" in page.right_side.get_text(), "Поле ввода телефона не найдено"
    # Login field in right side check
    assert "Логин" in page.right_side.get_text(), "Поле ввода логина не найдено"
    # Email field in right side check
    assert "Почта" in page.right_side.get_text(), "Поле ввода почты не найдено"
    # Ls field in right side check
    assert "Лицевой счёт" in page.right_side.get_text(), "Поле ввода лицевого счета не найдено"
    # Active tab check
    class_attr = page.phone_tab.get_attribute("class")
    assert "rt-tab--active" in class_attr, "Форма авторизации через телефон не активна по умолчанию"


def test_auth_with_correct_phone_number(web_browser):
    """ Make sure u can log in with correct phone number"""

    page = MainPage(web_browser)

    # input data
    page.username_field = "valid_phone"
    page.password_field = "valid_password"

    page.login_button.click()
    page.wait_page_loaded()

    # check url
    link = page.get_current_url()


    assert "https://b2c.passport.rt.ru/account_b2c/page?state=" in link


def test_auth_with_correct_email(web_browser):
    """ Make sure u can log in with correct email  address"""

    page = MainPage(web_browser)

    # input data
    page.username_field = "valid_email"
    page.password_field = "valid_password"

    page.login_button.click()
    page.wait_page_loaded()

    # check url
    link = page.get_current_url()


    assert "https://b2c.passport.rt.ru/account_b2c/page?state=" in link


def test_auth_with_correct_login(web_browser):
    """ Make sure u can log in with correct login"""

    page = MainPage(web_browser)

    # input data
    page.username_field = "valid_login"
    page.password_field = "valid_password"

    page.login_button.click()
    page.wait_page_loaded()

    # check url
    link = page.get_current_url()


    assert "https://b2c.passport.rt.ru/account_b2c/page?state=" in link


def test_auth_with_not_correct_phone_number(web_browser):
    """ Make sure u can't log in with not correct phone number"""

    page = MainPage(web_browser)

    # input data
    page.username_field = "invalid_phone"
    page.password_field = "valid_password"

    page.login_button.click()
    page.wait_page_loaded()

    # check url
    link = page.get_current_url()


    assert  "https://b2c.passport.rt.ru/auth" in link


def test_auth_with_not_correct_email(web_browser):
    """ Make sure u can't log in with not correct email address"""

    page = MainPage(web_browser)

    # input data
    page.username_field = "invalid_email"
    page.password_field = "valid_password"

    page.login_button.click()
    page.wait_page_loaded()

    # check url
    link = page.get_current_url()


    assert  "https://b2c.passport.rt.ru/auth" in link


def test_auth_with_not_correct_login(web_browser):
    """ Make sure u can't log in with not correct login"""

    page = MainPage(web_browser)

    # input data
    page.username_field = "invalid_login"
    page.password_field = "valid_password"

    page.login_button.click()
    page.wait_page_loaded()

    # check url
    link = page.get_current_url()


    assert  "https://b2c.passport.rt.ru/auth" in link


def test_password_recovery_form_opens(web_browser):
    """ Make sure password recovery page are opens correctly"""

    page = MainPage(web_browser)

    # go to the password recovery page
    page.password_recovery_button.click()
    page.wait_page_loaded()

    # check url
    link = page.get_current_url()

    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?" in link


def test_check_password_recovery_form(web_browser):
    """ Make sure password recovery page have some forms"""

    page = MainPage(web_browser)

    # go to the password recovery page
    page.password_recovery_button.click()
    page.wait_page_loaded()

    # Password recovery page title
    assert "Восстановление пароля" in page.password_recovery_title.get_text(), "Словосочетание 'Восстановление пароля' не найдено на странице."
    # Check page sides
    assert page.left_side.find() and page.right_side.find(), "Форма разделена неверно на два блока."
    # Active tab check
    class_attr = page.phone_tab.get_attribute("class")
    assert "rt-tab--active" in class_attr, "Форма авторизации через телефон не активна по умолчанию."
    # Continue btn check
    assert page.continue_button_password_recovery_form.find(), "Кнопка 'Продолжить' не найдена."
    # Back btn check
    assert page.back_btn_password_recovery_form.find(), "Кнопка 'Вернуться назад' не найдена."
    # Captcha field check
    assert page.captcha_field.find(), "Поле ввода 'Символы' не найдено."
    # Captcha picture check
    assert page.captcha_picture.get_attribute("src"), "Отсутствует картинка 'Captcha'."


def test_back_btn_works(web_browser):
    """Make sure that the back button works properly"""

    page = MainPage(web_browser)

    # go to the password recovery page
    page.password_recovery_button.click()
    page.wait_page_loaded()

    # go back to auth page
    page.back_btn_password_recovery_form.click()
    page.wait_page_loaded()

    # check url
    link = page.get_current_url()

    assert "https://b2c.passport.rt.ru/auth" in link


def test_registration_form_opens(web_browser):
    """ Make sure registration page are opens correctly"""

    page = MainPage(web_browser)

    # go to the registration page
    page.registration_btn.click()
    page.wait_page_loaded()

    # check url
    link = page.get_current_url()

    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration" in link


def test_registration_form_have_all_field(web_browser):
    """ Make sure registration form have all fields"""

    page = MainPage(web_browser)

    # go to the registration page
    page.registration_btn.click()
    page.wait_page_loaded()

    # Check page sides
    assert page.left_side.find() and page.right_side.find(), "Форма разделена неверно на два блока."
    # Check registration page title
    assert "Регистрация" in page.registration_title.get_text(), "Слово 'Регистрация' не найдено на странице."
    # Name field in right side check
    assert "Имя" in page.right_side.get_text(), "Поле ввода имени не найдено."
    # Last name field in right side check
    assert "Фамилия" in page.right_side.get_text(), "Поле ввода фамилии не найдено."
    # Region field in right side check
    assert "Регион" in page.right_side.get_text(), "Поле ввода почты не найдено."
    # Email/mobile phone field in right side check
    assert "E-mail или мобильный телефон" in page.right_side.get_text(), "Поле ввода почты не найдено."
    # Password field in right side check
    assert "Пароль" in page.right_side.get_text(), "Поле ввода пароля не найдено."
    # Password check field in right side check
    assert "Подтверждение пароля" in page.right_side.get_text(), "Поле ввода для подтверждение пароля не найдено."
    # Registration btn check
    assert "Зарегистрироваться" in page.right_side.get_text(), "Кнопка 'Зарегистрироваться' не найдена."


def test_name_field(web_browser):
    """ Make sure  that the name field works properly"""

    page = MainPage(web_browser)

    # go to the registration page
    page.registration_btn.click()
    page.wait_page_loaded()

    # input data
    page.name_field = "valid_name"


    # click on registration btn
    page.registration_btn_accept.click()

    # check url
    link = page.get_current_url()
    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=" in link
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in page.name_error_message.get_text(), "Сообщение об ошибке не появилось."


def test_lastname_field(web_browser):
    """Make sure that the lastname field works properly"""

    page = MainPage(web_browser)

    # go to the registration page
    page.registration_btn.click()
    page.wait_page_loaded()

    # input data
    page.lastname_field = "valid_lastname"

    # click on registration btn
    page.registration_btn_accept.click()

    # check url
    link = page.get_current_url()

    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=" in link
    # Error message appears check
    assert "Необходимо заполнить поле кириллицей. От 2 до 30 символов." in page.lastname_error_message.get_text(), "Сообщение об ошибке не появилось."


def test_email_phone_field(web_browser):
    """Make sure that the email phone field works properly"""

    page = MainPage(web_browser)

    # go to the registration page
    page.registration_btn.click()
    page.wait_page_loaded()

    # input data
    page.email_phone_field = "valid_phone"

    # click on registration btn
    page.registration_btn_accept.click()

    # check url
    link = page.get_current_url()

    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=" in link
    # Error message appears check
    assert "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru" in page.email_error_message.get_text(), "Сообщение об ошибке не появилось."


def test_password_field(web_browser):
    """Make sure that the password field works properly"""

    page = MainPage(web_browser)

    # go to the registration page
    page.registration_btn.click()
    page.wait_page_loaded()

    # input data

    page.password_field = "valid_password"

    # click on registration btn
    page.registration_btn_accept.click()
    page.wait_page_loaded()

    # check url
    link = page.get_current_url()

    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=" in link
    # Error message appears check
    assert "Длина пароля должна быть не менее 8 символов" in page.password_error.get_text(), "Сообщение об ошибке не появилось."


def test_password_recovery_field(web_browser):
    """Make sure that the password recovery field works properly"""

    page = MainPage(web_browser)

    # go to the registration page
    page.registration_btn.click()
    page.wait_page_loaded()

    # input data
    page.password_field = "valid_password"
    page.password_confirm = "valid_password"

    # click on registration btn
    page.registration_btn_accept.click()
    page.wait_page_loaded()

    # check url
    link = page.get_current_url()

    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=" in link
    # Error message appears check
    assert "Длина пароля должна быть не менее 8 символов" in page.password_confirm_error.get_text(), "Сообщение об ошибке не появилось."


def test_success_registration(web_browser):
    """Make sure u can finish registration successfully"""

    page = MainPage(web_browser)

    # go to the registration page
    page.registration_btn.click()
    page.wait_page_loaded()

    # input data
    page.name_field = "valid_name"
    page.lastname_field = "valid_lastname"
    page.email_phone_field = "new_valid_email"
    page.password_field = "valid_email"
    page.password_confirm = "valid_email"

    # click on registration btn
    page.registration_btn_accept.click()
    page.wait_page_loaded()

    # check url
    link = page.get_current_url()

    assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?execution=" in link


def test_registration_alrdy_used_email(web_browser):
    """Make sure u cant create user with alrdy used email"""

    page = MainPage(web_browser)

    # go to the registration page
    page.registration_btn.click()
    page.wait_page_loaded()

    # input data
    page.name_field = "valid_name"
    page.lastname_field = "valid_lastname"
    page.email_phone_field = "valid_email"
    page.password_field = "valid_password"
    page.password_confirm = "valid_password"

    # click on registration btn
    page.registration_btn_accept.click()
    page.wait_page_loaded()

    # Password field check
    assert page.popup_window.find(), "Всплывающее окно не найдено."
    # Check alrdy exist title
    assert "Учётная запись уже существует" in page.alrdy_exist_title.get_text(), "Сообщение 'Учётная запись уже существует не найдено'"
    # Check go_to_login_btn
    assert page.go_to_login_btn.find, "Кнопка 'Войти'не найдена"
    # Check reset_pass_btn
    assert page.reset_pass_btn.find, "Кнопка 'Восстановить пароль' не найдена"


def test_registration_alrdy_used_phone(web_browser):
    """Make sure u cant create user with alrdy used phone"""

    page = MainPage(web_browser)

    # go to the registration page
    page.registration_btn.click()
    page.wait_page_loaded()

    # input data
    page.name_field = "valid_name"
    page.lastname_field = "valid_lastname"
    page.email_phone_field = "valid_phone"
    page.password_field = "valid_password"
    page.password_confirm = "valid_password"

    # click on registration btn
    page.registration_btn_accept.click()
    page.wait_page_loaded()

    # Password field check
    assert page.popup_window.find(), "Всплывающее окно не найдено."
    # Check alrdy exist title
    assert "Учётная запись уже существует" in page.alrdy_exist_title.get_text(), "Сообщение 'Учётная запись уже существует не найдено'"
    # Check go_to_login_btn
    assert page.go_to_login_btn.find, "Кнопка 'Войти'не найдена"
    # Check reset_pass_btn
    assert page.reset_pass_btn.find, "Кнопка 'Восстановить пароль' не найдена"

