"""
Тесты для класса страницы с выбранным продуктом
Проверяет:
    Доступность кнопки добавить в корзину
    Добавление товара в корзину
"""
import pytest
import mimesis  # Для генерации данных
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

# Используемые ссылки
BASE_LINK = "http://selenium1py.pythonanywhere.com/"
CATALOG_LINK = BASE_LINK + "catalogue/"
# В основном работаем с этой книгой
BOOK_LINK = CATALOG_LINK + "coders-at-work_207/"
# другая книга
BOOK1_LINK = CATALOG_LINK + "the-city-and-the-stars_95/"
PROMO_LINK = "?promo=newYear2019"


def generate_new_user():
    """
    Генерирует нового пользователя
    Возвращает email и password
    """
    person = mimesis.Person()
    return (person.email(), person.password(length=12))


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage():
    """
    Класс тестов с регистрацией пользователя
    """
    def setup_method(self):
        """
        Задаем ссылку для каждого метода
        """
        self.main_link = BASE_LINK
        self.book_link = BOOK_LINK

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """
        Выполняется для каждой функции:
            открыть страницу регистрации;
            зарегистрировать нового пользователя;
            проверить, что пользователь залогинен.
        """
        page = MainPage(browser, self.main_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, page.browser.current_url)
        login_page.register_new_user(*generate_new_user())
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """
        Пользователь может добавить продукт в корзину
        """
        page = ProductPage(browser, self.book_link)
        page.open()
        page.get_product_name()
        page.get_product_price()
        page.should_be_see_add_to_basket_btn()
        page.should_be_click_btn_add_to_basket()
        page.is_product_in_basket_message()
        page.is_price_in_basket_message()
        page.should_be_go_to_basket()
        page.is_product_in_basket_correct()
        page.is_price_in_basket_correct()

    def test_user_cant_see_success_message(self, browser):
        """
        Открываем страницу товара
        Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        """
        page = ProductPage(browser, self.book_link)
        page.open()
        page.is_not_present_message_after_adding_to_basket()


@pytest.mark.need_review
@pytest.mark.parametrize('link', [
    "?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3",
    "?promo=offer4", "?promo=offer5", "?promo=offer6",
    pytest.param("?promo=offer7",
                 marks=pytest.mark.xfail), "?promo=offer8", "?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    """
    Тестируем 10 страниц, ищем одну, на которой не проходит тест
    """
    page = ProductPage(browser, BOOK_LINK + link)
    page.open()
    page.get_product_name()
    page.get_product_price()
    page.should_be_see_add_to_basket_btn()
    page.should_be_click_btn_add_to_basket()
    page.solve_quiz_and_get_code()
    page.is_product_in_basket_message()
    page.is_price_in_basket_message()
    page.should_be_go_to_basket()
    page.is_product_in_basket_correct()
    page.is_price_in_basket_correct()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста
    """
    link = BOOK_LINK
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.there_is_a_message_that_the_basket_is_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = BOOK1_LINK
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


#################################################################
# Далее идут необязательные тесты
# ##############################################################
def test_guest_can_add_product_to_basket_one_page(browser):
    """
    Проверяем, что пользователь может добавить продукт в корзину
    для одного сайта
    Задание 4.3.3
    """
    test_guest_can_add_product_to_basket(browser, PROMO_LINK)


@pytest.mark.xfail(reason="Тестовое упражнение")
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser):
    """
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    page = ProductPage(browser, BOOK_LINK)
    page.open()
    page.should_be_see_add_to_basket_btn()
    page.should_be_click_btn_add_to_basket()
    page.is_not_present_message_after_adding_to_basket()


def test_guest_cant_see_success_message(browser):
    """
    Открываем страницу товара
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    page = ProductPage(browser, BOOK_LINK)
    page.open()
    page.is_not_present_message_after_adding_to_basket()


@pytest.mark.xfail(reason="Тестовое задание")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared
    """
    page = ProductPage(browser, BOOK_LINK)
    page.open()
    page.should_be_see_add_to_basket_btn()
    page.should_be_click_btn_add_to_basket()
    page.is_dissappeared_message_about_adding_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = BOOK1_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail()
def test_guest_can_see_product_in_basket_opened_from_product_page(browser):
    """
    Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке
    Ожидаем, что в корзине уже есть товары
    """
    link = BOOK_LINK
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_not_empty()
