import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser): # парсер инфы из параметров
    parser.addoption('--language', action='store', default="None",
                     help="Choose language")


@pytest.fixture(scope="function") # формирует фикстуру/ декоратор для работы с браузером
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

# Если возникают ошибки при работе то необходимо установить в виртуальное окружение версию pytest==7.1.1 с той что рекомендуется в курсе не работают Conftest4
# все либы есть в requirements.txt