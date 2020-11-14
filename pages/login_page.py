"""
Модуль с проверками на странице регистрации
"""
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """
    Класс для страницы с входом или  регистрацией пользователя
    """
    def should_be_login_page(self):
        """
        Проверяем, что в url страницы есть слово 'login'
        Проверяем, что на странице есть форма для входа
        Проверяем, что на странице есть форма для регистрации
        """
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Login address is wrong"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def register_new_user(self, email, password):
        """
        Регистрирует нового пользователя
        """
        self.should_be_register_form()
        self.fill_text_box(*LoginPageLocators.REGISTER_EMAIL, email)
        self.fill_text_box(*LoginPageLocators.REGISTER_PWD_1, password)
        self.fill_text_box(*LoginPageLocators.REGISTER_PWD_2, password)
        self.click_button(*LoginPageLocators.REGISTER_BTN)
