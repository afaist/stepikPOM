from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
import pyperclip


class BasePage():
    def __init__(self, browser, url:str, timeout=10):
        self.browser = browser
        self.url     = url
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
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))
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

