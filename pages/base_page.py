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


class BasePage():
    """
    Базовый класс для всех страниц
    """
    def __init__(self, browser, url: str, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        Открывает ссылку
        """
        self.browser.get(self.url)

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
            print(f"Your code: {alert_text}")
            alert.accept()
            code = alert_text.split(":")[-1]
            pyperclip.copy(code)
            print(f"Код {code} скопирован в буфер обмена.")
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
