"""
Тесты главной страницы приложения
"""
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

# Ссылка на главную страницу приложения
BASE_LINK = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    """
    Класс с тестами входа пользователя
    """

    def setup_method(self):
        """
        Задаем ссылку для каждого метода
        """
        self.link = BASE_LINK

    def test_guest_can_go_to_login_page(self, browser):
        """
        Гость может перейти на страницу регистрации
        """
        # инициализируем Page Object, передаем в констурктор экземлпяр
        # драйвера и url
        page = MainPage(browser, self.link)
        # открываем страницу
        page.open()
        # выполняем метод страницы - переходим на страницу логина
        page.go_to_login_page()
        # Делаем проверки на странице логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        """
        Гость может видеть ссылку на страницу регистрации
        """
        page = MainPage(browser, self.link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Гость открывает главную страницу
    Переходит в корзину по кнопке в шапке сайта
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста
    """
    page = MainPage(browser, BASE_LINK)
    page.open()
    page.is_basket_link_present()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.there_is_a_message_that_the_basket_is_empty()
