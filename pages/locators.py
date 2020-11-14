"""
Модуль описывает пути к элементам соответствующих страниц
"""
from selenium.webdriver.common.by import By


class BasePageLocators():
    """
    Базовый класс для селекторов
    """
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    # ссылка перехода в корзину в шапке страницы
    BASKET_LINK = (
        By.CSS_SELECTOR,
        "div.basket-mini.pull-right.hidden-xs span.btn-group a.btn.btn-default"
    )
    # селектор для залогиненого пользователя
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    """
    Элементы на главной странице сайта
    """
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    """
    Элементы на странице регистрации
    """
    # форма входа
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    # форма регистрации
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PWD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PWD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR,
                    "#register_form.well button.btn.btn-lg.btn-primary")


class ProductPageLocators():
    """
    Элементы, используемые при добавлении продукта в корзину
    """
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR,
                         ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR,
                     "div.col-sm-6.product_main p.price_color")
    # информация в сообщении о добавлении в корзину
    PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR,
                          "div.alert-success.fade.in div.alertinner strong")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR,
                        "div.alert-info.fade.in div.alertinner p strong")
    # кнопка перехода в корзину
    TO_BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    # информация из корзины
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR,
                         "div.basket-items div.row div.col-sm-4 h3 a")
    PRICE_IN_BASKET = (
        By.CSS_SELECTOR,
        "div.basket-items div.row div.col-sm-1 p.price_color.align-right")
    # Сообщение о добавлении товара в корзину
    ALERT_ADD = (By.CSS_SELECTOR,
                 "div.alert-success:nth-child(1) > div.alertinner")


class BasketPageLocators():
    """
    Элементы, используемые на странице корзины
    """
    # форма для содержимого корзины, появляется, если корзина не пуста
    BASKET_FORM = (By.CSS_SELECTOR, "form#basket_formset")
    # строка содержимого в корзине (может быть несколько)
    BASKET_ITEM = (By.CSS_SELECTOR, "form#basket_formset div.basket-items")
    # информация о том, что корзина пуста
    BASKET_EMPTY_INFO = (By.CSS_SELECTOR,
                         "div.page_inner div.content div#content_inner p")
