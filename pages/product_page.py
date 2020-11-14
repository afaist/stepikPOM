"""
Модуль проверок на странице продукта
"""
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """
    Класс для страницы продукта
    """
    def get_product_name(self):
        self.product_name = self.get_element_text(
            *ProductPageLocators.PRODUCT_NAME)
        print(f"Product name = '{self.product_name}'")

    def get_product_price(self):
        self.price = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)
        print(f"price = {self.price}")

    def should_be_see_add_to_basket_btn(self):
        """
        Есть кнопка Добавить в корзину
        """
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN),\
            "Button 'Add to basket' not present!"

    def should_be_click_btn_add_to_basket(self):
        """
        Добавляем в корзину текущий товар
        """
        self.click_button(*ProductPageLocators.ADD_TO_BASKET_BTN)

    def is_not_present_message_after_adding_to_basket(self):
        """
        Пользователь не видит сообщение об успешном добавлении
        продукта в корзину
        """
        assert self.is_not_element_present(
            *ProductPageLocators.ALERT_ADD
        ), "The message about adding to the cart is visible!"

    def is_dissappeared_message_about_adding_to_basket(self):
        """
        Не появляется сообщение об успехе добавления товара
        в корзину
        """
        assert self.is_disappeared(
            *ProductPageLocators.ALERT_ADD), "The message is appeared!!!"

    def is_product_in_basket_message(self):
        """
        Выбранный продукт добавлен в корзину
        Проверяется правильность наименования товара в сообщении
        о добавлении в корзину
        """
        product = self.get_element_text(
            *ProductPageLocators.PRODUCT_IN_MESSAGE)
        assert self.product_name == product, \
            "The name product in message about add to the basket is wrong!!!"

    def is_price_in_basket_message(self):
        """
        Цена продукта в сообщении о добавлнении в корзину правильная
        """
        price = self.get_element_text(*ProductPageLocators.PRICE_IN_MESSAGE)
        print(f"Price added to the basket: {price}")
        assert self.price == price, "The price in the basket is wrong!!!!"

    def should_be_go_to_basket(self):
        """
        Переходим в корзину
        """
        self.click_button(*ProductPageLocators.TO_BASKET_LINK)

    def is_product_in_basket_correct(self):
        """
        Проверяем, что в корзине находится нужный продукт
        """
        product = self.get_element_text(*ProductPageLocators.PRODUCT_IN_BASKET)
        print(f"Product in the basket: {product}")
        assert self.product_name == product, \
            "The name product in basket wrong!!!"

    def is_price_in_basket_correct(self):
        """
        Проверяем, что цена в корзине соответствует выбранной
        """
        price = self.get_element_text(*ProductPageLocators.PRICE_IN_BASKET)
        print(f"Price in the basket: {price}")
        assert self.price == price
