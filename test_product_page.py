"""
Тесты для класса страницы с выбранным продуктом
Проверяет:
    Доступность кнопки добавить в корзину
    Добавление товара в корзину
"""
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

BASE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/"
BOOK_LINK = "coders-at-work_207/"  # В основном работаем с этой книгой
PROMO_LINK = "?promo=newYear2019"


@pytest.mark.skip(reason="This doesn't need to be checked at this time")
@pytest.mark.parametrize('link', [
    "coders-at-work_207/?promo=offer0", "coders-at-work_207/?promo=offer1",
    "coders-at-work_207/?promo=offer2", "coders-at-work_207/?promo=offer3",
    "coders-at-work_207/?promo=offer4", "coders-at-work_207/?promo=offer5",
    "coders-at-work_207/?promo=offer6",
    pytest.param("coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    "coders-at-work_207/?promo=offer8", "coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    """
    Тестируем 10 страниц, ищем одну, на которой не проходит тест
    """
    page = ProductPage(browser, BASE_LINK + link)
    page.open()
    page.should_be_add_product_to_basket()


@pytest.mark.skip(reason="This doesn't need to be checked at this time")
def test_guest_can_add_product_to_basket_one_page(browser):
    """
    Проверяем, что пользователь может добавить продукт в корзину
    для одного сайта
    Задание 4.3.3
    """
    test_guest_can_add_product_to_basket(browser, BOOK_LINK + PROMO_LINK)


@pytest.mark.xfail(reason="Тестовое упражнение")
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser):
    """
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    page = ProductPage(browser, BASE_LINK + BOOK_LINK)
    page.open()
    page.should_be_see_add_to_basket_btn()
    page.should_be_click_btn_add_to_basket()
    page.is_not_present_message_after_adding_to_basket()


def test_guest_cant_see_success_message(browser):
    """
    Открываем страницу товара
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    page = ProductPage(browser, BASE_LINK + BOOK_LINK)
    page.open()
    page.is_not_present_message_after_adding_to_basket()


@pytest.mark.xfail(reason="Тестовое задание")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared
    """
    page = ProductPage(browser, BASE_LINK + BOOK_LINK)
    page.open()
    page.should_be_see_add_to_basket_btn()
    page.should_be_click_btn_add_to_basket()
    page.is_dissappeared_message_about_adding_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = BASE_LINK + "the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = BASE_LINK + "the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста
    """
    link = BASE_LINK + BOOK_LINK
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_empty()
    basket_page.there_is_a_message_that_the_basket_is_empty()


@pytest.mark.xfail()
def test_guest_can_see_product_in_basket_opened_from_product_page(browser):
    """
    Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке
    Ожидаем, что в корзине уже есть товары
    """
    link = BASE_LINK + BOOK_LINK
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_basket_not_empty()
