"""
Модуль описывает параметры командной строки и
фикстуры pytest
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """
    Добавляем две опции в командную строку теста:
        --language - язык пользователя, по умолчанию - русский
        --browser_name - название браузера, по умолчанию - chrome
    """
    parser.addoption("--language",
                     action="store",
                     default="en",
                     help="Choose language for web page."
                     "Example: pytest --language=es test_items.py")
    parser.addoption("--browser_name",
                     action="store",
                     default="chrome",
                     help="Choose browser for test: 'chrome' or 'firefox'")


@pytest.fixture(scope="function")
def browser(request):
    """
    Настраиваем браузер и язык пользователя
    """
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    print("User language - {}".format(user_language))
    if user_language == "":
        # Пользователь использовал опцию --language, но не задал значение опции
        user_language = "ru"
    # переменная для браузера, browser уже используется в имени функции
    web_eng = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test...\n")
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        web_eng = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test...\n")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        web_eng = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield web_eng
    print("\nquit browser...")
    web_eng.quit()
