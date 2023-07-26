#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://b2c.passport.rt.ru'

        super().__init__(web_driver, url)

    def is_authenticated(self):
        # Проверяем, что текущий URL содержит '/account_b2c'
        return '/account_b2c' in self.get_current_url()

    # Login button
    login_button = WebElement(xpath='//button[@id="kc-login"]')
    # Password recovery button
    password_recovery_button = WebElement(id='forgot_password')
    # Left side
    left_side = WebElement(xpath='//*[@id="page-left"]')
    # Right side
    right_side = WebElement(xpath='//*[@id="page-right"]')
    # Title left side
    search_title_left = WebElement(xpath='//html/body/div[1]/main/section[1]/div/div[2]/h2')
    # Auth_title
    auth_title = WebElement(xpath='//h1[@class="card-container__title" and text()="Авторизация"]')
    # Password_recovery_title
    password_recovery_title = WebElement(xpath='//h1[@class="card-container__title" and text()="Восстановление пароля"]')
    # Phone_tab
    phone_tab = WebElement(xpath='//*[@id="t-btn-tab-phone"]')
    # Login/Email/Ls/Phone field
    username_field = WebElement(id='username')
    # Password_field
    password_field = WebElement(id='password')
    # Continue_button_password_recovery_form
    continue_button_password_recovery_form = WebElement(id='reset')
    # Back_btn_password_recovery_form
    back_btn_password_recovery_form = WebElement(id='reset-back')
    # Captcha_field
    captcha_field = WebElement(id='captcha')
    # Captcha_picture
    captcha_picture = WebElement(xpath='//*[@class="rt-captcha__image"]')
    # Registration btn
    registration_btn = WebElement(id="kc-register")
    # Registration_title
    registration_title = WebElement(xpath='//h1[@class="card-container__title" and text()="Регистрация"]')
    # Registration btn
    registration_btn_accept = WebElement(xpath='//*[@class="rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded register-form__reg-btn"]')
    # Name field
    name_field = WebElement(name="firstName")
    # Lastname field
    lastname_field = WebElement(name="lastName")
    # Email/mobile phone field
    email_phone_field = WebElement(id='address')
    # Password confirm field
    password_confirm = WebElement(id='password-confirm')
    # Name error message
    name_error_message = WebElement(xpath='//html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/span')
    # Lastname error message
    lastname_error_message = WebElement(xpath='//html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/span')
    # Email or phone error message
    email_error_message = WebElement(xpath='//*[@class="rt-input-container__meta rt-input-container__meta--error"]')
    # Password error message
    password_error = WebElement(xpath='//*[@class="rt-input-container rt-input-container--error new-password-container__password"]')
    # Password recovery error message
    password_confirm_error = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    # Pop-up window
    popup_window = WebElement(xpath='//div[@class="card-modal__card-wrapper"]')
    # Alrdy exist title
    alrdy_exist_title = WebElement(xpath='//h2[@class="card-modal__title" and text()="Учётная запись уже существует"]')
    # GotoLogin btn
    go_to_login_btn = WebElement(xpath='//div[@name="gotoLogin" and text()="Войти"]')
    # Reset_pass_btn
    reset_pass_btn = WebElement(xpath='//div[@id="reg-err-reset-pass" and text()=" Восстановить пароль "]')