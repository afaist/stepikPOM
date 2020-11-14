"""
Модуль для страницы корзины
"""
from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    """
    Класс для страницы с корзиной
    """
    def __init__(self, browser, url: str, timeout=10):
        super().__init__(browser, url, timeout)
        # Сообщения о пустой корзине на разных языках
        self.languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty.",
        }

    def is_basket_empty(self):
        """
        В корзине нет товаров
        2 способа проверки:
            1 - на странице нет формы, содержащей список товаров
            2 - нет ни одного элемента строки внутри формы
        """
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_FORM), "The basket is not empty!"
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEM,
            timeout=1), "The basket is not empty!"

    def is_basket_not_empty(self):
        """
        В корзине есть товары
        Проверяем:
            1 - есть форма, содержащая список товаров
            2 - есть хотя бы один элемент внутри формы
        """
        assert self.is_element_present(
            *BasketPageLocators.BASKET_FORM
        ), "There is no basket form on this page"
        assert self.is_element_present(
            *BasketPageLocators.BASKET_ITEM), "There is no items in basket"

    def there_is_a_message_that_the_basket_is_empty(self):
        """
        Есть сообщение о том, что корзина пустая
        """
        txt = self.get_element_text(*BasketPageLocators.BASKET_EMPTY_INFO)
        assert txt.startswith(self.languages[
            self.language]), "Message about empty basket is wrong!"
