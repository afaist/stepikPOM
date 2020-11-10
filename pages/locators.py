from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME      = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRODUCT_PRICE     = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    # информация в сообщении о добавлении в корзину
    PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_IN_MESSAGE   = (By.CSS_SELECTOR, \
        "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    # кнопка перехода в корзину
    TO_BASKET_LINK    = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    # информация из корзины
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, \
                         "#basket_formset > div > div > div.col-sm-4 > h3 > a")
    PRICE_IN_BASKET   = (By.CSS_SELECTOR, \
                         "#basket_formset > div > div > div.col-sm-1 > p")
