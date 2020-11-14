"""
Этот модуль содержит описание базового класса
для всех страниц в проекте
"""
import math
import pyperclip
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage():
    """
    Базовый класс для всех страниц
    """
    def __init__(self, browser, url: str, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.language = "en"
        self.product_name = ""
        self.price = ""

    def open(self):
        """
        Открывает ссылку
        """
        self.browser.get(self.url)
        # выясняем язык пользователя
        self.language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language"
        )

    def is_element_present(self, how, what):
        """
        два аргумента:
            как искать (css, id, xpath и тд)
            и собственно что искать (строку-селектор)
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        """
        Переключается в окно alert
        Получает число для вычисления
        Вычисляет заданную функцию
        Вводит ответ в окне alert
        Нажимает кнопку OK в окне alert
        Нужна для выполнения задания 4.3.2
        """
        alert = self.browser.switch_to.alert
        x_value = alert.text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(float(x_value)))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print("Your code: {}".format(alert_text))
            alert.accept()
            code = alert_text.split(":")[-1]
            pyperclip.copy(code)
            print("Код {} скопирован в буфер обмена.".format(code))
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        """
        Проверяет, что элемент не появляется на странице в течение
        заданного времени
        """
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """
        Проверяет, что какой-то элемент исчезает
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        """
        Переход на страницу входа
        """
        self.click_button(*BasePageLocators.LOGIN_LINK)

    def should_be_login_link(self):
        """
        Проверяем, что есть ссылка на login
        """
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_basket_link_present(self):
        """
        Проверяем, что есть ссылка на корзину
        """
        assert self.is_element_present(
            *BasePageLocators.BASKET_LINK), "Basket link is not presented"

    def get_element(self, how, what):
        """
        Находит элемент на странице
        """
        try:
            element = self.browser.find_element(how, what)
        except NoSuchElementException:
            assert False, "Element not found!"
        return element

    def get_element_text(self, how, what) -> str:
        element = self.get_element(how, what)
        return element.text

    def fill_text_box(self, how, what, txt):
        """
        Заполняет элемент переданным текстом
        """
        element = self.get_element(how, what)
        element.clear()
        element.send_keys(txt)

    def click_button(self, how, what):
        """
        Находит кнопку или ссылку и кликает по ней
        """
        element = self.get_element(how, what)
        if element.is_displayed() and element.is_enabled():
            element.click()
        else:
            assert False, "Element is not displayed or enabled"

    def go_to_basket_page(self):
        """
        Переход на страницу корзины
        """
        self.click_button(*BasePageLocators.BASKET_LINK)

    def should_be_authorized_user(self):
        """
        Проверяем, что пользователь зарегистрирован
        """
        assert self.is_element_present(
            *BasePageLocators.USER_ICON
        ), "User icon is not presented, probably unauthorised user"
