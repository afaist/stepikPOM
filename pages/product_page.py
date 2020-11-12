from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_product_to_basket(self):
        """
        Выполняет всю работу по странице
        """
        self.get_product_name()
        self.get_product_price()
        self.should_be_see_add_to_basket_btn()
        self.should_be_click_btn_add_to_basket()
        self.solve_quiz_and_get_code()
        self.is_product_in_basket_message()
        self.is_price_in_basket_message()
        self.should_be_go_to_basket()
        self.is_product_in_basket_correct()
        self.is_price_in_basket_correct()

    def get_product_name(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        self.product_name = product.text
        print(f"Product name = '{self.product_name}'")

    def get_product_price(self):
        self.price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
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
        add_to_basket_btn = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

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
        product = self.browser.find_element(
            *ProductPageLocators.PRODUCT_IN_MESSAGE)
        print(f"Product added to the basket: {product.text}")
        assert self.product_name == product.text, \
            "The name product in message about add to the basket is wrong!!!"

    def is_price_in_basket_message(self):
        """
        Цена продукта в сообщении о добавлнении в корзину правильная
        """
        price = self.browser.find_element(
            *ProductPageLocators.PRICE_IN_MESSAGE)
        print(f"Price added to the basket: {price.text}")
        assert self.price == price.text, "The price in the basket is wrong!!!!"

    def should_be_go_to_basket(self):
        """
        Переходим в корзину
        """
        basket_link = self.browser.find_element(
            *ProductPageLocators.TO_BASKET_LINK)
        basket_link.click()

    def is_product_in_basket_correct(self):
        """
        Проверяем, что в корзине находится нужный продукт
        """
        product = self.browser.find_element(
            *ProductPageLocators.PRODUCT_IN_BASKET)
        print(f"Product in the basket: {product.text}")
        assert self.product_name == product.text, \
            "The name product in basket wrong!!!"

    def is_price_in_basket_correct(self):
        """
        Проверяем, что цена в корзине соответствует выбранной
        """
        price = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        print(f"Price in the basket: {price.text}")
        assert self.price == price.text
