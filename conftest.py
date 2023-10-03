import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Choose browser language')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print("\nStarting browser...")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    yield browser

    print("\nQuitting browser..")
    browser.quit()
